from app import app


def test_index_returns_demo_message():
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert response.get_json()["message"] == "Hello from the Jenkins demo application"
