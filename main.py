
import whisper

model = whisper.load_model("base")  # Removed `weights_only`
result = model.transcribe('erp_and_crm.wav')

print(result["text"])
