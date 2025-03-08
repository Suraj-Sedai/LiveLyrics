import pyaudio
import wave

def record_audio(output_filename="recorded_clip.wav", record_seconds=10, sample_rate=44100, channels=1):
    audio = pyaudio.PyAudio()

    # Set up recording stream
    stream = audio.open(format=pyaudio.paInt16, channels=channels,
                        rate=sample_rate, input=True,
                        frames_per_buffer=1024)

    print("Recording for", record_seconds, "seconds...")
    frames = []

    for _ in range(0, int(sample_rate / 1024 * record_seconds)):
        data = stream.read(1024)
        frames.append(data)

    print("Recording finished.")

    # Stop and close stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio to a file
    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

    print(f"Audio saved as {output_filename}")

# Record a 10-second audio clip
record_audio()


