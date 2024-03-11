from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=("env/pg.env", "env/jwt.env"))


class PgConfig(BaseConfig):
    """This class is used to load environment variables for Postgres from pg.env"""

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_URL: str


class JwtConfig(BaseConfig):
    """This class is used to load environment variables for JWT from jwt.env"""

    SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_EXPIRATION_MINUETS: int


class Settings(PgConfig):
    """This class is used to load environment variables from .env files."""


settings: Settings = Settings()
