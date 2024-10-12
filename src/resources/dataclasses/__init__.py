from dataclasses import dataclass


@dataclass
class ScoreRecord:
    id: int
    difficulty: str
    score: int
    date: str
