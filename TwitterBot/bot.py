from re import T
import time
import tweepy

consumer_key = "IdJM1LgDTo1jezG6eSn9D31rK"
consumer_secret = "yzGGzS1c1zTWHZUxKomIhCSy85KAZ17KOWTN73TGK3ASkcq0Lt"
key = "1458485541826072584-MnfkXPnhcKahQMKoualBIElKsYtkxk"
secret = "N5mYadf8gmed4xBVv1Lb2bFGH5qQXcFsBbUIAAdosNPXf"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
 
bot_id= int(api.verify_credentials().id_str)
mention_id = 1

words = ["I think you gay", "lets go ", "Fortnite is better than Valorant", "Fortnite", "You suck bitch"]
message = "I think younare gay @{}"
message = "why are you gay @{}"
message = "lets go"



while True:
    mentions = api.mentions_timeline(since_id=mention_id) 
    for mention in mentions:
        print("Mention tweet found")
        print(f"{mention.author.screen_name} - {mention.text}")
        mention_id = mention.id
        if mention.in_reply_to_status_id is None and mention.author.id != bot_id:
            if True in [word in mention.text.lower() for word in words]:
                try:
                    print("Attempting to reply...")
                    api.update_status(message.format(mention.author.screen_name), in_reply_to_status_id=mention.id_str)
                    print("Successfully roasted that bitch :)")
                except Exception as exc:
                    print(exc)
    time.sleep(15) 


while True:
    mentions = api.mentions_timeline(since_id=mentions_id)  
    for mention in mentions:
        print("found that bitch ")
        print (f "{mention.author.screen_name} said: {mention.text}")
        mentions_id = mention.id
        if mention.in_reply_to_status_id is None and mention.author.id != bot_id:
            if True in [word in mention.text.lower() for word in words]:
                try:
                    print("Attempting to reply...")
                    api.update_status(message.format(mention.author.screen_name), in_reply_to_status_id=mention.id_str)
                    print("Successfully roasted that bitch :)")
                except Exception as exc:
                    print(exc)
    time.sleep(15)
    
        





     
