from app.utils.request import request

HOST = 'http://localhost:5001/api'

list = request(
    f'{HOST}/post/list',
    method='GET',
    params=dict(page=1, size=10)
)

print(list)