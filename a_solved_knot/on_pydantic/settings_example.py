from pydantic_settings import BaseSettings, SettingsConfigDict

"""
First attempt to get the grip of pydantic_settings. Unfortunately,
right now I do have big problems to understand how to use it! Of which
I do feel really said about.
"""


class Settings(BaseSettings):
    app_name: str = "Default Name"
    admin_email: str
    items_per_user: int = 1

    model_config = SettingsConfigDict(env_file=".env")


if __name__ == "__main__":
    settings = Settings()
    print(settings)
