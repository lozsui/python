import cmd_util

import typer

app = typer.Typer(add_completion=False)


@app.command()
def version():
    """Return version of cmd util application"""
    print(f"...{__name__}")
    print(cmd_util.__version__)

