import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia
listener = aa.Recognizer()
machine = pyttsx3.init()
def talk(text):
    machine.say(text)
machine.runAndWait()
def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("Sun rha hu be")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if 'Jarvis' in instruction:
                instruction = instruction.replace('jarvis',"")
                print(instruction)
        
    except:
        pass
    return instruction
def play_jarvis():
    instruction = input_instruction()
    print(instruction)
    if 'play' in instruction:
        song = instruction.replace('khel',"")
        talk("suna rha hu" + song)
        pywhatkit.playonyt(song)
    elif 'time' in instruction:
        time = datetime.datetime.now().strftime("%I:%M%p")
        talk('Current time' + time)
    elif "date" in instruction:
        date = datetime.datetime.now().strtime("%d /%m /%Y")
        talk("today's date" + date)
    elif 'how are you' in instruction:
        talk("I m fine,what about you")
    elif "what is your name" in instruction:
        talk("I am daniels , what can i do for you ?")
    elif 'who is' in instruction:
        human = instruction.replace('who is',' ')
        info = wikipedia.summary(human,1)
        print(info)
        talk(info)
    else:
        talk("please repeat")
play_jarvis() 
