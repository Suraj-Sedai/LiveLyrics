from dejavu import Dejavu
from dejavu.recognize import FileRecognizer

# Database configuration
config = {
    "database": {
        "host": "localhost",
        "user": "root",
        "passwd": "password",
        "db": "dejavu"
    }
}

# Initialize Dejavu
djv = Dejavu(config)

# Recognize song from the recorded clip
song = djv.recognize(FileRecognizer, "recorded_clip.wav")
print("Recognized Song:", song)
