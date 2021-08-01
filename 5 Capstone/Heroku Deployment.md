# Deploy a Django Project on Heroku

## Setup

1. Preparation
A few good organizational practices will make this entire process much smoother.  
    - Your Django project *must* be in its own git repo.
	- Your Django project *should* be at the root of that repo (The `manage.py` file and hidden `.git` folder should be in the same directory.)
	- Your Django project *should* be developed in a virtual environment with `pipenv` or `venv`.

2. Create a Heroku Account  
Go to [heroku.com](https://www.heroku.com) and create a free account.

3. Download the Heroku CLI  
Follow the instructions at [devcenter.heroku.com](https://devcenter.heroku.com/articles/heroku-cli) to download the Heroku CLI for your operating system.

## Create a new Heroku App
In a terminal, `cd` into the root of your project's git repo.  
Run this command:
```bash
heroku login
```
The `heroku login` command will:
1. Verify that the Heroku CLI is installed
2. Log into your Heroku account from the terminal  

This should open Heroku in your browser.  Follow the prompts to log in.

#### [Create an app from the command line](https://devcenter.heroku.com/articles/git#for-a-new-heroku-app)
To create your app, run this command, replacing `[your-app-name]` with your app's name:
```shell
$ heroku create [your-app-name]
```

### Note:
There is a chance that the name you want is taken.  Try variations of your preferred name until you get one that isn't taken.  
Once deployed, your app will be hosted at `https://your-app-name.herokuapp.com/` but you can set up a custom domain (i.e.: `your-app-name.com`, `your-app-name.net`) if you buy the domain from a DNS (Domain Name System) service like [Namecheap](https://www.namecheap.com) or [Google Domains](https://domains.google.com).

## Heroku & Git
Heroku 