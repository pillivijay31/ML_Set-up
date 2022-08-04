# ML_Set-up
Machine Learning Setup

Software and Account Requirement
1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documenation](https://git-scm.com/docs/gittutorial)

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

### Deployment
To setup CI/CD pipeline in Heroku we need 3 information
1. HEROKU_EMAIL : vijay31civil@gmail.com
2. HEROKU_API_KEY : <>
3. HEROKU_APP_NAME : ml-project-31

>NOTE: for ubuntu system add 'sudo' before docker in the code

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase

To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 <image_name's IMAGE ID> 27f955987347
```
 
To check running container in docker
```
docker ps
```

To stop docker container
```
docker stop <container_id>
```

> We donot need to install from requirements.txt file, we can directly install from the below code

```
python setup.py install
```