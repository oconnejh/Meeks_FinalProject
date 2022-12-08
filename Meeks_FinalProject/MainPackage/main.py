'''
Name: Sarah Zimmer, Sara Jundi, John O'Connell, Brett Perez
email: perezbd@mail.uc.edu, zimmese@mail.uc.edu
Assignment: Final Project
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: In this project, we use everything we learned during the semester to decipher a hidden message and display an image that proves we deciphered the message.
Citations: 
https://www.youtube.com/watch?v=uPT-LkYSP_o
https://www.geeksforgeeks.org/convert-json-to-dictionary-in-python/
https://stackoverflow.com/questions/41276755/convert-txt-file-into-a-list-of-integers-in-python
Anything else that's relevant: 
'''

from Functions import *
import os

englishDict = dictionary('english.txt')
#print(englishDict)

meeksData = encryptData('EncryptedGroupHints.json', 'Meeks')
#print(meeksData)

meeksMessage = decryptMessage(meeksData, englishDict)
print(meeksMessage)
display_image(os.path.dirname(os.path.abspath(__file__)) + "/MeekGroupPic.jpeg")