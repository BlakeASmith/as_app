import os
import click
@click.group()
def asapp():
    """Launch websites in app mode."""
    ...


@click.option(
    "--chrome", "-c",
    help="The chromium/google chrome binary to use.",
    default="chromium-browser",
)
@click.argument("url")
@asapp.command()
def open(chrome, url):
    """Open a url in app mode."""
    os.system(f"{chrome} --app={url}")

