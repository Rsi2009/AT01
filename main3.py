import requests

def get_random_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data[0]["url"] if data else None
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return None
