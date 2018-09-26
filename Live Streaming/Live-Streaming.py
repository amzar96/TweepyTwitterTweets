import tweepy
import json
import csv

csvFile = open('tweetliststreaming.csv', 'a')
csvWriter = csv.writer(csvFile)

consumer_key= ''
consumer_secret= ''
access_token=''
access_token_secret=''

class StreamListener(tweepy.StreamListener):
    def on_data(self, status):
        tweet = json.loads(status)

        print('@%s: %s' % (tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore')))
        csvWriter.writerow([tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore')])

    def on_error(self, status):
        	print("Error! -> {}".format(status))
        	return False




if __name__ == '__main__':
    listener = StreamListener()
    text = "python"
    # Show system message
    print('Collect tweet with : '+text+'! ==>')

    # Authenticate
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Connect the stream to our listener
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=[text],async=True)

