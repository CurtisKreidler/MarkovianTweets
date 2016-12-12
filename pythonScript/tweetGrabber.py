import twitter
import re
import config
import sys
import os

# statuses = api.GetUserTimeline(screen_name='StephenAtHome')
twitterHandleName = sys.argv[1] #commandline TwitterHandleName

TWEETCOUNTER = 0
# please don't take my oauth token/ I realize that this is not the most secure but this project
# was meant to be made into executable that was called by our main2.cpp
api = twitter.Api(consumer_key= config.user_consumer_key,
                  consumer_secret= config.user_consumer_secret,
                  access_token_key=	config.access_token_key,
                  access_token_secret= config.access_token_secret)
#print(api.VerifyCredentials()) #for testing connection

def data_grab(twitter_handle):
    global TWEETCOUNTER
    intialTimelineInfo = api.GetUserTimeline(screen_name = twitter_handle, exclude_replies = True, include_rts = False)
    latestTweetIds = [s.id for s in intialTimelineInfo]
    firstId = latestTweetIds[0]
    itr = 0
    data = []
    for itr in range(0,30): #iteraterates for blocks of ~200 tweets at a time
        itr+=1
        statuses = api.GetUserTimeline(screen_name = twitter_handle, exclude_replies = True, include_rts = False, max_id = firstId)
        last = [s.id for s in statuses]
        #print(last[len(last)-1])#testing to get the id of the last tweet added to the list
        data.insert(itr,[s.text for s in statuses])#grabs the text in the puts it in a list and adds it to the larger list
        firstId = last[len(last)-1]
        TWEETCOUNTER += len(statuses) #number of tweets per block
    return data # returns a list of lists


def sanitize_unicode(data): #need to get rid of bad symbols
   # data = data.split("") # need to read through list and take out lists then in those lists remove escape characters
    clean_data = ""
    for lists in data:
        for sentences in lists:
            clean_data += sentences.encode('utf-8')
            #clean_data = clean_data.append(sentences.encode('utf-8'))

    return clean_data#str

def sanitize_links_and_hashtags(data):
    test =""
    for tweets in data:
        for text in tweets:
            text = re.sub(r'(http\S+|\@\S+|\#\S+)', " ", text)#remove links, tweetAts and hashtags(Not Proven To work)
            test += text
            # print(test)

    return test

def data_out(data): #writes it to a file for markov chain

    save_path = os.path.dirname(__file__)#'/Documents/MarkovianTweets/text/'
    completeName = os.path.join(save_path, "../text/"+ twitterHandleName +".txt")
    file = open(completeName,"w", 0)
    clean_data = sanitize_unicode(sanitize_links_and_hashtags(data))
    file.write(clean_data)#might need to be str(clean_data)
    file.close()
    #print(sanitize_unicode(sanitize_links_and_hashtags(data)))


def main():
    text = data_grab(twitterHandleName)#reads twitter handel iterates through chunks of tweets excluding replies and retweets
    data_out(text)#strips text of most funny stuff and puts it in test.txt
    print "Number of Tweets added to the test.txt file: " , TWEETCOUNTER   #counts tweets output to text file


if __name__ == "__main__":
    main()
