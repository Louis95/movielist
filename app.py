from flask import Flask, jsonify
from utilities import make_get_request
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    """
     Prints out a welcome note.

             Parameters:
             Returns:
                     'welcome!!
     """
    return 'Welcome!!'


def replace_people(movies_list, people_list):
    """
     Replaces the people value with a list of all the people who acted in that movies.

             Parameters:
                     movies_list (list): A list of dictionaries
                     people_list (list): Another list of dictionaries

             Returns:
                     movies_list  (list): a new movies_list with the value of the people replace in a the dictionaries
     """
    try:

        for movies_dict in movies_list:
            movies_dict['people'] = []
            for people_dict in people_list:
                # I was quite confuse as to what to do with /films that are not in /people
                if movies_dict['title'] in people_dict['movies']:
                    movies_dict['people'].append(people_dict['people'])

            # if len(dict1['people']) == 0:
            #     dict1['people'] = make_get_request(backup[0])[]

        return movies_list
    except ImportError:
        return None



@app.route("/movies")
def get_movies():
    """
     Get the list of movies.

             Parameters:

             Returns:
                    movies_people  (list): a list of dictionaries
     """
    data = make_get_request("https://ghibliapi.herokuapp.com/films?limit=20")
    pe = get_people_in_movies()
    movies_people = replace_people(data, pe)

    return jsonify(movies_people)


def get_people_in_movies():
    """
     Get the list of people who acted in a film.

             Parameters:



             Returns:
                    people_and_movies_list  (list): a list of dictionaries
     """
    people_movies = make_get_request("https://ghibliapi.herokuapp.com/people?limit=20")
    people_and_movies_list = []
    for people in people_movies:
        people_movies_dict = {'people': people['name'],
                              'movies': [make_get_request(i)['title'] for i in people['films']]}

        people_and_movies_list.append(people_movies_dict)

    return people_and_movies_list


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    app.run()
