import tweepy
import hcjy_config as ct
client=tweepy.Client(bearer_token=ct.BEARER_TOKEN)

query='makeup -is:retweet'

response=client.search_recent_tweets(query=query,max_results=11)

for data in response.data:
    print(data.id)
    print(data)