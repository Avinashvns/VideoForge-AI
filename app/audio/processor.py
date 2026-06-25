from pathlib import Path

from mutagen import File

from .constants import SUPPORTED_AUDIO_FORMATS
from .exceptions import AudioNotFound, UnsupportedAudioFormat
from .models import AudioInfo


class AudioProcessor:

    def load(self, file_path: str) -> Path:
        """
        Load audio file path.
        """

        path = Path(file_path)

        if not path.exists():
            raise AudioNotFound(f"Audio file not found: {file_path}")

        return path

    def validate(self, path: Path) -> None:
        """
        Validate audio extension.
        """

        if path.suffix.lower() not in SUPPORTED_AUDIO_FORMATS:
            raise UnsupportedAudioFormat(
                f"Unsupported format: {path.suffix}"
            )

    def get_info(self, file_path: str) -> AudioInfo:
        """
        Read audio metadata.
        """

        path = self.load(file_path)

        self.validate(path)

        audio = File(path)

        if audio is None:
            raise ValueError("Unable to read audio metadata.")

        info = audio.info

        sample_rate = getattr(info, "sample_rate", 0)
        channels = getattr(info, "channels", 0)

        return AudioInfo(
            file_name=path.name,
            file_path=str(path.resolve()),
            extension=path.suffix,
            duration=round(info.length, 2),
            sample_rate=sample_rate,
            channels=channels,
        )