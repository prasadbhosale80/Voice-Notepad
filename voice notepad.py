#YT link for help:https://www.youtube.com/watch?v=1I8MdTszcv8&t=692
fname=str(input("Write your File Name with extention",))
import speech_recognition as s
sr=s.Recognizer()
print("Speak what you want to type")
with s.Microphone() as m:
    audio=sr.listen(m)
    try:
        query=sr.recognize_google(audio,language='eng-in')
        print("\n",query,"\n")
        print("Done yor file opening soon...")
    except:
        print("Could not recognize Speak again")

f = open(fname, "a")
f.write(query)
f.close()

f = open(fname,"r")
print("\n\n\n",f.read(),"\n")
