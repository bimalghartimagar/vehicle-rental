def test_resources_without_login(test_client, resources):
    """
    GIVEN a Flask API application
    WHEN the '/api/{resources}/ is requested (GET)
    THEN check if all the resources return unauthorized (401) status"""
    for resource in resources:
        response = test_client.get(f'/api/{resource}/')
        assert response.status_code == 401
