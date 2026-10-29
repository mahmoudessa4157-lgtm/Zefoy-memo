from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# ⚠️ حط لينك فيديو التيك توك هنا
TIKTOK_URL = "https://vt.tiktok.com/ZSgtVVrVd/"

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

service = Service("/usr/bin/chromedriver")

# عدد المشاهدات اللي عايزها
for i in range(50):
    try:
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(TIKTOK_URL)
        time.sleep(10)  # استنى 10 ثواني عشان يتسجل مشاهدة
        driver.quit()
        print(f"✅ View {i+1} sent")
    except Exception as e:
        print(f"❌ Error on view {i+1}: {e}")
