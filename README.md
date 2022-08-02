# Start blog
Initilisation project
```
git init 
```
Create two files: .gitignore, README.md
```
echo venv >> .gitignore
echo ## Start blog >> README.md
```
Setting up git
```
git add -A
git commit -a -m "Start blog"

git branch -M main
git remote add origin https://github.com/dimamatrusmat/blog.git

git push origin main
```
Create venv for project
```
pythom -m venv venv

venv\Script\activate
```
## Start django
Install django
```
pip install django
```
Start project
```
django-admin startproject myBlog
```
Moving to another folder
```
cd myBlog
```
Start server
```
python manage.py runserver
```

## Option for Blog
Work with migrations
```
python manage.py migrate
```
Create superuser
```
python manage.py createsuperuser
```

## Create app blog
```
django-admin startapp blog
```
