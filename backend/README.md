# Flask Backend

## Getting started

Minimal read: [Flask quickstart](https://flask.palletsprojects.com/en/3.0.x/quickstart/)

### How to run it:

- make sure you're in `backend/`
- `python3 -m venv venv` (this only needs to be run the first time you run the app)
- `pip3 install -r requirements.txt` (this only needs to be run the first time you run the app)
- `. venv/bin/activate`
- `flask --app armma create-db` (this only needs to be run the first time you run the app or if you make any changes to the db schema)
- `flask --app armma run --debug`

So only steps 1, 4 and 6 are necessary from the second execution onward.

Note that Flask automatically reloads if it detects any code changes, so there's no need to restart it yourself.

If using VSCode, make sure to [select](https://code.visualstudio.com/docs/python/environments#_working-with-python-interpreters) the interpreter in the virtual environment.

### How to run tests

- run `pytest`
- run `coverage html` for test coverage info