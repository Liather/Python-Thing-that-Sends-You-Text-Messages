# Python-Thing-that-Sends-You-Text-Messages

This project is run by Twilio, a python library, used to send text messages. I have used Twilio to send myself insults through out the day. I have used the website http://www.robietherobot.com/insult-generator.htm to come up with the insults. I intend on automaticaly taking insults from this website rather than having a hard coded list.

Here are the steps to setting up (This is installing pip and python properly):

  Step 1 (Installing python): Go to the python website and install the python installer.https://www.python.org/downloads/
  
  step 2: When you open then the installer select the box to create path and click the top option. 
            ---If you open the python installer and it has three options (repair, uninstall and change) select uninstall. Once that is                    done repeat step 2---
            
  Step 3 (preparing to install pip): If you complete step 1 and 2 properly you can open command prompt (cmd) whcih you can do by opening              start menu and typing cmd. type python and hit enter. If you get this message below, move on to step 4. If not try again.
           .
           'Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
           Type "help", "copyright", "credits" or "license" for more information.'

Step 4: If you have successfuly complete the last 3 steps go to https://bootstrap.pypa.io/get-pip.py and copy all of the text. Open Python            idle and paste the text into a new project. Save this file and close python idle. Double click on the file you saved. To                  comfirm that you installed pip correectly, go to cmd and type pip and hit enter. If your pip installation was 
           successful then there should be information about pip. If you have been able to setup python and pip then you can move on to              setting up twilio

Here are the steps to get this working:

  Step 1: Go to the twilio website and and create an account. Next setup twilio by following this video
    https://www.youtube.com/watch?v=aE_5F49iH3g

  Step 2: Open cmd and type 'pip install twilio'
  
  Step 3: Open the 'send_sms.py' file.
