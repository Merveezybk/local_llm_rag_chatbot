🛠️ Teknoloji Yığını (Tech Stack)
Projede kullanılan teknolojiler, performans, yerel çalışma yeteneği ve geliştirici deneyimi kriterlerine göre özenle seçilmiştir.

⚙️ Kurulum ve Çalıştırma
Projeyi kendi bilgisayarınızda (Windows/Mac/Linux) çalıştırmak için aşağıdaki adımları izleyin.

1. Ön Gereksinimler
Python 3.10 veya üzeri yüklü olmalıdır.

uygulaması bilgisayarınıza kurulmuş olmalıdır.

2. Depoyu Klonlayın
3. Sanal Ortam Kurulumu (Önerilen)
4. Kütüphanelerin Yüklenmesi
5. LLM Modellerinin Hazırlanması
Ollama üzerinden gerekli modelleri indirin (Bu işlem bir kez yapılır):

6. Veritabanının Oluşturulması (RAG Ingestion)
Analiz edilecek PDF dosyasını (örneğin belge.pdf) ana dizine kopyalayın ve veritabanını oluşturun:

Başarılı olduğunda chroma_db_v2 klasörü oluşturulacaktır.

7. Servisi Başlatın
Artık sunucunuz http://127.0.0.1:8000 adresinde çalışıyor! 🚀

🔌 API Kullanımı
Test etmek için tarayıcınızdan adresine gidebilir veya aşağıdaki uç noktaları kullanabilirsiniz.

🟢 1. Health Check (Sistem Kontrolü)
Servisin ayakta olup olmadığını kontrol eder.

URL: GET /health


💬 2. Soru Sorma (Ask)
Doküman içeriğiyle ilgili soru sormak için kullanılır.

URL: POST /ask

Body (JSON):

🧪 Test Süreçleri
Projenin güvenilirliğini artırmak için Unit Test ve Entegrasyon Testleri yazılmıştır. Test edilen senaryolar:

Happy Path: Ana sayfa ve Health check erişimi.

Validation Errors: Boş veri gönderimi, eksik parametreler (422 Hatası).

Method Not Allowed: Yanlış HTTP metodu kullanımı (405 Hatası).

Testleri çalıştırmak için terminale şunu yazın:

📂 Proje Yapısı
Modüler ve geliştirilebilir bir yapı tercih edilmiştir:

👨‍💻 Geliştirici Notları & Karşılaşılan Zorluklar
PDF Şifreleme Sorunu: Bazı PDF dosyaları okunurken pypdf şifreleme hatası verdi. Bu sorun cryptography kütüphanesi projeye dahil edilerek çözüldü.

Prompt Mühendisliği: Modelin halüsinasyon görmesini (uydurmasını) engellemek için, System Prompt kısmına "Eğer bilgi metinde yoksa bilmiyorum de" kuralı eklendi.