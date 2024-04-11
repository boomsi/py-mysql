1. encoded = jwt.encode(user, JWT_SECRET, algorithm="HS256", json_encoder=Encoder)
    datetime 不能序列化，需要自定义json_encoder

```py
class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime) or isinstance(obj, date):
            return obj.timestamp()
        return json.JSONEncoder.default(self, obj)
```

