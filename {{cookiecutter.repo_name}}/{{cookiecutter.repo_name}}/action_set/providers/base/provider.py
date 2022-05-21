from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING

from {{cookiecutter.repo_name}}.action_set.providers.base.model import BaseActionOptionsModel
from {{cookiecutter.repo_name}}.logs import get_logger

if TYPE_CHECKING:
    pass


class BaseActionProvider(metaclass=ABCMeta):
    """Base class for action providers classes."""

    name: str
    options_model: type[BaseActionOptionsModel]

    default: bool = False
    hidden: bool = False

    def __init__(self, options: dict[str, str], *args, **kwargs):
        self.options = self.options_model(**options)
        self._logger = get_logger(__name__)
        self._kwargs = kwargs
        self._args = args

    @abstractmethod
    def is_healthy(self) -> bool:
        pass
