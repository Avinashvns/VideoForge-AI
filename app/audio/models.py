from dataclasses import dataclass


@dataclass
class AudioInfo:
    file_name: str
    file_path: str
    extension: str
    duration: float
    sample_rate: int
    channels: int