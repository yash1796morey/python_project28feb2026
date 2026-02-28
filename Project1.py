##Fake Headling Project
import random

subjects=["Sharukh Khan","Virat Kohli",
          "Nirmala Sitaraman","A Mumbai Cat",
          "Group of Monkey","PM Modi",
          "Rikshaw Driver From Delhi"]

actions=["launches","cancels",
         "dances with","eats",
         "declare war on",
         "orders","celebrates"]

places_or_thing=["At Red Fort","Mumbai Local Train",
                 "a plate of samosa",
                 "inside parliment",
                 "At Ganga Ghat","During Ipl Match","At India Gate"]

#Start headline loop

while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place_or_thing=random.choice(places_or_thing)

    headline=f"Breaking news :{subject} {action} {place_or_thing}" 
    print("\n" + headline)
    user_input=input("\n Do you want another headline (yes/no)").strip().lower()
    if user_input=="no":
        break

##Print good bye message 
print("\n Thank you for using fake news headling generator.Have a fun day")
 