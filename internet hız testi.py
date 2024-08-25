import speedtest
import time

def test_speed():
    print("Hız testi başlatılıyor...")
    st = speedtest.Speedtest()
    st.get_best_server()
    
    print("Sunucu seçiliyor...")
    start_time = time.time()

    print("İndirme testi başlatılıyor...")
    download_speed = st.download() / 1_000_000  # Mbps
    print(f"İndirme hızı: {download_speed:.2f} Mbps")

    print("Yükleme testi başlatılıyor...")
    upload_speed = st.upload() / 1_000_000  # Mbps
    print(f"Yükleme hızı: {upload_speed:.2f} Mbps")

    print("Ping testi başlatılıyor...")
    ping = st.results.ping
    print(f"Gecikme: {ping} ms")

    end_time = time.time()
    total_duration = end_time - start_time
    print(f"\nTest süresi: {total_duration:.2f} saniye")

    print("\nSonuçlar:")
    print(f"İndirme Hızı: {download_speed:.2f} Mbps")
    print(f"Yükleme Hızı: {upload_speed:.2f} Mbps")
    print(f"Gecikme: {ping} ms")
    print(f"Toplam Süre: {total_duration:.2f} saniye")

if __name__ == "__main__":
    test_speed()

