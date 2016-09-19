import facebook
import re
token = "Paste your access token over Here"
graph = facebook.GraphAPI(token)
#pages = ['rahuldravid']
profile = graph.get_object("Paste Your object Id")
posts = graph.get_connections(profile['id'],"posts") // this line would connect us to the facebook profile
for post in posts['data']:
        try:
            graph.put_object(post['id'],"likes") //this line would like all the posts of facebook
            graph.put_comment(post['id'],message="Long live rahul dravid") // I am going to comment "Long live rahul dravid"
            print "I am commenting :" +post["message"] // Just to check whether our script is working or not...Lets print message
        except:
            continue
