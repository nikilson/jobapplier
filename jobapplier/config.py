# config.py
from dataclasses import dataclass, field
from naukri import NaukriConfig

@dataclass
class BaseConfig:
    driver: str
    naukri: NaukriConfig = field(default_factory=NaukriConfig)

