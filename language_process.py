import re #For finding patter
import time #For timing functions' times



SUBJECT_1 = ['I','We']
SUBJECT_2 = ['You']
SUBJECT_3 = ['He','She','It','They']
SUBJECT = SUBJECT_1 + SUBJECT_2 + SUBJECT_3

message = input()
translated_text = ''
startTime = time.time()

subjectRegex = re.compile(r'(I|We|You|He|She|It|They)')

def detectVerbing():
    subject = subjectRegex.search(message)
    if subject.group() != None:
        print('Subject detected :',subject.group())

def detectSubject():
    for word in message.split():
        if word.title() in SUBJECT:
            print('Subject detected : ',word)

def detectContinuousPresentTense():
    for word in message.split():
        if word.title() in SUBJECT:
            print('Subject detected.')


    for i in range(len(message)):
        if message[i] == "'":
            print('Subject detected.')

detectVerbing()
print(time.time(), startTime)


    