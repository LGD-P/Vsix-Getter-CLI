from pathlib import Path
import requests
from bs4 import BeautifulSoup
import requests
import json

URL_LIST = []
OUTPUT_DIR = Path("VSIX-DL")
API = "https://ms-vscode.gallery.vsassets.io/_apis/public/gallery/publisher/" \
    "{PUBLISHER}/extension/{EXT_NAME}/{VERSION}/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage"



class GetVsx:
    @staticmethod
    def prepare_url_list(txt_file: str ='ext_list.txt', api_url: str = API, url_list: list = URL_LIST ): 
        """format data from vscode list before download function"""
        with open(txt_file,'r') as f:
            lignes = f.readlines()
            for ligne in lignes:
                publisher = ligne[:ligne.find('.')]
                ext_name = ligne[ligne.find('.') +1 : ligne.find('@')]
                version = ligne[ligne.find('@') +1 :].strip()
                url ={ext_name : api_url.format(
                    PUBLISHER=publisher,
                    EXT_NAME=ext_name,
                    VERSION=version
                    )}
                url_list.append(url)
        return url_list
    
    @staticmethod
    def download_from_list_and_rename(url_list: list = URL_LIST, ext: str="vsix"):
        """Download from a url list and rename file from ext name"""
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        for e in url_list:
            for k, v in e.items():
                try:
                    response = requests.get(v, stream=True)
                    response.raise_for_status()
                    filename = f"{k}.{ext}"
                    filepath = OUTPUT_DIR / filename
                    with open(filepath, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    print(f"Download complete : {filepath}")
                except requests.exceptions.RequestException as e:
                    print(f"Error {v} : {e}")

    @staticmethod
    def download_from_url_and_rename(url: str, ext: str="vsix"):
        """Download from a single url and rename file from ext name"""
        data = GetVsx.build_vsix_dict(url)
        for k,v in data.items():
            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            try:
                response = requests.get(v, stream=True)
                response.raise_for_status()
                filename = f"{k}.{ext}"
                filepath = OUTPUT_DIR / filename
                with open(filepath, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"Download complete : {filepath}")
            except requests.exceptions.RequestException as e:
                print(f"Error : {e}")


    
    @staticmethod
    def build_vsix_dict(url:str, api_url:str=API):
        """Scrap the store with the url to return dict with ext name and api link"""
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        script = soup.find('script', class_='jiContent')
        data = json.loads(script.string)
        publisher = data['Resources']['PublisherName']
        ext_name = data['Resources']['ExtensionName']
        version = data['Resources']['Version']
        result = { ext_name : API.format(
            PUBLISHER=publisher,
            EXT_NAME=ext_name,
            VERSION=version
            )}
        return result
    
    @staticmethod
    def read_and_extract(url_list_file : str = "url_list_file.txt"):
        """Open the list and use build_vsix_dict()"""
        download_list = []
        with open(url_list_file, 'r') as f:
            lignes = f.readlines()
            for ligne in lignes:
                data = GetVsx.build_vsix_dict(ligne.strip())
                download_list.append(data)
        return download_list
    

