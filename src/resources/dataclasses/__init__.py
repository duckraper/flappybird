from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ScoreRecord:
    id: int
    difficulty: str
    score: int
    date: str