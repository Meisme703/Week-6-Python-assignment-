import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    # Get multiple URLs from user
    urls = input("Please enter the image URLs separated by commas: ").split(',')

    for url in urls:
        url = url.strip()  # Remove any leading/trailing whitespace

        try:
            # Fetch the image
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise exception for bad status codes

            # Extract filename from URL or generate one if not available
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            if not filename:
                filename = "downloaded_image.jpg"
            
            # Prevent downloading duplicate images
            filepath = os.path.join("Fetched_Images", filename)
            if os.path.exists(filepath):
                print(f"✗ Duplicate image found: {filename}. Skipping download.")
                continue

            # Save the image in binary mode
            with open(filepath, 'wb') as f:
                f.write(response.content)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}\n")

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error for URL '{url}': {e}")
        except Exception as e:
            print(f"✗ An error occurred for URL '{url}': {e}")

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()