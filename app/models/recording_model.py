from dataclasses import dataclass

@dataclass
class Recording:
    audio_id: int
    audio_title: str
    audio_timestamp: str
    audio_path: str
    audio_size: int
    audio_duration: int
