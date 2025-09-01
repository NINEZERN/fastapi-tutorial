from pydantic_settings import BaseSettings 

class Settings(BaseSettings):
    database_url: str 
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"
        env_prefix = ""

settings = Settings() # type: ignore
print (settings.database_url) # type: ignore