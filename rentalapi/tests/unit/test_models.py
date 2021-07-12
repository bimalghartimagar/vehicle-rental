def test_new_user(new_test_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed password and role fields are defined correctly
    """
    assert new_test_user.email == 'test@test.com'
    assert new_test_user.username == 'test_username'
    assert new_test_user.password != 'test_password'
    assert new_test_user.type_id == 1
