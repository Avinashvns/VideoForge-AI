from dataclasses import dataclass


@dataclass
class AudioInfo:
    file_name: str
    file_path: str
    extension: str
    duration: float
    sample_rate: int
    channels: int


    @property
    def duration_str(self) -> str:
        minutes = int(self.duration // 60)
        seconds = int(self.duration % 60)
        return f"{minutes:02}:{seconds:02}"