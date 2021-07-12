from flask import json


def test_home_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Welcome to Vehicle Rental API.' in response.data


def test_home_page_post(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is posted to (POST)
    THEN check that a '405' status code is returned
    """
    response = test_client.post('/')
    assert response.status_code == 405
    assert b'Welcome to Vehicle Rental API.' not in response.data


def test_empty_results(test_client, resources):
    """
    GIVEN a Flask API application
    WHEN the '/api' is requested (GET)
    THEN check that list of URLs of existing resources are returned"""
    response = test_client.get('/api/')
    assert response.status_code == 200

    sorted_keys_list = sorted(list(_get_json_from_resopnse(response).keys()))
    assert len(sorted_keys_list) == 5
    assert all([a == b for a, b in zip(resources, sorted_keys_list)])


def test_empty_results_for_public_resource(test_client):
    """
    GIVEN a Flask API application
    WHEn the '/api/search/vehicles is requested (GET)
    THEN check that the empty list is returned"""
    response = test_client.get('/api/search/vehicles')
    assert response.status_code == 200
    assert len(_get_json_from_resopnse(response)) == 0

# Helper function


def _get_json_from_resopnse(response):
    return json.loads(response.get_data(as_text=True))
