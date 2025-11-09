import rich_click as click
from logic_controller import GetVsx

@click.command()
def from_vscode_list():
    """To get the vscode list in your current dir use: code --list-extensions --show-versions | tail -n+2  > ext_list.txt"""
    list_from_vs_code = GetVsx.prepare_url_list()
    GetVsx.download_from_list_and_rename(list_from_vs_code)


@click.command()
def from_url_list():
    """You should have your url list in your current dir as : url_list_file.txt"""
    url_list = GetVsx.read_and_extract()
    GetVsx.download_from_list_and_rename(url_list)


@click.command()
@click.argument("url")
def from_single_url(url):
    """Just give the extension url from https://marketplace.visualstudio.com ."""
    GetVsx.download_from_url_and_rename(url)
    