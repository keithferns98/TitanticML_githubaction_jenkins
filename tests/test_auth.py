def test_login_success(client):
    response = client.post(
        "/auth/login",
        data = {
            "username": "keith",
            "password": "ferns123"
        }
    )
    assert response.status_code == 200

    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"