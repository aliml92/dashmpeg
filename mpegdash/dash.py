# this module repackages encoded mp4 video files ( with av1 and opus)  
# three files are created. 
# example:  ${src_path}/stream.mp4  -> ${dest_path}/stream/stream.mpd
#                                      ${dest_path}/stream/stream_audio.webm 
#                                      ${dest_path}/stream/stream_video.mp4
#         
# finally in frontend ${dest_path}/stream/stream.mpd file is used to playback the file ${src_path}/stream.mp4


import os, secrets
import subprocess

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
        if self.__is_key_valid():
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

# ----  check key validitiy (private method) ---- #
    def __is_key_valid(self):
        try:
            int(self.kid, 32) and int(self.key, 32)
            return True
        except ValueError:
            return False     






class DashReverse:
    def __init__(self):
        pass


# ----  generate encrypted dash content  ---- # 
    def run(self, src_path, dest_path):
        if self.__is_key_valid():
            files = os.listdir(src_path)
            if len(files) == 2:
                f_t1, f_ext1 = os.path.splitext(files[0])
                f_t2, f_ext2 = os.path.splitext(files[1])
                t1 = t2 = f_t1.split('-', 1)[0]
                if f_ext1 == "webm":
                    a = src_path + "/" + files[0]
                else:    
                    v = src_path + "/" + files[1]
                subprocess.run(f"packager in={a},stream=audio,output={dest_path}/temp/{f_title}.webm,drm_label=AUDIO \
                in={v},stream=video,output={dest_path}/temp/{f_title}.mp4,drm_label=SD \
                --enable_raw_key_decryption \
                --keys label=AUDIO:key_id={self.kid}:key={self.key},label=SD:key_id={self.kid}:key={self.key}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.run(f"ffmpeg -i {dest_path}/temp/{f_title}.webm -i {dest_path}/temp/{f_title}.mp4 -c copy -map 0:a -map 1:v -strict -2 {dest_path}/{f_title}.mp4",shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            else:
                v =  src_path + "/" + files[0]
                v_t, v_ext = os.path.splitext(files[0])
                v_t = v_t.split('-', 1)[0]
                subprocess.run(f"packager  in={v},stream=video,output={dest_path}/{v_t}.mp4,drm_label=SD \
                --enable_raw_key_decryption \
                --keys label=SD:key_id={self.kid}:key={self.key}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
        else:
            print("ERROR: key_id or key is invalid. Make sure they are the ones used during encryption")

# ----   set kid and key  ---- #
    def set_key(self, kid, key):
        self.kid = kid
        self.key = key



# ----  check key validitiy (private method) ---- #
    def __is_key_valid(self):
        try:
            int(self.kid, 32) and int(self.key, 32)
            return True
        except ValueError:
            return False     

