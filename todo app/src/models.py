# example code: Task-model
from dataclasses import dataclass
from datetime import date

@dataclass
class Task:
    id: int
    title: str
    category: str
    prority: str
    deadline: date
    done: bool = False
