from TwitterAPI import TwitterAPI

"""
print('Hello world!')

lista = []

for index in range(10, 1, -1):
    lista.append(f"Lista decrescente, item {index}")

for item in lista:
    print(f"Item {item}\n")
"""

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

#r = api.request('statuses/update', {'status':'Teste de tweet do meu app'})
#print (r.status_code)