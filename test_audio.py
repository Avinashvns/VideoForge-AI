from app.audio import AudioProcessor

processor = AudioProcessor()

info = processor.get_info(
    "assets/voice/test.mp3"
)

print(info)
print(info.duration_str)