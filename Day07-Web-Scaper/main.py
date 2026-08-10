import requests
from bs4 import BeautifulSoup
import csv
import os

OUTPUT_FILE = "output/quotes.csv"
url = "https://quotes.toscrape.com/"

def scrape_quotes():
	try:
		response = requests.get(url, timeout=10)
		response.raise_for_status()
		
	except requests.RequestException as error:
		print(f"❌ Failed to access website: {error}")	
	
	soup = BeautifulSoup(response.text, "html.parser")
	
	quotes = soup.find_all("div", class_="quote")
	
	data = []
	
	for quote in quotes:
		text = quote.find("span", class_="text").text
		author = quote.find("small", class_="author").text
		
		tags = quote.find_all("a", class_="tag")
		tag_list = [tag.text for tag in tags]
		
		data.append({
			"quote" : text,
			"author" : author,
			"tags" : ",".join(tag_list)
		})
		
		
		
		print(f"Quote: {text}")
		print(f"Author: {author}")
		print()
		
		for tag in tags:
			print(tag.text, end =" ")
		print(f"""
		
		
		""")
		save_to_csv(data)
	
	
def save_to_csv(data):
	os.makedirs("output", exist_ok=True)	
	with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
		writer = csv.DictWriter(file, fieldnames=["quote", "author", "tags"])

		writer.writeheader()
		writer.writerows(data)
	print(f"Scraped {len(data)} quotes")
	print (f"Saved to {OUTPUT_FILE}")
	
	
def main():
	print("=" * 30)
	print("       QUOTE SCRAPER")
	print("=" * 30)

	scrape_quotes()


if __name__ == "__main__":
	main()