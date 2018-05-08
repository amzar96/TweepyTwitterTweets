import tweepy
import json
import csv

csvFile = open('tweetliststreaming.csv', 'a')
csvWriter = csv.writer(csvFile)

consumer_key= 'YDQTpRIw3Eu3QWZjm7i1I2TjA'
consumer_secret= 'ifUyV84GKZHbnVBsWWqBdKUs7NAOwHF81tBjpntu27gI358VOL'
access_token='75163309-r39wFPr8ozJohjbgxrcaCMEtk7jqXZB9nSm9mGSKN'
access_token_secret='iUHaw9HQSOwhrZ9YBevADvh4V2ZlcNfT3KzzCATA6QeUZ'

#consumer_key= 'CHky1yfiABs1YaIGdZfK98Zhg'
#consumer_secret= 'tVBpes9lDtvC1F56ov4a4y3msUmeyMYVtVAMZ962UPi93j3uaK'
#access_token='966703597625815040-aiC8veIjwoIBxTXG5kPaQHCoED2ZtnF'
#access_token_secret='CqJDVqD109b14JTe3gpznBzftWNrhpioZmRLlZUbCbPKY'

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

