import redis as r

class RedisInit():
    def __init__(self, host, port, db):
        self.redis = r.Redis(
            host=host,
            port=port,
            db=db
        )
    
    def set(self, key, value, **kwargs):
        self.redis.set(key, value, **kwargs)
    
    def get(self, key):
        return self.redis.get(key)

    def delete(self, key):
        self.redis.delete(key)

redis = RedisInit('localhost', 6379, 0)
