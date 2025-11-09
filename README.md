
<p align=center>
    <img src='assets/logo.ico' width="250px">
</p>

- This is a simple CLI tool to get your VsCode VSIX files extension : 

## 1\ From your current VsCode :

- You can export a list of your currently installed extensions from VSCode : 

```bash
    code --list-extensions --show-versions | tail -n+2  > ext_list.txt
```
- output exemple : 

```bash
    batisteo.vscode-django@1.15.0
    bracketpaircolordlw.bracket-pair-color-dlw@0.0.6
    cweijan.vscode-mysql-client2@8.4.2
    cweijan.vscode-postgresql-client2@8.4.2
    esbenp.prettier-vscode@11.0.0
    inferrinizzard.prettier-sql-vscode@1.6.0
    mhutchie.git-graph@1.30.0
```
- output exemple from CLI : 

<p align=center>
    <img src="assets/dl_from_vscode_list.png" width="650px">
</p>


## 2\ From a url list : 

- You can download extensions from a list you've created and saved in `url_list_file.txt` : 

```txt
    https://marketplace.visualstudio.com/items?itemName=ms-python.pylint
    https://marketplace.visualstudio.com/items?itemName=fnando.linter
```

```bash
    python3 main.py from-url-list
```

## 3\ From a single url :
- Finally, you can download a single extension directly from its marketplace URL 

```bash
    python3 main.py from-single-url https://marketplace.visualstudio.com/items?itemName=fnando.linter
```

*Every download is stored in your current dir under `VSIX-DL/` dir*

____________

- After downloading, you can then install your favorite extensions :

<p align=center>
    <img src="assets/install_vsix.png" width="450px">
</p>


____________

- You can view the help menu : 

<p align=center>
    <img src="assets/help_menu.png" width="850px">
</p>

*Check the .txt files in the repo to find example formats.*

____________


## Install : 

- clone the repo :

```bash
    git clone https://github.com/LGD-P/Vsix-Getter-CLI.git
    cd VSIX-GETTER
```

- Create and activate the env

```bash
    python3 -m venv env 
    source env/bin/activate
```

- Install Dependencies : 

```bash
    pip install -r requirements.txt
```

You're ready to go ! 
