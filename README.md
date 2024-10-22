# SBX work meeting autumn 2004

Two hands-on examples for the SBX work meeting

## Running a whisper model on wombat
Hint: Don't do this in you home folder to speed up everything

1. Clone repository and enter container directory `git clone https://github.com/spraakbanken/work_meeting_autumn_2024 && cd work_meeting_autumn_2024/whisper`
2. touch .nobackup
3. Create virtual environment `virtualenv env && . ./env/bin/activate`
4. Install pytorch `pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121`
5. Install all other dependencies `pip install -r requirements.txt`
6. Download demo data `bash download.sh`
7. Run transcription `LD_PRELOAD=./env/lib/python3.9/site-packages/nvidia/cudnn/lib/libcudnn.so.9 python transcribe.py input.mp3`
   
## Deploying a container on demo

1. Clone repository and enter container directory `git clone https://github.com/spraakbanken/work_meeting_autumn_2024 && cd work_meeting_autumn_2024/container`
3. Build image `podman compose build
4. Start container in the background `podman compose up -d
5. Exclude from backup `touch ~/.local/share/containers/.nobackup
6. Enable linger `loginctl enable-linger`
7. create .htaccess file e.g. in /export/htdocs/herbert/container
```
RewriteRule ^(.*)$ http://localhost:5000/$1 [P]
Header edit* Location "http://localhost:5000/" "http://demo.spraakdata.gu.se/herbert/container"
```
