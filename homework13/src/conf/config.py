from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    CLOUDINARY_NAME: str = 'hw-13'
    CLOUDINARY_API_KEY: int = 645381621127547
    CLOUDINARY_API_SECRET: str = 'secret'
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: int
    MAIL_USERNAME: str = "reese@meta.ua",
    MAIL_PASSWORD: str = "secretPassword",
    MAIL_FROM: str = "reese@meta.ua",
    MAIL_PORT: int = 567234,
    MAIL_SERVER: str = "smtp.meta.ua",

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()