import requests
from tqdm import tqdm

def unshorten_url(url):
    try:
        response = requests.head(url, allow_redirects=True)
        return response.url
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Enter a list of shortened URLs (one per line):")
    urls = []
    while True:
        url = input().strip()  # Remove leading/trailing whitespace
        if not url:
            break
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url  # Add "https://" if missing
        urls.append(url)

    print("\nUnshortened URLs:")
    for url in tqdm(urls):
        unshortened_url = unshorten_url(url)
        print(f"{url} => {unshortened_url}")

if __name__ == "__main__":
    main()
