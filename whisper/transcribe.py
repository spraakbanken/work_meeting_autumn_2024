import sys
from pathlib import Path
import stable_whisper

if __name__ == "__main__":
    audio_path = sys.argv[1]
    srt_path = Path(audio_path).stem + ".srt"
    model = stable_whisper.load_model('base')
    result = model.transcribe(audio_path)
    result.to_srt_vtt(srt_path)