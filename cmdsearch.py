import requests
from bs4 import BeautifulSoup
import re
import time
import random

# List of random user-agent strings
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15',
    # ... (add more user-agents as needed)
]

# Function to search Google and extract up to 100 unique .kh domain URLs
def search_kh_urls(domain):
    try:
        urls = set()
        start = 0
        while len(urls) < 100:
            user_agent = random.choice(user_agents)  # Select a random user-agent
            headers = {
                'User-Agent': user_agent
            }
            url = f"https://www.google.com/search?q=site:.{domain}+&start={start}"
            response = requests.get(url, headers=headers)
            
            # Check if the request was successful
            if response.status_code == 429:
                print("Rate limit exceeded. Sleeping for 60 seconds.")
                time.sleep(60)  # Sleep for 60 seconds before retrying
                continue
            
            response.raise_for_status()

            # Parse HTML response
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)

            for link in links:
                url = link['href']
                if url.startswith("http") and f".{domain}" in url:
                    # Normalize URL to avoid duplicates (remove query parameters and fragments)
                    normalized_url = re.sub(r'(\?|\&)([^=]+)\=([^&]+)', '', url)
                    urls.add(normalized_url)

                    if len(urls) >= 100:
                        break
            
            start += 10  # Move to the next page of results
            time.sleep(random.uniform(5, 10))  # Introduce a random delay between requests to avoid rate limits

        return list(urls)[:100]  # Convert set to list and return up to 100 unique URLs
    except requests.exceptions.RequestException as e:
        print(f"Error fetching search results: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    domain = input("Enter the domain (.kh): ").strip().lower()
    if domain.startswith('.'):
        domain = domain[1:]  # Remove leading dot if present

    found_urls = search_kh_urls(domain)
    
    if found_urls:
        print(f"Unique URLs found with .{domain} domain:")
        for idx, url in enumerate(found_urls, start=1):
            print(f"{idx}. {url}")
    else:
        print(f"No URLs with .{domain} domain found.")
