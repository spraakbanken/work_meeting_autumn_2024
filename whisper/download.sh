curl -L https://sverigesradio.se/topsy/ljudfil/srse/9174000.mp3 --output - | ffmpeg -i - -to 00:03:00 input.mp3
