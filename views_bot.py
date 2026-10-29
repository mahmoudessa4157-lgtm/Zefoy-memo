import os
from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import threading

app = Flask(__name__)

def send_view(tiktok_url, count):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    options.binary_location = "/usr/bin/chromium"

    for i in range(count):
        try:
            service = Service("/usr/bin/chromedriver")
            driver = webdriver.Chrome(service=service, options=options)
            driver.get(tiktok_url)
            time.sleep(5) # ثواني عشان التيك توك يحسبها مشاهدة
            driver.quit()
            print(f"View {i+1} sent successfully!")
        except Exception as e:
            print(f"Error on view {i+1}: {e}")

@app.route('/send-views', methods=['POST', 'OPTIONS'])
def handle_views():
    if request.method == 'OPTIONS':
        return '', 204
    data = request.json
    url = data.get('url')
    count = int(data.get('count', 10))

    if not url:
        return jsonify({"success": False, "error": "Missing URL"}), 400

    thread = threading.Thread(target=send_view, args=(url, count))
    thread.start()

    return jsonify({"success": True, "message": f"Started sending {count} views"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)