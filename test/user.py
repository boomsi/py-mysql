# from request import request
from app.utils.request import request

HOST = 'http://localhost:5001/api'

registry = request(
    f'{HOST}/user/registry', 
    method='POST', 
    data=dict(username='test', password='test'),
)
print(registry)

login = request(
    f'{HOST}/user/login',
    method='POST',
    data=dict(username='test', password='test')
)
print(login)
