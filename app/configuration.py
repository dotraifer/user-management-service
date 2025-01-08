import yaml
from pydantic import BaseModel

# Load the configuration from the YAML file
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)


class DataBaseConfigurations(BaseModel):
    """
    Schema for database configurations.

    Attributes:
        url (str): The URL of the database.
    """
    url: str


class Configurations(BaseModel):
    """
    Schema for application configurations.

    Attributes:
        database (DataBaseConfigurations): The database configurations.
    """
    port: int = 8000
    host: str = "0.0.0.0"
    cache_size: int = 200
    database: DataBaseConfigurations


# Initialize the Configurations object with the loaded configuration
Configurations = Configurations(**config)
