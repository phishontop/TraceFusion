import json

import requests


PLATFORMS = {"steam", "discord"}


def lookup(name: str, value: str) -> dict:
    response = requests.get(f"http://167.99.206.172:5000/api/{name}/lookup?key=YvodwXmlkFEmctQ&id={value}")
    return response.json()


def main():
    while True:
        platform_name = input("Enter platform name (Steam/Discord): ").lower()
        if platform_name not in PLATFORMS:
            print("Invalid platform")
            continue

        user_id = input("Enter user ID (Steam/Discord ID): ")
        print(json.dumps(lookup(platform_name, user_id), indent=4))


if __name__ == "__main__":
    main()

