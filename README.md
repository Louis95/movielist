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
                    "python app.py" to run after installing dependencies
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
Run `docker build -t movielist .`

then 
Run `docker run -it -p 5000:5000 movielist`

you will be able to access the application at `http://0.0.0.0:5000/`

### Endpoints



### Deployment

This guide assumes that you already had gone through the process of installing and authenticating the Heroku Toolbelt.

I'm assuming that you already have heroku installed. If you haven't installed heroku, please check the [installation guide](https://devcenter.heroku.com/articles/heroku-cli)

#### Gunicorn

Gunicorn is a pure-Python HTTP server for WSGI applications. We'll be deploying our applications using the Gunicorn webserver.

First, we need to install gunicorn using  `pip3 install gunicorn`. Next `touch Procfile` to create the file.

Procfile is exceedingly simple. It only needs to include one line to instruct Heroku correctly for us: `web: gunicorn --bind 0.0.0.0:$PORT app:app`

#### Create Your Heroku App

To create the Heroku app run `heroku create flaskmovieslist`. The output will include a git _url_ for your Heroku application. Copy this as we'll use it in a moment.

```
heroku create flaskmovieslist
Creating app... done, ⬢ flaskmovieslist
```
Now if you check your Heroku Dashboard in the browser, you'll see an application by that name. But it doesn't have our code or anything yet - it's empty. Let's get our code up there.

#### Add git remote for Heroku to the local repository

Using the git URL obtained from the last step, in the terminal run: `git remote add heroku heroku_git_url`

#### Push it!
Push it up! `git push heroku master`

#### Hosted Url
`https://flaskmovieslist.herokuapp.com/movies `

#### Git Link
`https://github.com/Louis95/movielist`


### Assumptions made

- My tests were mostly to test if my application works as expected. I did not test to ensure that the application can gracefully handle invalid input or unexpected user behavior.
- the limit query parameter is not working as specified in the documentation example `https://ghibliapi.herokuapp.com/people?limit=250` does not return 250 records  
