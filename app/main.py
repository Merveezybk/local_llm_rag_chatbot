from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma


MODEL_ADI = "gemma3:4b"        # Senin kullandığım model
EMBEDDING_MODEL = "nomic-embed-text"
DB_KLASORU = "./chroma_db_v2"  # oluşturduğum hafıza klasörü

# 1. Uygulamayı Başlatma
app = FastAPI(title="Benim RAG Servisim", version="1.0")

print(" Sistem hazırlanıyor.")

# 2. Yapay Zeka ve Hafızayı Yükleme
try:
    llm = ChatOllama(model=MODEL_ADI)
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    
    # Hafızayı diskten okuyoruz
    db = Chroma(
        persist_directory=DB_KLASORU, 
        embedding_function=embeddings
    )
    print(" Hafıza (Vector Store) başarıyla yüklendi.")
except Exception as e:
    print(f" HATA: Sistem yüklenirken sorun oluştu: {e}")

# --- API UÇ NOKTALARI (ENDPOINTS) ---

class SoruModeli(BaseModel):
    soru: str

@app.get("/")
def ana_sayfa():
    return {"mesaj": "RAG API Çalışıyor! /docs adresine giderek test edebilirsin."}

@app.get("/health")
def health_check():
    return {"durum": "aktif", "versiyon": "1.0"}

@app.post("/ask")
def soru_sor(istek: SoruModeli):
    """
    Kullanıcıdan soru alır, dokümanlarda arar ve cevap döner.
    """
    try:
        print(f"📩 Gelen Soru: {istek.soru}")
        
        # A. RETRIEVAL (Bilgi Getirme): Soruyu veritabanında arıyoruz
        ilgili_dokumanlar = db.similarity_search(istek.soru, k=3) # En alakalı 3 parça
        
        # B. CONTEXT (Bağlam): Bulunan parçaları birleştiriyoruz
        baglam = "\n\n".join([doc.page_content for doc in ilgili_dokumanlar])
        
        if not baglam:
            return {"cevap": "Üzgünüm, dokümanlarda bu konuyla ilgili bilgi bulamadım."}

        # C. GENERATION (Cevap Üretme): Bilgiyi LLM'e verip cevap istiyoruz
        prompt = f"""Aşağıdaki bilgileri kullanarak soruyu cevapla.
        Eğer bilgi metinde yoksa "Bilmiyorum" de.
        
        BİLGİLER:
        {baglam}
        
        SORU: {istek.soru}
        """
        
        cevap = llm.invoke(prompt)
        
        return {
            "cevap": cevap.content,
            "kaynaklar": [doc.page_content[:100] + "..." for doc in ilgili_dokumanlar] # Kaynakları gösterme
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))