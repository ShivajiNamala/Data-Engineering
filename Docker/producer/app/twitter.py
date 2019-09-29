import json
import os
import time
import tweepy
import kafka
import configparser

kafka_topic = "topic1"
kafka_producer = None
#tracks = ['ISRO', 'kashmir', '#metoo']
#region = [ -79.691891, 43.433702, -79.449082, 43.998009]
region = [ -81.330702, 42.689977, -73.333302, 47.019803]
#language = ['en', 'es', 'fr']

class StdOutListener(tweepy.streaming.StreamListener):

    def on_data(self, data):
        	
        try:
            kafka_producer.send(kafka_topic, value=str(data).encode())
        except kafka.errors.KafkaError:
            print("Error sending data to Kafka")
        return True

    def on_error(self, status):
        print(status)
        kafka_producer.close()


if __name__ == '__main__':
    config = configparser.RawConfigParser()
    config.read('twitter.properties')
    consumer_key = config.get('TwitterApiCredentials', 'consumer_key')
    consumer_secret = config.get('TwitterApiCredentials', 'consumer_secret')
    access_token = config.get('TwitterApiCredentials', 'access_token')
    access_token_secret = config.get('TwitterApiCredentials', 'access_token_secret')   

    time.sleep(10)   # wait until Kafka is running
    kafka_service = os.environ['KAFKA_SERVICE']
    print("Producer is using kafka service {0}".format(kafka_service))

    kafka_producer = kafka.KafkaProducer(bootstrap_servers=[kafka_service],api_version=(0, 10))
    listener = StdOutListener()

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    stream = tweepy.Stream(auth, listener)
    stream.filter(locations=region)
    #stream.filter(locations=region,languages=languages,track=track)
