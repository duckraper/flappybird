from datetime import datetime
from typing import List, Union, Dict

from dataclass_csv import DataclassReader, DataclassWriter

from src.core.game.settings import DATA_DIR
from src.resources.dataclasses import ScoreRecord


class ScoreManager:
    def __init__(self, game):
        self.file_path: 'Path' = DATA_DIR / 'scores.csv'
        self.scores: List[Dict['str', Union[str, int]]] = []
        self.game: 'Game' = game
        self.load_scores()

    def initialize_file(self):
        if not self.file_path.exists():
            cols = ','.join(ScoreRecord.__annotations__.keys())
            with open(self.file_path, 'w') as f:
                f.write(cols + '\n')

    def load_scores(self):
        self.initialize_file()

        with open(self.file_path, 'r') as f:
            reader = DataclassReader(f, ScoreRecord)
            for row in reader:
                record = row.__dict__
                self.scores.append(record)

    def save_score(self, score: int):
        new_record = ScoreRecord(
            id=len(self.scores) + 1,
            score=score,
            difficulty=self.game.difficulty,
            date=str(datetime.now())  # str(datetime.now().strftime('%H:%M:%S %d-%m-%Y'))
        )
        self.scores.append(new_record.__dict__)

    def save_scores_to_file(self):
        with open(self.file_path, mode='w') as f:
            writer = DataclassWriter(f, [
                ScoreRecord(**record)
                for record in self.scores
            ], ScoreRecord)
            writer.write()

    def get_top_scores(self, li: int = 0, ls: int = 5) -> List[Dict]:
        scores = sorted([
            score
            for score in self.scores
            if score['difficulty'] == self.game.difficulty
        ],
            key=lambda score: score['score'],
            reverse=True
        )

        return scores[li: ls]

    def get_highest_score(self) -> int:
        return max((
            score['score']
            for score in self.scores
            if score['difficulty'] == self.game.difficulty
        ),
            default=0
        )
