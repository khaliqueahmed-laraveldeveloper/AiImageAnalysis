import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('my_key', 'Hello Redis!', ex=10)  # Set a key with an expiration time of 10 seconds
value=r.get('my_key')
print(value.decode('utf-8'))