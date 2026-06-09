#google text to speech
from gtts import gTTS
import speech_recognition as sr
import playsound
from time import ctime
import os
import uuid
import smtplib
import webbrowser
# to make sure it listens
def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Start talking")
        audio= r.listen(source,phrase_time_limit=5)
    data=""
    #exception handeling
    try:
        data=r.recognize_google(audio,language='en-US')
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I cannot here you")
    except sr.RequestError as e:
        print("request failed")
    return data
listen()
#To respond back with audio
def respond(String):
    print(String)
    tts=gTTS(text=String,lang='en-US')
    tts.save("speech.mp3")
    filename="Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
#respond('hey codegnan how are you')
#start giving actions
#virtual assistant actions
def virtual_assistant(data):
    """ gives your actions"""
    if "how are you" in data:
        respond("Good and doing well")
    if "time" in data:
        listening=True
        respond(ctime())
    if "open google" in data.casefold():
        listening =True
        url="https://www.google.com/"
        webbrowser.open(url)
        respond("success")
    if "locate" in data:
        webbrowser.open('https://www.google.com/maps/search/'+data.replace('locate',""))
        result="located"
        respond("Located {}".format(data.replace("locate","")))
    if "email" in data:
        listening =True
        respond("Whome should i send email to?")
        to =listen().lower()
        edict={"lokesh":"lokeshdot72@gmail.com"}
        toaddr=edict[to]
        respond("What is the subject?")
        subject=listen()
        respond("what should i tell that person")
        message=listen()
        content='Subject :{}\n\n{}'.format(subject,message)
        #inir gmail SMTP
        mail=smtplib.SMTP('smtp.gmail.com',587)
        #identify the server
        mail.ehlo()
        mail.starttls()
        #login
        mail.login('mogalapallilokesh@gmail.com',"pmfp xjmt gwer fhhe")
        mail.sendmail('mogalapallilokesh@gmail.com',toaddr,content)
        mail.close()
        respond("Email Sent")
    if "stop" in data:
        listening =False
        print("listening stopped")
        respond("Okay done take care...")
    try:
        return listening
    except UnboundLocalError:
        print("Timedout")
respond("Hey lokesh how are you")
listening=True
while listening:
    data=listen()
    listening=virtual_assistant(data)
