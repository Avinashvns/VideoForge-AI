from dataclasses import dataclass, field
from typing import List


@dataclass
class Sentence:
    id: int
    text: str

    word_count: int = 0
    character_count: int = 0

    estimated_duration: float = 0.0

    scene_id: int = 0

    image_name: str = ""

    image_prompt: str = ""

    start_time: float = 0.0

    end_time: float = 0.0


@dataclass
class Paragraph:
    id: int
    sentences: List[Sentence] = field(default_factory=list)


@dataclass
class Script:
    title: str

    paragraphs: List[Paragraph] = field(default_factory=list)

    total_paragraphs: int = 0

    total_sentences: int = 0

    total_words: int = 0