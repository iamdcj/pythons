import json
import requests

## Basic Fetch
def fetchBasic():
    return requests.get("https://iamdcj.free.beeceptor.com")

print(fetchBasic().status_code)
print(fetchBasic().text)

## Fetch some JSON
def fetchJson():
    return requests.get('https://jsonplaceholder.typicode.com/todos/1')

print(fetchJson().status_code)
jsonData = fetchJson().json()

print(jsonData["userId"])