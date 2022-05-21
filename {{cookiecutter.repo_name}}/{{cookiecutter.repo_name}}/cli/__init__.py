import logging
from pathlib import Path

import typer

from {{cookiecutter.repo_name}}.cli.command import Command
from {{cookiecutter.repo_name}}.cli.context import AppContextObject, Context
from {{cookiecutter.repo_name}}.cli.controllers import config
from {{cookiecutter.repo_name}}.cli.utils.echo_shortcuts import get_art_title
from {{cookiecutter.repo_name}}.config.configurator import get_configurator
from {{cookiecutter.repo_name}}.config.path import get_config_path
from {{cookiecutter.repo_name}}.exceptions import AppException
from {{cookiecutter.repo_name}}.logs import get_logger, set_logging_configuration

__all__ = ("app",)

app = typer.Typer(cls=Command)

app.add_typer(config.app, name="config")


def on_close(ctx: Context):
    def wrapper(*args, **kwargs):
        if ctx.obj and ctx.obj.spinner:
            ctx.obj.spinner.stop()
        ctx.close()

    return wrapper


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    config_path: Path = typer.Option(get_config_path(), "--config", "-C"),
    verbose: bool = typer.Option(False, "--verbose-logs", "-v", is_flag=True),
):
    ctx.call_on_close(on_close(ctx))

    typer.echo(get_art_title())

    set_logging_configuration(log_level=logging.INFO if verbose else logging.ERROR)

    if config_path.is_file():
        configurator = get_configurator(config_path=str(config_path))
    else:
        raise AppException(f"Config file [{config_path}] not found!")

    ctx.obj = AppContextObject(
        config_path=config_path,
        config=configurator,
        logger=get_logger(f"cli.{ctx.invoked_subcommand if ctx.invoked_subcommand else 'default'}"),
    )
