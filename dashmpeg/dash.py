import os, secrets
import subprocess
import glob
from pathlib import Path
import logging

""" default key id and key value """
DEFAULT_KEY_ID = "0123456789abcdef0123456789abcdef"
DEFAULT_KEY = "0123456789abcdef0123456789abcdef"


logging.basicConfig(level=logging.ERROR)




""" ||||||||||||||||||||||||||||||||||| """
""" Create dash content from .mp4 files """
""" ||||||||||||||||||||||||||||||||||| """

class Dash:
    def __init__(self, src_path, dest_path, kid=None, key=None):
        self.src_path = src_path
        self.dest_path = dest_path
        self.kid = kid or DEFAULT_KEY_ID
        self.key = key or DEFAULT_KEY
        self.dash_folders = []
        self.mpd_paths = []
        self.recoved_file = ""


    """ generate encrypted dash content  """  
    def run(self):
        if not _is_key_valid(self.kid, self.key):
            logging.error(f"{self.kid} or {self.key} is invalid. Make sure they are hex strings with 32 characters")
            return
        if not _is_path_valid(self.src_path, self.dest_path):
            logging.error(f"Invalid or Non-existent path: {self.src_path} or {self.dest_path}")
            return
        videos = glob.glob(os.path.join(self.src_path,"*.mp4"))
        if len(videos) == 0:
            logging.error(f"There is not any .mp4 files found in {self.src_path}")
            return
        for video in videos:
            v_title = Path(video).stem
            input = self.src_path + "/" + video
            try:
                result = subprocess.run(f"packager input={input} --dump_stream_info | grep -w 'Audio' ", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except FileNotFoundError as e:
                logging.error(e)
            if result.returncode == 0:
                dest_webm = os.path.join(self.dest_path,v_title,f'{v_title}-audio.webm')
                dest_mp4 = os.path.join(self.dest_path,v_title,f'{v_title}-video.mp4')
                dash_folder = os.path.join(self.dest_path,v_title)
                mpd_file = os.path.join(dash_folder,f'{v_title}.mpd')
                sp = subprocess.run(f"packager in={input},stream=audio,output={dest_webm},drm_label=AUDIO \
                    in={input},stream=video,output={dest_mp4},drm_label=SD \
                    --allow_codec_switching \
                    --enable_raw_key_encryption \
                    --keys label=AUDIO:key_id={self.kid}:key={self.key},label=SD:key_id={self.kid}:key={self.key} \
                    --mpd_output {mpd_file} ", 
                    shell=True,  stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
                if sp.returncode != 0:
                    logging.error(sp.stderr)
                    return
                self.dash_folders.append(dash_folder)
                self.mpd_paths.append(mpd_file)    
            else:
                dest_mp4 = os.path.join(self.dest_path,v_title,f'{v_title}-video.mp4')
                dash_folder = os.path.join(self.dest_path,v_title)
                mpd_file = os.path.join(dash_folder,f'{v_title}.mpd')
                sp = subprocess.run(f"packager  in={input},stream=video,output={dest_mp4},drm_label=SD \
                    --allow_codec_switching \
                    --enable_raw_key_encryption \
                    --keys label=SD:key_id={self.kid}:key={self.key} \
                    --mpd_output {mpd_file} ", 
                    shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
                if sp.returncode != 0:
                    logging.error(sp.stderr)
                    return
                self.dash_folders.append(dash_folder)
                self.mpd_paths.append(mpd_file)  

    """  set kid and key  """
    def set_key(self, kid, key):
        self.kid = kid
        self.key = key 



    """  generate random kid and key  """
    def gen_random_key(self):
        self.kid = secrets.token_hex(16)
        self.key = secrets.token_hex(16)

    """ get kid and key  """
    def get_key(self):
        return [ self.kid , self.key ]

    """ get dash folders """
    """ used to recover dash content back to mp4 """
    def get_dash_folders(self):
        return self.dash_folders    

    """ get mpd paths """
    """ possibly used with shaka player """
    def get_mpd_paths(self):
        return self.mpd_paths



""" |||||||||||||||||||||||||||||||||||| """
""" Recreate mp4 files from dash content """
""" |||||||||||||||||||||||||||||||||||| """

class Recover:
    def __init__(self):
        pass

# ----   decrypted dash content back to mp4 ---- # 
    def run(self, src_path, dest_path):
        if not _is_key_valid(self.kid, self.key):
            logging.error(f"{self.kid} or {self.key} is invalid. Make sure they are hex strings with 32 characters")
            return
        if not _is_path_valid(src_path, dest_path):
            logging.error(f"Invalid or non-existent path: {src_path} or {dest_path}")
            return
        mp4 = glob.glob(os.path.join(src_path,"*.mp4"))
        webm = glob.glob(os.path.join(src_path,"*.webm"))
        vlen, alen = len(mp4), len(webm)
        if vlen == 1 and alen == 1:
            mp4, = mp4
            webm, = webm
            title = Path(mp4).stem
            title = title.split('-', 1)[0]
            temp_webm = os.path.join(dest_path,"temp",f'{title}.webm')
            temp_mp4 = os.path.join(dest_path,"temp",f'{title}.mp4')
            recovered_mp4 = os.path.join(dest_path,f'{title}.mp4')
            try:
                sp = subprocess.run(f"packager in={webm},stream=audio,output={temp_webm},drm_label=AUDIO \
                    in={mp4},stream=video,output={temp_mp4},drm_label=SD \
                    --enable_raw_key_decryption \
                    --keys label=AUDIO:key_id={self.kid}:key={self.key},label=SD:key_id={self.kid}:key={self.key}", 
                    shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
                if sp.returncode != 0:
                    logging.error(sp.stderr)
                    return    
                try:
                    fp = subprocess.run(f"ffmpeg -i {temp_webm} -i {temp_mp4} -c copy -map 0:a -map 1:v -strict -2 {recovered_mp4}",
                        shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
                    if fp.returncode != 0:
                        logging.error(fp.stderr)
                        return
                    self.recovered_file = recovered_mp4    
                    # TODO # delete temporary files 
                except FileNotFoundError as e:
                    logging.error(e)
            except FileNotFoundError as e:
                logging.error(e)
        elif vlen == 1 and alen == 0:
            mp4, = mp4
            title = Path(mp4).stem
            recovered_mp4 = os.path.join(dest_path,f'{title}.mp4')
            try:
                sp = subprocess.run(f"packager in={mp4},stream=video,output={recovered_mp4},drm_label=SD \
                    --enable_raw_key_decryption \
                    --keys label=SD:key_id={self.kid}:key={self.key}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
                if sp.returncode != 0:
                    logging.error(sp.stderr)
                    return
                self.recovered_file = recovered_mp4        
            except FileNotFoundError as e:
                logging.error(e)
        else:
            logging.error(f"{src_path} must contain one pair of a/v stream files or single v stream file")                
            return


    """   set kid and key  """
    def set_key(self, kid, key):
        self.kid = kid
        self.key = key

    """ get recovered mp4 files paths """
    def get_recovered(self):
        return self.recoved_files

""" ||||||||||||||||| """
""" Utility functions """
""" ||||||||||||||||| """

"""  check if given paths are valid """
def _is_path_valid(src_path, dest_path):
    if Path(src_path).exists() and Path(dest_path).exists():
        return True
    else:
        return False    

"""  check if key are valid """
def _is_key_valid(kid, key):
    try:
        int(kid, 32) and int(key, 32)
        return True
    except ValueError:
        return False 