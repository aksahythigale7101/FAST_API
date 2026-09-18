from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
  CURRENT_DIR: str = os.path.dirname(os.path.abspath(__file__))
  BASE_DIR: str = os.path.dirname(CURRENT_DIR)

  DB_PATH: str = os.path.join(BASE_DIR, "products.db")
  DATABASE_URL:str = f"sqlite+aiosqlite:///{DB_PATH}"
  #DATABASE_URL:str
  class config:
       env_file = ".env"





settings = Settings()

