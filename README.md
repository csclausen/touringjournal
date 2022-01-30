# touringjournal backend
Minimal Flask quickstart with User login/registration views and Tailwind CSS

Installation

$ pip install -r requirements.txt

$ npm install


Run the project locally

$ npx tailwindcss -i ./flaskapp/static/input.css -o ./flaskapp/static/output.css --watch

$ export FLASK_APP=flaskapp

$ export FLASK_ENV=development

# If first time setup or you want to drop database and start fresh
$ flask init-db

$ flask run
