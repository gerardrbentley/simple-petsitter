# Simple Petsitter

Streamlit app deployed to Heroku

## What's this?


- `README.md`: This Document! To help you find your way around
- `streamlit_app.py`: The main app that gets run by streamlit
- `requirements.txt`: Pins the version of packages needed (handled by Heroku)
- `Procfile`: Special file to tell Heroku how to run our app (`streamlit run`)
- `LICENSE`: Follows streamlit's use of Apache 2.0 Open Source License
- `.gitignore`: Tells git to avoid comitting / scanning certain local-specific files

## Local Setup

Assumes working python installation and some command line knowledge ([install python my way](https://tech.gerardbentley.com/python/beginner/2022/01/29/install-python.html)).

```sh
git clone git@github.com:gerardrbentley/simple-petsitter.git
cd simple-petsitter
python -m venv ./venv
. ./venv/bin/activate
# ./venv/Scripts/activate for Windows
python -m pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Heroku 

launch: see Procfile.

Gets port from Heroku.
Doesn't create credentials or try to open browser

```sh
streamlit run streamlit_app.py --server.port $PORT --server.headless true
```

### Manual App Creation Step 1

- New App on [heroku](https://dashboard.heroku.com/apps)

![Heroku New App Button](images/2022-03-17-22-23-25.png)

- Give it a name that's available

![Heroku create app screen](images/2022-03-17-22-26-33.png)

- Select Github deployment for automated. Heroku CLI is also popular (see [this streamlit recommended guide](https://towardsdatascience.com/quickly-build-and-deploy-an-application-with-streamlit-988ca08c7e83))

![Heroku app dashboard pre deploy](images/2022-03-17-22-30-14.png)

- Find your Github repo if you've connected this way

![Heroku app dashboard with github](images/2022-03-17-22-32-37.png)

- Choose your branch for automatic deploys. (You can push code to other branches for safe keeping without overwriting the live site)

![Heroku Enable Auto Deployment](images/2022-03-17-22-35-53.png)