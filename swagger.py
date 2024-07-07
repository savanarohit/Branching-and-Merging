# Python script to fetch and parse Swagger JSON from
import requests

def fetch_endpoints(swagger_url):
    response = requests.get(swagger_url)
    if response.status_code == 200:
        swagger_json = response.json()
        endpoints = [path for path in swagger_json["paths"]]
        return endpoints
    else:
        raise Exception(
            f"Failed to fetch Swagger JSON: {response.status_code} - {response.text}"
        )

if __name__ == "__main__":
    swagger_url = "http://petstore.swagger.io/v2/swagger.json"
    try:
        endpoints = fetch_endpoints(swagger_url)
        for endpoint in endpoints:
            print(endpoint)
    except Exception as e:
        print(e)
