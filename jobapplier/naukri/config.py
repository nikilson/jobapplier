# config.py
from dataclasses import dataclass

@dataclass
class NaukriConfig:
    username: str = ""
    password: str = ""
    url: str = ""
