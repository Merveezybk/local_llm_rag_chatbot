import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

# --- AYARLAR ---
DOSYA_ADI = "belge.pdf"           # Klasördeki PDF'in adı
EMBEDDING_MODEL = "nomic-embed-text" # Sayıya çeviren model
DB_KLASORU = "./chroma_db_v2"       # Veritabanının kaydedileceği yer

def veritabani_olustur():
    print(" İŞLEM BAŞLIYOR...")

    # 1. PDF Kontrolü
    if not os.path.exists(DOSYA_ADI):
        print(f" HATA: '{DOSYA_ADI}' dosyası bulunamadı! Klasöre PDF koydun mu?")
        return

    # 2. PDF Yükleme
    print(f"📄 '{DOSYA_ADI}' okunuyor...")
    loader = PyPDFLoader(DOSYA_ADI)
    docs = loader.load()
    print(f"   -> Toplam {len(docs)} sayfa bulundu.")

    # 3. Parçalama (Chunking)
    print("  Metin parçalara ayrılıyor...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    print(f"   -> {len(splits)} küçük parçaya bölündü.")

    # 4. Veritabanına Kayıt
    print(" Veritabanı oluşturuluyor (biraz sürebilir)...")
    # Eğer eski veritabanı varsa hata vermemesi için temizleyelim (opsiyonel)
    if os.path.exists(DB_KLASORU):
        import shutil
        shutil.rmtree(DB_KLASORU)
        
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=OllamaEmbeddings(model=EMBEDDING_MODEL),
        persist_directory=DB_KLASORU
    )
    
    print(f" BAŞARILI! Veritabanı '{DB_KLASORU}' klasörüne kaydedildi.")

if __name__ == "__main__":
    veritabani_olustur()