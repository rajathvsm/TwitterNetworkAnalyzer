'''
Created on Oct 12, 2014

@author: moodi
'''
import twitter
from sys import argv
import networkx as nx
import matplotlib as plt
user = argv[1]
numOfLevels =2
api = twitter.Api("x", "y", "a", "b") 
#OAuth authentication

def fetchFollower(user):
    _followers=api.GetFollowers(screen_name=user)
    for follower in _followers:
        graph.add_node(follower.screen_name, followerCount=follower.followers_count)
        graph.add_edge(user, follower.screen_name)
    return _followers

graph=nx.DiGraph()
level=0
try:
#while (level<numOfLevels):
    followers=[]
    second_followers=[]
    followers=fetchFollower(user)
#    level+=1
    graph.add_node(user,followerCount=len(followers))
    for follower in followers:
        second_followers.append(fetchFollower(follower.screen_name))
    
except:
    print "Rate limit exceeded"
    pass    
# for f in second_followers:
#     print f.screen_name
print "First level of followers : "+str(len(followers))
print "Second level of followers : "+str(len(second_followers))
print "Total number of followers reached : " + str(graph.number_of_nodes()-1)
            
nx.draw_circular(graph)

nx.write_gexf(graph, user+".gexf")  
    