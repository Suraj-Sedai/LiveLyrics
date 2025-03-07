import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import requests
import config  # Import API credentials

def recognize_song(audio_file):
    url = config.ACR_HOST
    headers = {"Authorization": f"Bearer {config.API_KEY}"}
    files = {"sample": open(audio_file, "rb")}
    
    print("🔍 Identifying song...")
    response = requests.post(url, headers=headers, files=files)
    data = response.json()
    
    if "metadata" in data and "music" in data["metadata"]:
        song = data["metadata"]["music"][0]
        title, artist = song["title"], song["artists"][0]["name"]
        return f"🎶 {title} by {artist}"
    return "❌ No match found!"

# print(recognize_song("sample.wav"))


def record_audio(filename="sample.wav", duration=5, samplerate=44100):
    print("🎤 Recording...")
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype=np.int16)
    sd.wait()  # Wait until recording is finished
    write(filename, samplerate, audio_data)
    print("✅ Recording saved as", filename)

record_audio()
