from fastapi.testclient import TestClient

from app.main import app



client = TestClient(app)

def test_ana_sayfa():
    """Ana sayfaya erişim testi"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mesaj": "RAG API Çalışıyor! /docs adresine giderek test edebilirsin."}

def test_health_check():
    
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["durum"] == "aktif"

def test_bos_soru_hatasi():
    """Soru boş gönderilirse hata vermeli (Validation Test)"""
    # API şemasında zorunlu alan olduğu için 422 döner
    response = client.post("/ask", json={}) 
    assert response.status_code == 422