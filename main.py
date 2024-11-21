
import whisper

model = whisper.load_model("base")  # Removed `weights_only`
result = model.transcribe('plant.wav')

print(result["text"])
