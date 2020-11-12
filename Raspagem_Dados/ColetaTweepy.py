#COLETA DE TWEETS POR MEIO DA BIBLIOTECA TWEEPY
#Esse código foi aprendido principalmente por meio do canal Programação Dinâmica
#Mais informações acerca dos argumentos podem ser encontradas na documentação do Tweepy

import tweepy as tw
import pandas as pd

#Inserir informações pessoais
consumer_key = "xxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxx"
access_token = "xxxxxxxxxxxx"
access_token_secret = "xxxxxxxxxxxx"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth)
public_tweets = api.home_timeline()

#Define assunto a ser pesquisado nos tweets
query_search = 'ASSUNTO' + " -filter:retweets"

#Cria uma variável tweets a partir de um objeto Cursor
#http://docs.tweepy.org/en/v3.5.0/cursor_tutorial.html
tweets = tw.Cursor(api.search,
                  q=query_search).items(20)

#Verifica se está funcionando, imprimindo data e texto
for tweet in tweets:
    print(tweet.created_at)
    print(tweet.text)

#Definir todas as infos a serem extraídas dos tweets
twkeys = tweet._json.keys()
#dict_keys(['created_at', 'id', 'id_str', 'text', 'truncated', 'entities', 'metadata', 'source', 'in_reply_to_status_id', 'in_reply_to_status_id_str', 'in_reply_to_user_id', 'in_reply_to_user_id_str', 'in_reply_to_screen_name', 'user', 'geo', 'coordinates', 'place', 'contributors', 'is_quote_status', 'retweet_count', 'favorite_count', 'favorited', 'retweeted', 'lang'])

#Elaborar dicionário p/ organizar as infos extraídas
tweets_dict = {}
tweets_dict = tweets_dict.fromkeys(twkeys)

#Definir assunto a ser pesquisado e argumentos adicionais (filtrando retweets, definindo data e número de tweets)
query_search = 'ASSUNTO' + " -filter:retweets"
cursor_tweets = tw.Cursor(api.search,
                          until='2020-11-12',
            q=query_search).items(300)
#Utilizando o argumento since, pode-se obter os tweets mais recentes do dia atual, utilizando o argumento until, pode-se obter os últimos tweets do dia anterior à data informada

#Adicionando informações extraídas nas chaves correspondentes do dicionário
for tweet in cursor_tweets:
    for key in tweets_dict.keys():
        try:
            twkey = tweet._json[key]
            tweets_dict[key].append(twkey)
        except KeyError:
            twkey = ""
            tweets_dict[key].append("")
        except:
            tweets_dict[key] = [twkey]
        print("tweets_dict[key]: {} - tweet[key]: {}".format(tweets_dict[key], twkey))

#Adicionando itens do dicionário em um DataFrame
dfTweets = pd.DataFrame.from_dict(tweets_dict)
dfTweets.head()
dfTweets.text

#Salvando os tweets coletados em um arquivo csv
dfTweets.to_csv("TweetsColetados.csv", index=False)