## Start blog

git init 

echo venv >> .gitignore
echo ## Start blog >> README.md

git add -A
git commit -a -m "Start blog"

git branch -M main
git remote add origin https://github.com/dimamatrusmat/blog.git

git push origin main

pythom -m venv venv

venv\Script\activate

# Start django
pip install django

django-admin startproject myBlog

cd myBlog

python manage.py runserver