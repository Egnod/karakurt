from __future__ import annotations

from typing import TYPE_CHECKING

from {{cookiecutter.repo_name}}.action_set.providers.base import BaseActionProvider

if TYPE_CHECKING:
    pass


class StubActionProvider(BaseActionProvider):
    """Stub class for sync providers classes."""

    name: str = "stub"
    hidden: bool = True

    def __init__(self, *args, **kwargs):
        pass

    def is_healthy(self):
        NotImplementedError()
