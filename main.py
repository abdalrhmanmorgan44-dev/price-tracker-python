import requests
from bs4 import BeautifulSoup

def get_gold_price():
    # الرابط الذي سنبحث فيه (جوجل كمثال سريع ومستقر)
    url = "https://www.google.com/search?q=gold+price+per+ounce"
    
    # إخبار الموقع أننا متصفح حقيقي لتجنب الحظر
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # استخراج السعر من نتائج بحث جوجل
        # ملاحظة: أماكن السعر قد تختلف قليلاً من وقت لآخر حسب تحديثات جوجل
        price = soup.find("span", {"jsname": "vWLAgc"}).text
        
        print(f"--- Gold Price Tracker ---")
        print(f"Current Gold Price: ${price} per ounce")
        print(f"--------------------------")
        
    except Exception as e:
        print("Error: Could not fetch price. Make sure you are connected to the internet.")

if __name__ == "__main__":
    get_gold_price()
