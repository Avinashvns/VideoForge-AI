class SpeechError(Exception):
    """Base Speech Exception"""
    pass


class TranscriptionError(SpeechError):
    """Transcription Failed"""
    pass