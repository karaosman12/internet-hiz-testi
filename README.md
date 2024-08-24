# internet hiz testi 
# Internet Speed Test Python Script

Bu Python betiği, internet hızınızı test etmek için `speedtest-cli` kütüphanesini kullanır. Test, indirme ve yükleme hızınızı (Mbps cinsinden) ve ping sürenizi (ms cinsinden) ölçer. Ayrıca, test süresini de hesaplar.

## Özellikler

- **İndirme Hızı**: İnternet bağlantınızın veriyi indirme hızını ölçer.
- **Yükleme Hızı**: İnternet bağlantınızın veriyi yükleme hızını ölçer.
- **Ping Süresi**: İnternet bağlantınızın bir sunucuya yanıt verme süresini ölçer.
- **Test Süresi**: Testin ne kadar sürdüğünü ölçer.

## Gereksinimler

- Python 3.x
- `speedtest-cli` kütüphanesi

## Kurulum

1. **Python ve pip'in Yüklü Olduğundan Emin Olun**:
   - Python ve pip (Python paket yöneticisi) bilgisayarınızda yüklü olmalıdır. Yükleme için [Python'un resmi sitesini](https://www.python.org/downloads/) ziyaret edebilirsiniz.

2. **Gerekli Kütüphaneyi Yükleyin**:
   - Terminal veya komut istemcisini açın ve aşağıdaki komutu çalıştırarak `speedtest-cli` kütüphanesini yükleyin:
     ```bash
     pip install speedtest-cli
     ```

## Kullanım

1. **Kodu İndirin veya Kopyalayın**:
   - `speedtest.py` adlı bir dosya oluşturun ve aşağıdaki kodu bu dosyaya yapıştırın:

    ```python
    import speedtest
    import time

    def test_internet_speed():
        try:
            st = speedtest.Speedtest()
            print("Speedtest başlatılıyor...")
            print("Sunucular belirleniyor...")
            st.get_best_server()
            print("En iyi sunucu belirlendi.")
            print("Hız testi başlatılıyor. Lütfen bekleyin...")
            start_time = time.time()
            print("İndirme hızını ölçüyor...")
            download_speed = st.download() / 1_000_000  # Mbps cinsinden
            print(f"İndirme Hızı: {download_speed:.2f} Mbps")
            print("Yükleme hızını ölçüyor...")
            upload_speed = st.upload() / 1_000_000  # Mbps cinsinden
            print(f"Yükleme Hızı: {upload_speed:.2f} Mbps")
            ping = st.results.ping
            print(f"Ping Süresi: {ping} ms")
            end_time = time.time()
            duration = end_time - start_time
            print(f"Test süresi: {duration:.2f} saniye")
        except Exception as e:
            print(f"Bir hata oluştu: {e}")

    if __name__ == "__main__":
        test_internet_speed()
    ```

2. **Betikleri Çalıştırın**:
   - Terminal veya komut istemcisini açın ve betiği çalıştırmak için aşağıdaki komutu kullanın:
     ```bash
     python speedtest.py
     ```

3. **Sonuçları Görüntüleyin**:
   - Test tamamlandığında, indirme ve yükleme hızları, ping süresi ve test süresi ekrana yazdırılır.

## Katkıda Bulunma

Bu projeye katkıda bulunmak istiyorsanız, lütfen bir çekme isteği (pull request) gönderin veya bir sorun rapor edin. Her türlü katkı ve geri bildirim kabul edilir.

