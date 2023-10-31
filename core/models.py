from dataclasses import dataclass, field
from typing import List


@dataclass
class Catalog:
    filename: str
    data: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.length = len(self.data)
