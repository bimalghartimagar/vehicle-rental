from rentalapi.tests.functional.test_apis import _get_json_from_resopnse


def test_resources_after_login(auth):
    """
    GIVEN a Flask API application
    WHEN the '/api/auth/login/ is requested (GET)
    THEN check if status is 200 and token is returned
    on successful login"""

    response = auth.login('admin', 'admin123')
    assert response.status_code == 200
    response_keys = _get_json_from_resopnse(response).keys()
    assert 'access_token' in response_keys
    assert 'refresh_token' in response_keys


def test_fetching_resources_after_login(test_client_with_db, auth, resources):
    """
    GIVEN a Flask API application
    WHEN the '/api/{resource}/ is requested (GET)
    THEN check if each resource is accessible and has status 200"""

    response = auth.login('admin', 'admin123')
    assert response.status_code == 200
    response_json = _get_json_from_resopnse(response)
    assert 'access_token' in response_json.keys()
    assert 'refresh_token' in response_json.keys()

    for resource in resources:
        resource_response = test_client_with_db.get(
            f'/api/{resource}/',
            headers={
                'Authorization': f'Bearer {response_json["access_token"]}'
            })
        print(resource_response.data)
        assert resource_response.status_code == 200
