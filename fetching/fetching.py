import requests

response = requests.get("https://iamdcj.free.beeceptor.com")

print(response.status_code)
print(response.text)