MAX_CHAR = 280

texto = input()

lista_palavras = texto.split()
count_thread = 1
tail = 'Thread 🧵 1/4'
size_tail = len(tail)
tweet = ''
lista_tweet = []

while len(lista_palavras) > 0:

    palavra = lista_palavras.pop(0)
    tweet += ' ' + palavra
    size_tweet = len(tweet) + size_tail

    if size_tweet > MAX_CHAR:
        lista_palavras.insert(0, palavra)
        lista_tweet.append(tweet)
        tweet = ''
lista_tweet.append(tweet)

lista_tweet_tail = []
tamanho_thread = len(lista_tweet)

for pos, tweet in enumerate(lista_tweet, 1):
    tweet = tweet + ' ' + f'Thread 🧵 {pos}/{tamanho_thread}'
    lista_tweet_tail.append(tweet)

print('\n')
for tweet in lista_tweet_tail:
    print(tweet, end='\n\n\n')
