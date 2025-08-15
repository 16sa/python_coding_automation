import json
import requests
import logging

def hit_endpoint(url):
    list = []
    if url:
        try:
            data = requests.get(url)
            data.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
            dump = data.json()
            
            # The JSONPlaceholder API doesn't have a 'count' key at the top level,
            # so we use the length of the list to get the count.
            print(f"Total entries: {len(dump)}")
            
            # we'll just process the first 5 posts for demonstration.
            for post in dump[:5]:
                # we'll just print the post ID for this example
                print(f"Post ID: {post['id']}")
            
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching data: {e}")
    else:
        print("Error: URL is empty.")

# Use a working URL
hit_endpoint("https://jsonplaceholder.typicode.com/posts")