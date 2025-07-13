import redis

# client = redis.Redis(host='localhost', port=6379, db=0)
client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

client.set('foo', 'barśćż')

# dodanie przy połaczeniu decode_responses=True
# powoduje, ze dostajemy nie bajty a znaki tekstowe zdekodowane
value = client.get('foo')
print(value)  # b'bar\xc5\x9b\xc4\x87\xc5\xbc'
# print(value.decode('utf-8')) # barśćż
print("------")
print(value)
# ------
# barśćż
