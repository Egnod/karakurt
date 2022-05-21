from __future__ import annotations

import typing

from {{cookiecutter.repo_name}}.action_set.exceptions.default_provider import AppActionDefaultProviderNotFound
from {{cookiecutter.repo_name}}.action_set.providers import BaseActionProvider
from {{cookiecutter.repo_name}}.utils.enum import Enum

if typing.TYPE_CHECKING:
    from {{cookiecutter.repo_name}}.action_set.utils.metadata_manager import ActionMetadata


def get_provider_by_name(name: str) -> type[BaseActionProvider]:
    for cls in BaseActionProvider.__subclasses__():
        if name.upper() == cls.name.upper():
            return cls

    raise ValueError(f"Invalid provider name: {name}")


def get_default_provider() -> type[BaseActionProvider]:
    for cls in BaseActionProvider.__subclasses__():
        if cls.default:
            return cls

    raise AppActionDefaultProviderNotFound()


def get_providers_names() -> list[str]:
    result = []

    for cls in BaseActionProvider.__subclasses__():
        if not cls.hidden:
            result.append(cls.name)

    return result


def get_providers_names_enum() -> Enum:
    return Enum("ProvidersNames", dict(zip(get_providers_names(), get_providers_names())))  # type: ignore


def get_synchronizator(
    sync_config: dict[str, typing.Any], local_sync_metadata: ActionMetadata | None, forced: bool = False, **kwargs
):
    provider = get_provider_by_name(sync_config["provider"])

    return provider(
        options=sync_config["options"],
        targets=sync_config.get("targets", []),
        force=forced,
        local_sync_metadata=local_sync_metadata,
        **kwargs,
    )
