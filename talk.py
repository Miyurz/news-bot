from espeakng import ESpeakNG
import time as t

esng = ESpeakNG() 
esng.voice = "en-us+f3"
esng.pitch = 32
esng.speed = 150 
esng.say('Hello World!')

t.sleep(2)

esng.voice = 'german+f4'
esng.say('Hallo Welt!')

t.sleep(2)
esng.voice = 'english-us+f2'
esng.say("[[h@l'oU w'3:ld]]")

