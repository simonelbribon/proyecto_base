def test_pipeline(client):
    response = client.post("/pipeline", json={"text": "Fast API SEME"})
    assert response.status_code == 200

    data = response.json()
    assert "seme" in data
    assert "final" in data
