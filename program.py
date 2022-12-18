import pyautogui as pygu #To move mouse cursor and make click and keyboard strokes
from time import sleep #for delay
import pyperclip #to copy and past data
import webbrowser #to open webbrowser
import os #to close webbrowser
import RPi.GPIO as IO            # calling header file for GPIO’s of PI
import time                              # calling for time to provide delays in program


IO.setwarnings(False) 
IO.setmode (IO.BOARD)       # programming the GPIO by BOARD pin numbers, GPIO21 is called as PIN40
IO.setup(40,IO.OUT)         # initialize digital pin40 as an output.
going_on = True             # Variable that controls the execution of the program

#Open the default webbrowser and open web.whastapp
webbrowser.open_new('https://web.whatsapp.com/')

default_message = [
    "Hi I am your Whatsapp Bot from RaspberryPi. I can help you with basic home automation. You can try any of the following commands",
    "*turn on light* - _Turns on the led connected to pi_",
    "*turn off light* - _Turns off the led connected to pi_"]

turn_on_light = [
    "Sure, your Light is now turned on"
]

turn_off_light = [
    "Okay, Your LED is not turned off"
]

sorry_message = [
    "Sorry I could not understand your message", "Please write again your request"
]

good_bye_message = [
    "Ok, I am shutting down now",
    "Bye"
]


#Wait for whatsapp page to
def open_whatsapp():
    # check if whatsapp opened successfully
    find_whatsapp_header = None
    while find_whatsapp_header is None:
        find_whatsapp_header = pygu.locateOnScreen("Whatsapp_header.JPG", confidence=.8)
        use_here_button_pos = pygu.locateOnScreen("use_here_button.JPG", confidence=.8)
        if (use_here_button_pos):
            print("Whatsapp is being used somewhere else, clicking on use here")
            sleep(2)
            pygu.moveTo(use_here_button_pos[0], use_here_button_pos[1], duration=0.5)
            pygu.click()
        print(".")
        sleep(2)
    return 1

#checks for new message and opens it
def new_chat_available():
    # Check for new messages
    green_circle_pos = pygu.locateOnScreen("green_circle.JPG", confidence=.8)
    if (green_circle_pos):
        sleep(0.5)
        pygu.moveTo(green_circle_pos[0], green_circle_pos[1], duration=0.5)
        pygu.click()
        sleep(0.5)
        ok_button_pos = pygu.locateOnScreen("ok_button.JPG", confidence=.8)
        if (ok_button_pos):
            pygu.moveTo(ok_button_pos[0], ok_button_pos[1], duration=0.5)
            pygu.click()

        return 1
    else:
        sleep(1)
        return 0

def read_last_message():
    smily_paperclip_pos = pygu.locateOnScreen("smily_paperclip.JPG", confidence=.6)
    pygu.moveTo(smily_paperclip_pos[0], smily_paperclip_pos[1])
    pygu.moveTo(smily_paperclip_pos[0] + 65, smily_paperclip_pos[1] - 35, duration=0.5)
    sleep(0.5)
    pygu.tripleClick()
    sleep(2)
    pygu.hotkey('ctrl', 'c') # Ctrl + c -> Copy the incoming message
    sleep(0.5)
    pygu.moveTo(smily_paperclip_pos[0], smily_paperclip_pos[1])
    pygu.moveTo(smily_paperclip_pos[0] + 355, smily_paperclip_pos[1] + 15)
    sleep(0.5)
    pygu.click()
    sleep(2)
    return (pyperclip.paste())

def get_response(incoming_message):
    if "hello_bot" in incoming_message:
        return default_message
    if "turn on light" in incoming_message:
        IO.output(40,1)                      # turn the LED on
        return turn_on_light
    if "turn off light" in incoming_message:
        IO.output(40,0)                      # turn the LED off
        return turn_off_light
    if "stop_bot" in incoming_message:
        going_on = False
    else:
        return sorry_message      # response to any other message that it is not defined



def send_message(message_content):
    for content in message_content:
        pygu.typewrite(content, interval=.02)
        pygu.hotkey('shift', 'enter')
    sleep(0.5)
    pygu.hotkey('enter') #Enter key to send the message

def new_message_available():
    current_mouse_pos = pygu.position()
    pointer_color = pygu.pixel(current_mouse_pos[0], current_mouse_pos[1])
    if (pointer_color == (255, 255, 255)):
        return 1
    else:
        return 0


if (open_whatsapp()): #if whatsapp page is opened successfully
    print("##Whatsapp page ready for automation##")

while(going_on):

    if (new_chat_available() or new_message_available()):
        print("New chat or message is available")
        incoming_message = read_last_message() #read the last message that we received

        message_content = get_response(incoming_message) #decide what to respond to that message
        send_message(message_content) #send the message to person
        
    sleep(10)







