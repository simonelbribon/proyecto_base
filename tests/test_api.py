def test_pipeline(client):
    response = client.post("/v1/pipeline", json={"text": "Fast API SEME"})

    assert response.status_code == 200

    data = response.json()
    assert data["seme"] == "fast api seme"
    assert data["final"] == "FAST API SEME"
