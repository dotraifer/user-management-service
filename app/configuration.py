import yaml
from pydantic import BaseModel

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)


class DataBaseConfigurations(BaseModel):
    url: str


class Configurations(BaseModel):
    database: DataBaseConfigurations


Configurations = Configurations(**config)
