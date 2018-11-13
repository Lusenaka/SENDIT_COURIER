import pytest



def client_app():
    app = create_app()
    test_client = app.test_client()
    return test_client
