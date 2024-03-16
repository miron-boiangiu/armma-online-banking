import pytest
from flask import g
from flask import session

from armma.db.db import get_db


def test_register(client, app):
    # test that adding a user works
    response = client.post("/register", data={"username": "a", "password": "a"})

    # check that the user was inserted into the database
    with app.app_context():
        assert (
            get_db().execute("SELECT * FROM user WHERE username = 'a'").fetchone()
            is not None
        )


@pytest.mark.parametrize(
    ("username", "password", "message"),
    (
        ("", "", b"Username is required."),
        ("a", "", b"Password is required."),
        ("test", "test", b"already registered"),
    ),
)
def test_register_validate_input(client, username, password, message):
    response = client.post(
        "/register", data={"username": username, "password": password}
    )
    assert message in response.data


def test_login(client, auth):
    # Check response when not logged in
    assert b"error" in client.get("/logged_in_check").data

    # Check response when logged in
    auth.login()
    assert b"user" in auth.get("/logged_in_check").data


@pytest.mark.parametrize(
    ("username", "password", "message"),
    (("a", "test", b"Incorrect username."),
     ("test", "a", b"Incorrect password.")),
)
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data


def test_logout(app, auth):

    auth.login()
    assert b"success" in auth.get("/logged_in_check").data

    auth.logout()
    assert b"success" not in auth.get("/logged_in_check").data


