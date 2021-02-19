## Installation

Install Python
Install pip: pythttps://phoenixnap.com/kb/install-pip-windows
> pip install virtualenv
> python -m virtualenv venv

Before running any scripts:
> .\venv\Scripts\activate.bat
> pip install -r requirements.txt

And after installing new libraries
> pip freeze > requirements.txt


> pip install --upgrade 'markdown < 3'
> pip install urubu


## Deploying to gh-pages:

https://gist.github.com/cobyism/4730490

### tl;dr:

> git subtree push --prefix _build origin gh-pages


## Build

> python -m urubu build 
> python -m urubu serve
