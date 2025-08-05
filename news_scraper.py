import requests
from bs4 import BeautifulSoup

# A simple and scrape-friendly site
URL = "https://www.npr.org/sections/news/"
OUTPUT_FILE = "headlines.txt"

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error fetching the page:", e)
        return ""

def extract_headlines(html):
    soup = BeautifulSoup(html, "html.parser")
    headlines = []

    # NPR uses <h2 class="title"> for headlines
    for tag in soup.find_all("h2", class_="title"):
        text = tag.get_text(strip=True)
        if text:
            headlines.append(text)

    return headlines

def save_to_file(headlines):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for headline in headlines:
            f.write(headline + "\n")
    print(f"{len(headlines)} headlines saved to {OUTPUT_FILE}")

def main():
    html = fetch_html(URL)
    if html:
        headlines = extract_headlines(html)
        if headlines:
            save_to_file(headlines)
        else:
            print("No headlines found.")
    else:
        print("Failed to load HTML.")

if __name__ == "__main__":
    main()
