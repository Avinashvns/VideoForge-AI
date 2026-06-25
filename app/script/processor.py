from pathlib import Path

from .constants import SUPPORTED_SCRIPT_FORMATS
from .exceptions import (
    ScriptNotFound,
    UnsupportedScriptFormat,
)
from .models import Script, Paragraph, Sentence


class ScriptProcessor:

    def load(self, file_path: str) -> Path:

        path = Path(file_path)

        if not path.exists():
            raise ScriptNotFound(file_path)

        if path.suffix.lower() not in SUPPORTED_SCRIPT_FORMATS:
            raise UnsupportedScriptFormat(path.suffix)

        return path

    def read(self, file_path: str) -> str:

        path = self.load(file_path)

        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    
    def clean(self, text: str) -> str:
        """
        Clean raw script text.
        """

        # Normalize punctuation
        text = text.replace("。", "।")

        lines = []

        for line in text.splitlines():

            line = " ".join(line.split())

            if line:
                lines.append(line)

        return "\n\n".join(lines)


    def validate(self, text: str) -> None:
        """
        Validate script content.
        """

        if not text.strip():
            raise ValueError("Script is empty.")

    def process(self, file_path: str):

        text = self.read(file_path)
        text = self.clean(text)

        self.validate(text)

        paragraphs = []

        sentence_id = 1
        total_words = 0
        total_duration = 0.0

        from .constants import WORDS_PER_MINUTE

        for paragraph_index, paragraph_text in enumerate(
            text.split("\n\n"),
            start=1
        ):

            paragraph_text = paragraph_text.strip()

            if not paragraph_text:
                continue

            paragraph = Paragraph(id=paragraph_index)

            raw_sentences = paragraph_text.split("।")

            for raw_sentence in raw_sentences:

                raw_sentence = raw_sentence.strip()

                if not raw_sentence:
                    continue

                words = raw_sentence.split()

                duration = (
                    len(words) / WORDS_PER_MINUTE
                ) * 60

                clean_sentence = (
                    raw_sentence
                    .replace("。", "।")
                    .rstrip("।.")
                )

                sentence = Sentence(

                    id=sentence_id,

                    text=clean_sentence + "।",

                    word_count=len(words),

                    character_count=len(clean_sentence),

                    estimated_duration=round(duration, 2)

                )

                paragraph.sentences.append(sentence)

                total_words += len(words)

                total_duration += duration

                sentence_id += 1

            paragraphs.append(paragraph)

        script = Script(

            title="Untitled",

            paragraphs=paragraphs,

            total_paragraphs=len(paragraphs),

            total_sentences=sentence_id - 1,

            total_words=total_words

        )

        return script