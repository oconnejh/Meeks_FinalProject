from PIL import Image
import json

# Iteration to add each word to the dictionary along with the place #
def dictionary(txtFile):
    deciphererDict = {} # Dictionary to store key value pair: (place #, associated word)
    with open(txtFile) as textFileKey: # Make Python open and look at text file containing word list
        for index, line in enumerate(textFileKey): # Iterate and assign number to each word
            formattedString = line.replace('\n','') # Fix word spacing before storing in Dictionary
            deciphererDict.update({index:formattedString}) # Add place # and word to dictionary as key value pair
    return deciphererDict

# Get out dictionary data from EncryptedGroupHints.json
def encryptData(jsFile, groupName):
    with open(jsFile) as json_file:
        encryptedData = json.load(json_file)
        groupData = encryptedData[groupName] # Get our portion of the dictionary out
    return groupData

# Decipher the location by iterating over the dictionary and putting each word in a list
def decryptMessage(groupData, dictionary):
    answerList = [] # list to store results
    for i in groupData: 
        word_code = int(i) 
        answerList.append(dictionary[word_code]) #append list to store each answer
    return answerList


def display_image( filename ) :
    try:
        myimage = Image.open(filename)
        myimage.show()
    except:
        return None