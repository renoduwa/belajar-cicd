from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    # Robot CI akan melakukan simulasi request HTTP GET ke "/"
    response = client.get("/")
    
    # Validasi 1: Apakah server merespons dengan HTTP 200 OK?
    assert response.status_code == 200
    
    # Validasi 2: Apakah struktur JSON yang dikembalikan sesuai kontrak?
    assert response.json() == {"status": "success", "message": "Sistem Web Aktif"}