from pathlib import Path

import typer

from {{cookiecutter.repo_name}} import metadata


def get_config_path():
    app_config_path = typer.get_app_dir(metadata.name)

    return str(Path(app_config_path) / "config.yaml")
