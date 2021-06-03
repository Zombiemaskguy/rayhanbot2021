daEmail = "fatty" #put discord email here
daPassword = "fatty" #put discord password here
daUser = "fatty" #put discord user id here
#put list of words here
daVerbList = ["stop", "quit", "no", "keep", "why are you"]
daVerb2List = ["eating", "dying", "being fat", "throwing", "smoking crack"]
daNounList = ["you"]
daAdjectiveList = ["fat", "obese", "stupid", "idiodic", "uneducated", "illeterate"]
daNounList2 = ["fool", "noob", "monkey", "idiot", "fatty", "ewers-lover", "bitch", "simp"]
daFinisherList = ["lmao", "lol", " ", "stfu", " ", " "]
daChannelList = ["769029458861752332"]
daServer = "716121096197242890"
msgAsReply = True


#You don't need to change anything under this
daChannelDictionary = dict.fromkeys(daChannelList, "")
def getCreds():
    return(daEmail,daPassword)
def getCompliments():
    return(daVerbList, daVerb2List, daNounList, daAdjectiveList, daNounList2, daFinisherList)
def getScope():
    return(daUser,daChannelDictionary,daServer)
def getMisc():
    return(msgAsReply)