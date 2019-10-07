#importing the Twilio library and the Twilio client
import twilio
from twilio.rest import Client
#import random and time
import random
import time

#creating the 4 variables /Remember the account_sid etc go in the ''\
account_sid = 'account_sid'
auth_token = 'auth_token'
my_phone_number = 'my_phone_number'
my_twilio_phone_number = 'my_twilio_phone_number'

#these are the insults that will get sent to you
insult_list = ['Kill yourself!',
          'You are a waste of space!',
          'You are a waste of oxygen!',
          'You fucking asshole!',
          'Bitch Face!',
          'Pompous Shit Knob',
          'Idiotic Butt Dragon',
          'Racist Turd Pirate',
          'Dicknose Turd Socket',
          'Pie-Eating Nut Knob',
          'Racist Shart Blossum',
          'Butterface Slut Blossum',
          'Butterface Bitch Canoe',
          'Racist Fuck Hammer',
          'Lazy Cock Biscuit',]

#setting up the client
client = Client(account_sid, auth_token)

#this is where the message gets sent
x=0
for x in range(5):                  #to the phone number, where from            and what is in the message. Random insult from insulat list
    message = client.messages.create(to=my_phone_number, from_=my_twilio_phone_number, body=insult_list[random.randint(0,len(insult_list))])
    #time.sleep(5) This is where you can put a delay between how long between each insult
