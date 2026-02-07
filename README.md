### Proje Özeti
Yerel RAG (Retrieval-Augmented Generation) mimarisini kullanan, gizlilik odaklı bir yapay zeka asistanıdır. Kullanıcının yüklediği PDF dokümanlarını analiz eder ve internete veri göndermeden, tamamen kendi bilgisayarımızda (Localhost) soruları cevaplar.

### Kurulum ve Çalıştırma Adımları

Projeyi yerel bilgisayarınızda (Localhost) çalıştırmak için aşağıdaki adımları sırasıyla uygulayın.

#### 1. Ön Gereksinimler

Projenin çalışması için bilgisayarınızda şu iki temel aracın yüklü olması gerekir:

* **Python (3.10 veya üzeri):** Kodun çalışması için gereklidir.
* **[Ollama](https://ollama.com/):** Yapay zeka modelini (LLM) yerel bilgisayarınızda çalıştırmak için gereken platformdur.

#### 2. LLM Modelinin Başlatılması (Ollama Ayarları)

Bu proje, Google'ın **Gemma** modelini ve metinleri vektöre çevirmek için **Nomic** modelini kullanır. Terminali (Komut İstemi) açın ve şu komutları girerek modelleri indirin:

# Sohbet edecek yapay zeka modelini indir
ollama pull gemma:4b

# Metinleri vektöre çevirecek embedding modelini indir
ollama pull nomic-embed-text


*(Not: Ollama uygulaması arka planda çalışıyor olmalıdır. Modeller bir kez indirildikten sonra internet bağlantısına gerek kalmaz.)*

#### 3. Proje Kütüphanelerinin Yüklenmesi

Proje klasörüne gidin ve gerekli Python paketlerini yükleyin:

pip install -r requirements.txt


#### 4. Vektör Veritabanının Oluşturulması (RAG Hazırlığı)

Sistemin dokümanı tanıması için önce onu okuyup veritabanına kaydetmesi gerekir.

1. Analiz edilecek PDF dosyasını `belge.pdf` adıyla proje klasörüne koyun.
2. Aşağıdaki kurulum betiğini çalıştırın:

python app/rag_kurulum.py


*(Bu işlem başarıyla tamamlandığında, klasörünüzde `chroma_db_v2` adında bir veritabanı dosyası oluşacaktır.)*

#### 5. Uygulamanın Başlatılması

Her şey hazır! API sunucusunu ayağa kaldırmak için şu komutu çalıştırın:

uvicorn app.main:app --reload

Artık tarayıcınızdan **`http://127.0.0.1:8000/docs`** adresine giderek asistanı test edebilirsiniz. 


### Kullanılan Teknolojiler ve Tercih Sebepleri:


#### Python: 
  Yapay zeka ve veri işleme alanındaki en zengin kütüphane desteğine sahip olduğu için ana dil olarak seçildi.

#### FastAPI: 
  Flask'a göre daha yüksek performans (Asenkron yapı) sunduğu ve otomatik dokümantasyon (Swagger UI) sağladığı için tercih edildi.

#### Ollama & Gemma:4b: 
  Hassas verileri dışarı çıkarmadan, yerel bilgisayarda düşük kaynak tüketimiyle yüksek performanslı cevaplar üretebilmek için kullanıldı.

#### ChromaDB: 
  Sunucu kurulumu gerektirmeyen, dosya tabanlı ve hafif bir vektör veritabanı olduğu için projeye dahil edildi.

#### LangChain: 
  LLM, veritabanı ve doküman işleme süreçlerini standart ve modüler bir yapıda birbirine bağlamak için seçildi.
