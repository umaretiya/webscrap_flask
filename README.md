# ML_classification_Project

Machine Learning Porject of Credit card defaults prediction
```
classification Machine Learning projects
```
Data sources

[kaggle openshource datasts](https://kaggle.com)

For merging a existing repo with directory

git init

## docker images build
```
docker build -t <image name>:<tag>
docker image build -t <flask_docker> .

docker run -p 5000:5000 -d <webscrap>
remot docker repo 9909868/flaskwebscrap
docker ps

docker stop <container id>
```
pushing image 
```
docker tag flask_docker <your-docker-hub-username>/flask-docker
docker push <your-docker-hub-username>/flask-docker
```
heroku app flask-fsweb name
command :
heroku login
heroku container:login
docker login --username=<your-username> --password=<your-password>
heroku create <app-name>

heroku container:push web --app <app-name>
heroku container:release web --app <app-name>



echo "# git_repo" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/umaretiya/flask_FSDS.git
git push -u origin main


### force fully push
git remote add origin-push https://github.com/umaretiya/flask_FSDS.git
git fetch origin-push

git push --force-with-lease origin-push