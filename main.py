from pathlib import Path
import rich_click as click
from click_controller import from_vscode_list, from_url_list, from_single_url


click.rich_click.COMMAND_GROUPS = {
    "cli": [
        {
            "name": "VSIX Downloader",
            "commands": ["from-vscode-list", "from-url-list", "from-single-url"],
            "table_styles": {
                "show_lines": True,
                "row_styles": [ "cyan"],
                "border_style": "red",
                "box": "DOUBLE",
            },
        },
    ],
}


@click.group()
def cli():
    pass


cli.add_command(from_single_url)
cli.add_command(from_url_list)
cli.add_command(from_vscode_list)

if __name__ == "__main__":
    cli()
