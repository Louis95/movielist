MovieList
----------

###
MoviesList is an application that displaces information about movies and people (characters)


### Main Files: Project Structure

  ```
  ├── 
  ├──  Dockerfile
  ├─- README.md
  ├── app.py *** the main driver of the app.
                    "python app.py" to run after installing dependences
  ├── requirements.txt *** The dependencies we need to install with "pip3 install -r requirements.txt"
 
  ```

### Development Setup

First, [install Flask](http://flask.pocoo.org/docs/1.0/installation/#install-flask) if you haven't already.

  ```
  $ cd ~
  $ sudo pip3 install Flask
  ```

To start and run the local development server,

1. Initialize and activate a virtualenv:
  ```
  $ cd YOUR_PROJECT_DIRECTORY_PATH/
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```

2. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

3. Run the development server:
  ```
  $ export FLASK_APP=myapp
  $ export FLASK_ENV=development # enables debug mode
  $ flask run
  ```
Run Test

run `python3 tests.py` 


Using Docker

I'm assuming that you already have docker installed and authenticated
- Build the docker image
Run `docker build -t flaskstarship .`

then 
Run `docker run -it -p 5000:5000 flaskstarship`

you will be able to access the application at `http://0.0.0.0:5000/`

### Endpoints



### Deployment

This guide assumes that you already had gone through the process of installing and authenticating the Heroku Toolbelt.

I'm assumming that you already have heroku installed. If you haven't installed heroku, please check the [installation guide](https://devcenter.heroku.com/articles/heroku-cli)

#### Gunicorn

Gunicorn is a pure-Python HTTP server for WSGI applications. We'll be deploying our applications using the Gunicorn webserver.

First, we need to install gunicorn using  `pip3 install gunicorn`. Next `touch Procfile` to create the file.

Procfile is exceedingly simple. It only needs to include one line to instruct Heroku correctly for us: `web: gunicorn --bind 0.0.0.0:$PORT app:app`

#### Create Your Heroku App

In order to create the Heroku app run `heroku create flaskstarship`. The output will include a git _url_ for your Heroku application. Copy this as, we'll use it in a moment.

```
heroku create flaskstarship
Creating app... done, ⬢ flaskstarship
```
Now if you check your Heroku Dashboard in the browser, you'll see an application by that name. But it doesn't have our code or anything yet - it's completely empty. Let's get our code up there.

#### Add git remote for Heroku to local repository

Using the git url obtained from the last step, in terminal run: `git remote add heroku heroku_git_url`

#### Push it!
Push it up! `git push heroku master`

#### Hosted Url
`https://flaskstarship.herokuapp.com/starships`

#### Git Link
`https://github.com/Louis95/FlaskStarship`


### Assumptions made

- The [link](https://swapi.co/api/starships/) to SWAPI given in the instructions was broken so I decided to use a different [SWAPI](https://swapi.dev/api/starships/)

- The user will alway to pass a live url. A check could also be implemented to check if the given url is not broken before making the request.