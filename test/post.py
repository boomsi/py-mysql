from app.utils.request import request
import pprint

HOST = 'http://localhost:5001/api'

login = request(
    f'{HOST}/user/login',
    method='POST',
    data=dict(username='test', password='test')
)

token = login.get('data')

insert = request(
    f'{HOST}/post/create',
    method='POST',
    data=dict(
        title='2333',
        content='309303'
    ),
    headers=dict(
        Authorization=token
    )
)

print(insert)
id = insert.get('data')

update = request(
    f'{HOST}/post/update/{id}',
    method='PUT',
    data=dict(
        title='1010',
        content='222'
    ),
    headers=dict(
        Authorization=token
    )
)

print(update)

list = request(
    f'{HOST}/post/list',
    method='GET',
    params=dict(page=1, size=10),
    headers=dict(
        Authorization=token
    )
)

pprint.pprint(list, indent=2, depth=2)

delete = request(
    f'{HOST}/post/delete/{id}',
    method='DELETE',
    headers=dict(
        Authorization=token
    )
)

pprint.pprint(delete, indent=2, depth=2)



