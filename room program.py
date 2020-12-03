#!/usr/bin/env python
# coding: utf-8

# In[332]:


import random

item_list = ['red fuse', 'purple relay', 'green fuse','computer module', 'orange relay', 'blue fuse', 'nothing', 'useless junk']
room_list = ['Right Thruster Room','Maintenance Room', 'Left Thruster Room','Observation Deck', 'Dining Area', 'Bridge','Quarters', 'Sick Bay','Command Center', ]

random.shuffle(item_list)
random.shuffle(room_list)

Zero = 'Zero Chamber'
Reactor = 'Reactor Room'
Doom = 'Reactor has gone into meltdown, game over!'
Trip = 'In rushing, you trip knocking yourself unconscious, '           'you awake with fleeting moments as the vacuum of space creeps closer'

start = input('You have awoken in your Zero Chamber, your ships circuitries'
              ' have failed due to electromagnetic pulse from nearby star-system. You must repair the mainframe'
              ' to get fusion reactor cooling back online before the reactor goes critical. You have 12 minutes'
              ', Select room to move to (left, down, right)')


def output(value1, value2, options):
    print('You have entered', value1)
    print('You found', value2)
    input('Where to next? (' + options + ')').lower().strip()
    
    
if start.lower().strip() == 'right':
    output(room_list[0], item_list[0], "left, down, right")
    if start == "left" or "Left":
        print(Zero)
    elif start == "down" or "Down":
        print('You have entered', room_list[4])
        print('You found', item_list[4])
    elif start == "right" or "Right":
        output(room_list[5], item_list[5], "left, down") 
    else:
        print(Trip, Doom)
elif start.lower().strip() == "left":
    output(room_list[1], item_list[1], "down, right")
          
elif start.lower().strip() == "down":
    output(room_list[2],item_list[2], "up,left, right")

else:
    print(Trip, Doom)


# In[ ]:




