# ML_Set-up
Machine Learning Setup

Software and Account Requirement
1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)

Creating conda virtual environment
```
conda create -p vij python==3.7 -y
```
Activating conda virtual environment
```
conda activate vij/
```
or
```
conda activate vij
```

Creating requirements.txt and app.py files

Installing libraries in requirements.txt
```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```
or
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status
```
git status
```

To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to git
```
git push origin main
```

To check remote url
```
git remote -v
```