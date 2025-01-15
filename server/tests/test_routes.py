def test_send_preferences(client):
    response = client.post('/sendPreferences', json={"genres": ["fiction", "fantasy"]})
    assert response.status_code == 200
    assert response.json['message'] == "Préférences reçues"

def test_get_recommendations(client):
    response = client.get('/getRecommendations')
    assert response.status_code == 200
    assert len(response.json) > 0