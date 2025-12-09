from pydantic_settings import BaseSettings


class GlobalConfig(BaseSettings):
    UUID_LENGTH: int = 32


class DevConfig(GlobalConfig):
    ENVIRONMENT: str = "ENVIRONMENT NOT SET"


class ProdConfig(GlobalConfig):
    ENVIRONMENT: str = "ENVIRONMENT NOT SET"
