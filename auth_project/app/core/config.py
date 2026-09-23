from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str  # JWT sign करण्यासाठी secret.
    ALGORITHM: str # JWT signing algorithm.
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # Token किती वेळ valid असेल.

    class Config:
        env_file = '.env'


settings = Settings()
