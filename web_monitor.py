import requests
from bs4 import BeautifulSoup
import time

def track_price(url, target_price):
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # ملاحظة للمدير: هنا نقوم بسحب السعر (مثال افتراضي)
        # في مشروع حقيقي، سنستخدم ID أو Class محدد للمنتج
        price_text = soup.find("span", {"class": "price"}).get_text()
        current_price = float(price_text.replace('$', '').replace(',', ''))
        
        if current_price <= target_price:
            print(f"🎯 Alert! Price dropped to {current_price}. Ready to buy!")
            return True
        else:
            print(f"⏳ Still waiting... Current price: {current_price}")
            return False
            
    except Exception as e:
        print(f"❌ Error accessing site: {e}")

# تجربة منطق المراقبة
if __name__ == "__main__":
    print("🚀 Monitoring Engine Started...")
    # track_price("https://example.com/product", 100)
