# this module repackages encoded mp4 video files ( with av1 and opus)  
# three files are created. 
# example:  ${src_path}/stream.mp4  -> ${dest_path}/stream/stream.mpd
#                                      ${dest_path}/stream/stream_audio.webm 
#                                      ${dest_path}/stream/stream_video.mp4
#         
# finally in frontend ${dest_path}/stream/stream.mpd file is used to playback the file ${src_path}/stream.mp4


import os, secrets
import subprocess
import glob
from pathlib import Path

# ---- hardcoded default keys (test purposes only) ---- #
default_key_id = "0123456789abcdef0123456789abcdef"
default_key= "0123456789abcdef0123456789abcdef"




# ---- Dash Content Preparing Class ---- #
class Dash:
    def __init__(self, src_path, dest_path, kid=None, key=None):
        self.src_path = src_path
        self.dest_path = dest_path
        self.kid = kid or default_key_id
        self.key = key or default_key

# ----  generate encrypted dash content  ---- # 
    def run(self):
        if _is_key_valid(self.kid, self.key):
            files = os.listdir(self.src_path)
            for video in files:
                v_title, v_ext = os.path.splitext(video)
                input = self.src_path + "/" + video
                result = subprocess.run(f"packager input={input} --dump_stream_info | grep -w 'Audio' ", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                if result.returncode == 0:
                    subprocess.run(f"packager in={input},stream=audio,output={self.dest_path}/{v_title}/{v_title}-audio.webm,drm_label=AUDIO \
                    in={input},stream=video,output={self.dest_path}/{v_title}/{v_title}-video.mp4,drm_label=SD \
                    --allow_codec_switching \
                    --enable_raw_key_encryption \
                    --keys label=AUDIO:key_id={self.kid}:key={self.key},label=SD:key_id={self.kid}:key={self.key} \
                    --mpd_output {self.dest_path}/{v_title}/{v_title}.mpd ", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                else:
                    subprocess.run(f"packager  in={input},stream=video,output={self.dest_path}/{v_title}/{v_title}-video.mp4,drm_label=SD \
                    --allow_codec_switching \
                    --enable_raw_key_encryption \
                    --keys label=SD:key_id={self.kid}:key={self.key} \
                    --mpd_output {self.dest_path}/{v_title}/{v_title}.mpd ", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
        else:
            print("ERROR: key_id or key is invalid. Make sure they are hex strings with 32 characters")

# ----   set kid and key  ---- #
    def set_key(self, kid, key):
        self.kid = kid
        self.key = key 



# ----  generate random kid and key ---- #
    def gen_random_key(self):
        self.kid = secrets.token_hex(16)
        self.key = secrets.token_hex(16)

# ---- return kid and key ---- #
    def get_key(self):
        return { self.kid : self.key }

  






class DashReverse:
    def __init__(self):
        pass


# ----   decrypted dash content back to mp4 ---- # 
    def run(self, src_path, dest_path):
        if _is_key_valid(self.kid, self.key):
            if _is_path_valid(src_path, dest_path):
                mp4 = glob.glob(os.path.join(src_path,"*.mp4"))
                webm = glob.glob(os.path.join(src_path,"*.webm"))
                if len(mp4) == 1 and len(webm) == 1:
                    mp4, = mp4
                    webm, = webm
                    title = Path(mp4).stem
                    temp_webm = os.path.join(dest_path,"temp",f'{title}.webm')
                    temp_mp4 = os.path.join(dest_path,"temp",f'{title}.mp4')
                    output = os.path.join(dest_path,f'{title}.mp4')
                    try:
                        sp = subprocess.run(f"packager in={webm},stream=audio,output={temp_webm},drm_label=AUDIO \
                        in={mp4},stream=video,output={temp_mp4}.mp4,drm_label=SD \
                        --enable_raw_key_decryption \
                        --keys label=AUDIO:key_id={self.kid}:key={self.key},label=SD:key_id={self.kid}:key={self.key}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
                        if sp.returncode != 0:
                            print(sp.stderr)
                        else:
                            try:
                               fp = subprocess.run(f"ffmpeg -i {temp_webm} -i {temp_mp4} -c copy -map 0:a -map 1:v -strict -2 {output}",shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
                               if fp.returncode != 0:
                                    print(fp.stderr)
                                # todo # delete temp files 
                            except FileNotFoundError as e:
                                print(e)
                    except FileNotFoundError as e:
                        print(e)
                elif len(mp4) == 1 and len(webm) == 0:
                    mp4, = mp4
                    title = Path(mp4).stem
                    output = os.path.join(dest_path,f'{title}.mp4')
                    try:
                        sp = subprocess.run(f"packager in={mp4},stream=video,output={output},drm_label=SD \
                        --enable_raw_key_decryption \
                        --keys label=SD:key_id={self.kid}:key={self.key}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
                        if sp.returncode != 0:
                            print(sp.stderr)
                    except FileNotFoundError as e:
                        print(e)
                else:
                    print("ERROR: There must be only one pair of encrypted videos and audios or only one encrypted video")        
            else:
                 print("ERROR: make sure that source and destination folders exist")            
        else:
            print("ERROR: key_id or key is invalid. Make sure they are the ones used during encryption")

# ----   set kid and key  ---- #
    def set_key(self, kid, key):
        self.kid = kid
        self.key = key





# check if given paths are valid
def _is_path_valid(src_path, dest_path):
    if Path(src_path).exists() and Path(dest_path).exists():
        return True
    else:
        return False    


def _is_key_valid(kid, key):
    try:
        int(kid, 32) and int(key, 32)
        return True
    except ValueError:
        return False 