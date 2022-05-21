from __future__ import annotations

from typing import TYPE_CHECKING

from {{cookiecutter.repo_name}}.exceptions import AppException

if TYPE_CHECKING:
    pass


class AppActionDefaultProviderNotFound(AppException):
    def show(self):
        return "Default action provider not found!"
