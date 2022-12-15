# **WhatsAppBot**
Whatsapp Bot for the home automation
This is a colaboratory project developed by two students Gorka Legarreta and Benjamin Tagwercher for the subject Internet of Things with the proffesor Diego Casado.
## **Description**
A device which is able to communicate through whatsapp with the user and can control different types of actors. E.g. you can send your device a message via whatsapp when it has to turn on the light. If you are on vacation and you don't have anyone who is looking for the house, you can turn on the lights so people don´t know that no one is at home. That way you can prevent potential thieves from breaking into the house. 
Later there is the possibility to add sensors like a gas sensor, so the whatsapp bot can keep track of if everything is alright with your house.
## **Functionality**
First you have to run the program. To start to communicate with the bot, you have to write **hello_bot**. The bot will respond with "Hi I am your Whatsapp Bot from RaspberryPi. I can help you with basic home automation. You can try any of the following commands turn on light - Turns on the led connected to pi turn off light - Turns off the led connected to pi". If you respond with **turn on light** the bot will respond "Sure, your Light is now turned on" and turnes on the light which is connected to the RasperryPi. If you respond with **turn off the light** the bot will respond "Sure, your Light is now turned off" and turn off the light which is connectd to the RaspberryPi. If you respond with anything else the bot will respond with "Sorry I could not understand your message. Please write again your request :)". If you are done and you want to turn the bot off you have to write **stop_bot** the bot will not answer anymore.
## **Packages required to run the program**
  - pip3 install opencv-python
  - pip3 install pyperclip
  - pip3 install pyautogui
## **Personal reflections**
### Gorka Legarreta
It has been an intense subject in which I have learnt a lot of theorical things abount the Internet of Things. At the end, have been challeged with a final project to confirm all the concepts we aknowledged about the raspberry, and its sensors and actuators. With my partner, we came up with the idea about how to implement home automation with the raspberry pi and with its actuators. In essence, our project at this stage does not use any sensor, as the input we have the Whatsapp messages we send to the computer, but the result could have not been better for the time we had.

### Benjamin Tarwercher
As I do not have a lot of experience with IT courses, I heard a lot of things for the first time. I have heared something about IOT before but did not really know what it is about. The course helped me to understand the basics of this topic. Through our project with the RaspberryPi I could have an insight into coding and what steps you have to follow to create a new program. I also learned how the Raspberry works and how to set everything up. I know later I am not going to work for a company in which I have to code, but I think it still might be helpful to have at least some knowledge in this topic.
