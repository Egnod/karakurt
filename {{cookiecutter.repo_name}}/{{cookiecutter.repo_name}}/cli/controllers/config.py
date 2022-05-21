import typer

from {{cookiecutter.repo_name}}.cli.context import Context
from {{cookiecutter.repo_name}}.cli.utils.open_editor import open_editor

__all__ = ("app",)

app = typer.Typer()


@app.command("open")
def open_config(ctx: Context):
    open_editor(ctx.obj.config_path)


@app.command()
def path(ctx: Context):
    typer.echo(f"Path to config file: {ctx.obj.config_path}")
