from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class BaseConfig:
    data: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        for key, value in self.data.items():
            setattr(self, key, value)
    
    def get(self, key):
        return self.data.get(key)
    
    def set(self, key, value):
        self.data[key] = value
        setattr(self, key, value)


config = {
    "CameraModel" : "Gh0st X900",
    "Lens" : "gh 40.2mp",
    "FocalLength" : "40.2",
    "ISO" : "100",
    "ShutterSpeed" : "1/60",
    "Aperture" : "2.8",
    "ExposureCompensation" : "0",
    "Flash" : "Off",
    "WhiteBalance" : "Auto",
    "Artist": "Salman S",
    "OwnerName": "Gh0st"
}

gh0st_config = BaseConfig(config)

