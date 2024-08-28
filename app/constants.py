from pathlib import Path
from enum import Enum

class WorkingPath(Enum):
    ROOT = Path(__file__).parent.parent