import requests


def check_robots(url):
    robots_url = url.rstrip("/") + "/robots.txt"

    try:
        response = requests.get(robots_url)

        if response.status_code == 200:
            print("\nrobots.txt found:\n")
            print(response.text)
        else:
            print("\nrobots.txt not found (404). Continuing politely...\n")

        return True

    except Exception as e:
        print("Error:", e)
        return True