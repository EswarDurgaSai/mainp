from gtts import gTTS
import os
#open the text file and read it
text_file=open("u.txt","r").read()
 
#convert text to speech
speech=gTTS(text=text_file,lang='tl',slow=True)

#save the speech as an mp3 file
speech.save("voice.mp3")

#play the generated audio using the default media player
os.system("start voice.mp3")