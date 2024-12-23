import requests
from sense_hat import SenseHat
import time

sense = SenseHat()

# ThingSpeak API Key
api_key = "YOUR_WRITE_API_KEY"  # YOUR_WRITE_API_KEY yerine kendi API anahtarınızı girin
url = "https://api.thingspeak.com/update"

while True:
    # Sıcaklık ve basınç verilerini al
    temperature = sense.get_temperature()  # Sıcaklık verisi
    pressure = sense.get_pressure()  # Basınç verisi

    # Verileri ThingSpeak'e gönder
    params = {
        "api_key": api_key,
        "field1": temperature,  # Sıcaklık verisi
        "field2": pressure  # Basınç verisi
    }

    response = requests.get(url, params=params)

    # Yanıtı kontrol et
    if response.status_code == 200:
        print("Veri gönderildi: Sıcaklık - {}, Basınç - {}".format(temperature, pressure))
    else:
        print("Veri gönderimi başarısız. Hata kodu:", response.status_code)

    time.sleep(15)  # 15 saniye bekle ve veriyi tekrar gönder