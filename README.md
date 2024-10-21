# SBX work meeting autumn 2004

Two hands-on examples for the SBX work meeting

## Running a whisper model on wombat

## Deploying a container on demo

1. Clone repository and enter container directory `git clone https://github.com/spraakbanken/work_meeting_autum_2024 && cd work_meeting_autumn_2024/container`
3. Build image `podman compose build
4. Start container in the background `podman compose up -d
5. Exclude from backup `touch ~/.local/.nobackup
6. Enable linger `loginctl enable-linger`
7. create .htaccess file e.g. in /export/htdocs/herbert/container
```
RewriteRule ^(.*)$ http://localhost:5000/$1 [P]
Header edit* Location "http://localhost:5000/" "http://demo.spraakdata.gu.se/herbert/container"
```
