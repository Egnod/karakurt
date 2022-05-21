from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sitri import Sitri
from sitri.providers.contrib.yaml import YamlConfigProvider

from {{cookiecutter.repo_name}}.config.config_manager import ConfigManager

if TYPE_CHECKING:
    from {{cookiecutter.repo_name}}.action_set.providers.base import BaseActionProvider
    from {{cookiecutter.repo_name}}.action_set.providers.base.model import BaseActionModel


class Configurator(Sitri):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._sync_provider_class = None
        self.obj = None

    def set_config_obj(self, sync_provider_class: type[BaseActionProvider], config_obj: Any | None = None):
        self._sync_provider_class = sync_provider_class

        self.obj = (
            self.validate(self.config.provider._yaml, sync_provider_class=self._sync_provider_class)
            if not config_obj
            else config_obj
        )

    def get_validated(self, sync_provider_class: type[BaseActionProvider]):
        model = ConfigManager.get_config_model(provider_class=sync_provider_class)

        return model(**self.config.provider._yaml)

    @classmethod
    def validate(cls, config_data: dict, sync_provider_class: type[BaseActionProvider]) -> type[BaseActionModel]:
        model = ConfigManager.get_config_model(provider_class=sync_provider_class)

        return model(**config_data)


def get_configurator(config_path: str):
    config_provider = YamlConfigProvider(config_path, default_path_mode_state=True)
    config = Configurator(config_provider=config_provider)

    return config
