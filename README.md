# Django-React-todo-auth
this is just a simple web application just to work on user Login and permissions based on user Authentication.

<img width="314" alt="login" src="https://github.com/3westrick/Django-React-todo-auth/assets/109426803/8f11469d-232d-4705-9b22-340cdb698a93">
<br>
<hr>
<img width="368" alt="todo" src="https://github.com/3westrick/Django-React-todo-auth/assets/109426803/ded5febe-3df6-4768-9c89-1d0414bd2586">


## Installation | backend
first open the terminal and go to main folder that contains mysite and react-front.<br>
now we need a Virtual environment to install python packages.

```bash
python -m venv env
```
now to activate the environment (on mac)
```bash
source env/bin/activate
```
You should see "(env)" in your terminal, at the beginning of the line.<br>
Next use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements for backend.
```bash
pip install -r requirements.txt
```
And finally run the server
```bash
python mysite/manage.py runserver
```
it should run on 127.0.0.1:8000<br>
<strong>DO NOT CLOSE THE TERMINAL</strong>

## Installation | frontend
redirect your location to react-front and open another terminal.
you should already have [npm](https://nodejs.org/en/download) installed.
now use npm to install required packages
```bash
npm install
```

now run the server for React project by using this command:
```bash
npm start
```
it should run the server on 127.0.0.1:3000
