import requests
import json

def request(url, method, data=None, params=None, headers=None):
    if data:
        data = json.dumps(data)
    r = requests.request(
        method,
        url,
        data=data,
        params=params,
        headers={'Content-Type': 'application/json', ** (headers or {})}
    )
    if r.status_code < 300:
        return r.json()
    else:
        raise Exception(f'Request failed: {url}: {r.status_code}')
