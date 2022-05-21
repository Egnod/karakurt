from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import typer
from structlog.types import WrappedLogger
from yaspin.core import Yaspin
from yaspin.spinners import Spinners

from {{cookiecutter.repo_name}}.config.configurator import Configurator
from {{cookiecutter.repo_name}}.logs import get_logger


@dataclass
class AppContextObject:
    config_path: Path = Path()
    logger: WrappedLogger = get_logger("default")

    config: Configurator = Configurator(config_provider=None)

    spinner: Yaspin = Yaspin(spinner=Spinners.aesthetic)


class Context(typer.Context):
    obj: AppContextObject
