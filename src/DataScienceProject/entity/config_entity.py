from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir : Path = Path
    source_URL: str = str
    local_data_file: Path = Path
    unzip_dir: Path = Path


@dataclass
class DataValidationConfig:
    root_dir: Path = Path
    unzip_data_dir: Path = Path
    STATUS_FILE:str = str
    all_schema:dict = dict