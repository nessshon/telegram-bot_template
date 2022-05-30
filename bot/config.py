from dataclasses import dataclass

from environs import Env


@dataclass
class BotConfig:
    TOKEN: str
    CREATOR_ID: str
    STICKER_ID: str
    SERVICE_NAME: str
    SERVER_PASS: str


@dataclass
class DatabaseConfig:
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_HOST: str


@dataclass
class WebHookConfig:
    SITE: str
    PATH: str
    HOST: str
    PORT: str


@dataclass
class Config:
    bot: BotConfig
    db: DatabaseConfig
    webhook: WebHookConfig


env = Env()
env.read_env()

config = Config(
    bot=BotConfig(
        TOKEN=env.str("BOT_TOKEN"),
        CREATOR_ID=env.str("CREATOR_ID"),
        STICKER_ID=env.str("STICKER_ID"),
        SERVICE_NAME=env.str("SERVICE_NAME"),
        SERVER_PASS=env.str("SERVER_PASS"),
    ),
    db=DatabaseConfig(
        DB_USER=env.str("DB_USER"),
        DB_PASS=env.str("DB_PASS"),
        DB_NAME=env.str("DB_NAME"),
        DB_HOST=env.str("DB_HOST"),
    ),
    webhook=WebHookConfig(
        SITE=env.str("WEBHOOK_SITE"),
        PATH=env.str("WEBHOOK_PATH"),
        HOST=env.str("WEBHOOK_HOST"),
        PORT=env.str("WEBHOOK_PORT"),
    ),
)
