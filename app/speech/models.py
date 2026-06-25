from dataclasses import dataclass
from typing import List


@dataclass
class Segment:
    start: float
    end: float
    text: str


@dataclass
class Transcript:
    language: str
    duration: float
    segments: List[Segment]