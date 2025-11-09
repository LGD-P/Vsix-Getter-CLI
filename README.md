
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
    ms-python.debugpy@2025.14.1
    ms-python.python@2025.16.0
    ms-python.vscode-pylance@2025.9.1
    ms-python.vscode-python-envs@1.10.0
```

## 2\ From a url list : 

- You can download extensions from a list you've created and saved in `url_list_file.txt` : 

```txt
    https://marketplace.visualstudio.com/items?itemName=ms-python.pylint
    https://marketplace.visualstudio.com/items?itemName=fnando.linter
```

## 3\ From a single url :
- Finally, you can download a single extension directly from its marketplace URL 


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
    git clone https://github.com/LGD-P/Vsix-Getter.git
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