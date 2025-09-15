import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BOT_TOKEN = "8312513566:AAGeyU_Zb0yzErCa9_aPqBTUSKogMNpd4dQ"
CHAT_ID = "-4856635330"

def send_to_telegram(image_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    with open(image_path, "rb") as img:
        requests.post(url, data={"chat_id": CHAT_ID}, files={"photo": img})

def main():
    options = Options()
    # Headless'i yeni modda aç
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Normal tarayıcı gibi görünmesi için user-agent ekle
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/115.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)

    # Buraya istediğin kadar URL ekleyebilirsin
    urls = [
        "https://www.etstur.com/Voyage-Sorgun?check_in=30.08.2026&check_out=04.09.2026&adult_1=2&child_1=1&childage_1_1=9",
         "https://www.etstur.com/Gural-Premier-Belek?check_in=06.09.2026&check_out=11.09.2026&adult_1=2&child_1=0"   ]

    for i, url in enumerate(urls, start=1):
        driver.get(url)
        time.sleep(8)  # Pegasus için biraz daha uzun bekleme
        screenshot_path = f"screenshot_{i}.png"
        driver.save_screenshot(screenshot_path)
        send_to_telegram(screenshot_path)

    driver.quit()

if __name__ == "__main__":
    main()
