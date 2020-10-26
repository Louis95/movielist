import unittest
from app import app, replace_people, get_people_in_movies
from utilities import make_get_request


class MoviesListTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Welcome!!')

    def test_make_get_request(self):
        response = make_get_request("https://ghibliapi.herokuapp.com/films?limit=2")
        self.assertEqual(len(response), 2)

    def test_get_movies(self):
        response = self.client.get("/movies")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "application/json")

    def test_replace_people(self):
        list_dic1 = [
            {'id': '2baf70d1-42bb-4437-b551-e5fed5a87abe', 'title': 'Castle in the Sky', 'director': 'Hayao Miyazaki',
             'producer': 'Isao Takahata', 'people': ['https://ghibliapi.herokuapp.com/people/']}]

        list_dic2 = [{'people': 'Pazu', 'movies': ['Castle in the Sky']}, {'people': 'Kung', 'movies': ['Castle in the '
                                                                                                        'Sky']}]
        result = replace_people(list_dic1, list_dic2)
        self.assertEqual(result[0]["people"], ["Pazu", "Kung"])

    def test_people_movies(self):
        result = get_people_in_movies()
        self.assertEqual(len(result), 20)


if __name__ == '__main__':
    unittest.main()
