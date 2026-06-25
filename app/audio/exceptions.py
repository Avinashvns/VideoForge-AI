class AudioError(Exception):
    """Base Audio Exception"""
    pass


class UnsupportedAudioFormat(AudioError):
    """Unsupported audio format"""
    pass


class AudioNotFound(AudioError):
    """Audio file not found"""
    pass