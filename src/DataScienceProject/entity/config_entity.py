from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir : Path = Path
    source_URL: str = str
    local_data_file: Path = Path
    unzip_dir: Path = Path