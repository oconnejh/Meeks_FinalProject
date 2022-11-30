'''
Name: Sarah Zimmer, Sara Jundi, John O'Connell, Brett Perez
email: perezbd@mail.uc.edu
Assignment: Final Project
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: In this project, we use everything we learned during the semester to decipher a hidden message and display an image that proves we deciphered the message.
Citations: https://www.youtube.com/watch?v=uPT-LkYSP_o
Anything else that's relevant: 
'''

from PIL import Image

'''
#read the image
im = Image.open("John O'Connell High Res.jpg")

#show image
im.show()
'''

# Dictionary to store key value pair: (place #, associated word)
deciphererDict = {}

# Iteration to add each word to the dictionary along with the place #
with open('english.txt') as textFileKey: # Make Python open and look at text file containing word list
    for index, line in enumerate(textFileKey): # Iterate and assign number to each word
        formattedString = line.replace('\n','') # Fix word spacing before storing in Dictionary
        deciphererDict.update({index:formattedString}) # Add place # and word to dictionary as key value pair
       
