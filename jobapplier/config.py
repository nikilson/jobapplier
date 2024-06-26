# config.py
from dataclasses import dataclass, field
from naukri import NaukriConfig

@dataclass
class JobPreferences:
    location: str = ""
    maximum_lpa: str = ""
    minimum_lpa: str = ""
    role: str = ""
    skill_sets: list = field(default_factory=list)


@dataclass
class BaseConfig:
    driver: str
    job_preferences: JobPreferences = field(default_factory=JobPreferences)

    naukri: NaukriConfig = field(default_factory=NaukriConfig)
