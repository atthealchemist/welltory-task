from pydantic import Field

from common.config import Settings


class FastAPISettings(Settings):
    title: str = "Welltory Task API"
    openapi_url: str = "/api/openapi.json"
    api_prefix: str = "/api"
    api_root: str = "/api/v1"
    docs_url: str = "/api/v1/docs"

    @property
    def tasks_root(self):
        return f"{self.api_root}/tasks"


class ProjectSettings(FastAPISettings):
    version: str = "0.1.0"
    debug: bool = Field(..., env="DEBUG")
    secret_key: str = Field(..., env="SECRET_KEY")
    project_name: str = Field(..., env="PROJECT_NAME")


class UvicornSettings(Settings):
    host: str = "127.0.0.1"
    port: int = 8080
    reload: bool = True
    debug: bool = True


uvicorn_settings = UvicornSettings()
app_settings = ProjectSettings()
api_settings = FastAPISettings()
