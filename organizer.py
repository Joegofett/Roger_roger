import re

def clean(data): 
    """
    Final returns incremental keys 0-x each corresponding to a value that is a string example below 

    Message: Hello all this is a message 

    final = {0: 'Hello', 1 : 'All', 2 : 'this', 3 : 'is', 4 : 'a', 5 : 'message' }

    """
    new_data = data
    newList = new_data.split(' ')
    final = {}
    key = 0
    for info in newList:
        final[key] = info
        key += 1
    return final


def question(data):
    new_data = data
    newList = new_data.split(':')
    final = {}
    key = 0
    for info in newList:
        final[key] = info
        key += 1
    return final



def pollOptions(data):
    #new_data = data
    seperator = question(data)
    newList = seperator[2].split(',')
    temp = {}
    key = 0
    for info in newList:
        temp[key] = info
        key += 1
    return temp


def pollPrinter(questionid, optiond):
    """
    Input is two dict first dictionary is data split by : and the other is split by commas, the comma one is added together since they are the options 
    TODO add some type of catch for the 20 limit. Currently you can only have 20 emojis 
    """
    #new_sentence = questionid[1] + options
    old_sentence      = ""
    for x in optiond:
        old_sentence   += ',' + optiond[x]  
        #optionSection = options 
    new_sentence      = 'Poll:' + questionid[1]+ ':' + old_sentence
    return new_sentence
    
    
    
    
def emojis(optiond):
    for x in optiond:
        y = x + 1
    while y > 10:
        -1
        
    return y -1