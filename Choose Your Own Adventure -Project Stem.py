import random
animals= ["squirrels", "rabbits", "birds", "foxes", "raccoons", "mice", "deer", "lizards", "frogs", "moths"]
num1= random.randint(1000,5000)
num2= random.randint(2,5)
anim= animals[random.randint(1,10)]


#ROADMAP
def roadmap():
    
    answer=input("\nWould you like to see a roadmap? (Type: YES or yes if so) ")
    if answer=="YES"or answer=="yes":
        print("\nType 1 to continue into the forest. "+ otherName+" gets shot and needs help.\nType 2 to find a place to stay for the night. The pair find an abandoned cabin.\nType 3 to retrace your steps. They get lost and stumble upon something.\n\nIf you chose 1: \n\nType HELP to leave and find help. "+name+" will trip and break their ankle and both of them will die in the woods. \nType WAIT to wait with "+otherName+" for help. Help eventually arrives and both people are saved. \nType SHELTER to carry "+otherName+" to shelter. "+otherName+" bleeds out and dies, and "+name+" wanders aimlessly into the woods alone, still searching for a way out.\n\nIf you chose 2:\n\nType BREAK to try to break in. They won't be able to and "+name+" breaks their finger in the process. They have to stay outside in the cold for the night and wake up feeling awful and unrested, still lost.\nType BACK to give up on the cabin and keep walking. They shortly find a little cave and build a fire. They sleep here and wake up well-rested to continue their journey. Eventually they'll make it out alive.\nType KEY to walk around the cabin trying to find a key or other way in. They go around the back and find a basement door. They creep in and find bones and chains on the floor. Scared, they hurry out and find themselves wandering through the night, only getting more lost.\n\nIf you chose 3:\n\nType SNAKE to find a snake in front of the two people. "+ otherName+" will accidentally provoke the snake and will be bitten, causing "+name+" to think to suck the poison out of their leg. Since this practice is a dangerous myth, the both of them end up infected and incredibly sick, unable to continue forward. \nType BEAR to find a bear. The two people have wandered into the nesting space of a mother and her cubs. On the defensive, the mother bear lashes out and strikes both "+name+" and "+otherName+". They lay with broken bones, and bleeding limbs, a perfect meal for the hungry family. \nType ROCK to find a huge rock. They climb the rock and are able to see the edge of the trees, pointing them in the right direction forward, out of the forest.")

#determine what they chose to do for the first option
def choice(chosen): #chosen= user input
    if chosen=="1":
        optionOne()
    elif chosen=="2":
        optionTwo()
    elif chosen=="3":
        optionThree()
        
    else:
        while chosen!="1" and chosen !="2" and chosen !="3":
            chosen=(input("That's not an option, please enter the number that represents your choice. "))
            if chosen=="1":
                optionOne()
            elif chosen=="2":
                optionTwo()
            elif chosen=="3":
                optionThree()

#first choice for first option
def optionOne():
    print("\n\nThey decide to continue walking into the forest, and suddenly a shot rings out. "+otherName+" yelps and falls to the ground, clutching their leg. \nBleeding out, "+otherName+" cries, \"Help me! Please, "+name+" ! \nA hunter has mistaken "+otherName+" for an animal, and they have been shot. \n" +otherName+ " begs for "+name+" to go get someone to help them. \nWhat should "+name+" do? ")
#asks what to do
    user=input("\nShould "+name+" leave "+otherName+" to find help? (Type: HELP) \n\nShould "+ name+" stay with "+otherName+" and wait for someone to find them? (Type: WAIT) \n\nShould "+name+" try to carry "+otherName+ " to find a shelter for the night? (Type: SHELTER) ")
#sets up for choices
    if user=="HELP":
        firstEndingOne(user)
    elif user=="WAIT":
        secondEndingOne(user)
    elif user=="SHELTER":
        thirdEndingOne(user)
        
    else:
        while user!="HELP" and user !="WAIT" and user !="SHELTER":
            user=(input("That's not an option, please enter the correct word that represents your choice. "))
            if user=="HELP":
                firstEndingOne(user)
            elif user=="WAIT":
                secondEndingOne(user)
            elif user=="SHELTER":
                thirdEndingOne(user)
                
                
#ending one for option one
def firstEndingOne(response): #response=user input 
    print("\n\n"+name+" gets up and tells "+otherName+", \"I’m going to go find someone to help us. Stay here.\"\n"+otherName+" grumbles and lays down as "+name+" runs off into the trees. "+name+" has no idea where they're going, and running aimlessly, trips over a tree root. "+name+"'s ankle breaks and they yell out in pain and frustration, at the realization that they won’t be able to get help for "+otherName+" in this condition, and they will both likely die out here. \n"+name+" and "+otherName+"’s stories come to a slow, and lonely end, never finding a way out of the woods.")
    
#ending two for option one
def secondEndingOne(response):
    print("\n\n"+name+" tells "+otherName+", \"Hold on, stay still, I have an idea.\"\n"+name+" tears a sleeve from their jacket and quickly ties a makeshift tourniquet on "+otherName+"’s leg. "+otherName+" grumbles in pain and weakly tells "+name+" to go find help once again.\n\"No, someone will come, I’m not going to leave you here,\" "+name+ " replies.\nAfter what feels like hours, the pair hear rushing footsteps coming from the distance, and the hunter from before comes dashing towards them, followed closely by three men carrying a stretcher and other medical equipment. Relieved, "+name+" pats "+otherName+", saying, \"See? Someone came for us.\"\n"+otherName+" smiles weakly, eyes still closed, as they’re carried onto the stretcher and the two are rushed to safety at last.")

#ending three for option one
def thirdEndingOne(response):
    print("\n\n"+name+" puts an arm around "+otherName+" and tries to hoist them up. Putting weight on "+otherName+"’s leg is excruciating and they whine in pain. \n\"I’m sorry "+otherName+", I’m really sorry, just hold on, we need to find somewhere safer to stay,\" "+ name+" pleads.\n\"I told you to just go,\" "+otherName+" says, breathlessly.\nThe two shuffle to a hollowed out edge of a mountain and rest under the rock. Hours pass and there is no sign of anyone coming for them. Slowly, "+otherName+" begins to fade out of consciousness, and with tears in their eyes, "+name+" cries, \"Please, just a little while longer, please, hold on.\"\n"+otherName+" doesn’t respond, and "+name+" weeps with regret for not listening to them and getting help like they said. \nThe sun rises over the trees and "+name+" watches it, expressionless, still sitting by "+otherName+". Slowly they stand and decide to continue to search for a way out.")
    

#second choice for first option
def optionTwo():
    print("\n\n"+name+" and "+otherName+ " decide to find a place to stay and wait out the night. After a long time of walking, the pair stumble upon a small cabin. \"It looks abandoned,\" "+otherName+" says. \nThey look in through the windows and find the one-room structure completely empty, with the doors locked. \n\"Well? What should we do?\" "+name+" asks. ")
#asks what to do
    userTwo=input("\nShould they try to break in? (Type: BREAK ) \n\nShould they turn back and find somewhere else to stay? (Type: BACK ) \n\nShould they search for a key to the door? (Type: KEY ) ")
#sets up for choices
    if userTwo=="BREAK":
        firstEndingTwo(userTwo)
    elif userTwo=="BACK":
        secondEndingTwo(userTwo)
    elif userTwo=="KEY":
        thirdEndingTwo(userTwo)
        
    else:
        while userTwo!="BREAK" and userTwo !="BACK" and userTwo !="KEY":
            userTwo=(input("That's not an option, please enter the correct word that represents your choice. "))
            if userTwo=="BREAK":
                firstEndingTwo(userTwo)
            elif userTwo=="BACK":
                secondEndingTwo(userTwo)
            elif userTwo=="KEY":
                thirdEndingTwo(userTwo)
                
                
#ending one for option two
def firstEndingTwo(responseTwo):
    print("\nThey want to break in. "+name+" and "+otherName+" push and pound on the doors and windows. In a final attempt, "+name+" gives it all they’ve got and punches the door. A loud crack sounds from their hand, and they cry out in pain.\n\"Hey, let’s give it a rest, okay? We can just sleep out here, we can take shifts and keep watch,\"  "+otherName+" suggests. \n"+name+" gives in, \"Okay, okay,\" they say, clutching their hand. \"You can sleep first if you want.\"\nThey take turns sleeping through the night, and as the sun rises, the pair are weak and tired. But they have to continue. They get up, and sleepily walk further into the forest for another day.")

#ending two for option two
def secondEndingTwo(responseTwo):
    print("\n\"I think we should try something else, let’s not waste daylight on this, we don’t have much left,\" "+name+" says, looking at the quickly setting sun.\nThey walk around the cabin and continue forward. Shortly, they stumble upon a small cave.\n\"Oh perfect!,\" "+otherName+" exclaims, \"This should work good for the night.\"\nThe two make their way into the cave and get settled in. Once a small fire is built, they get comfortable (or as comfortable as they can be on a bunch of rocks) and turn in for the night. \nThey wake up mostly well-rested, and get up to keep searching for a way out. A few hours pass and the tree line thins, showing promise of the edge of the woods. Their journey comes to a close, and they have found their way out at last.")

#ending three for option two
def thirdEndingTwo(responseTwo):
    print("\n\"Let’s see if we can find a key somewhere,\" "+name+ " suggests. They trace around the perimeter of the structure, checking under rocks and in window frames, but find nothing. They make their way to the back of the house and find a set of basement doors unlocked. \n\"Should we go in?\" "+ otherName+" asks.\n\"Do you have a better idea?\" "+name+" retorts.\nThey creep down into the dark basement. \nReaching the bottom of the humid room, their eyes adjust to find a shocking sight. A chain, slightly rusted, lays accompanied by an assortment of dirty bones about the floor. \nTerrified and confused, they quickly dash up the steps and hurry away from the cabin. \nIn their rush, they have wound up more turned around than before, with absolutely no hope of finding a way home.")

#third choice for first option
def optionThree():
    print("\n\nThey have decided to retrace their steps. They turn around and try to see if they can find any sort of footprints to tell them where they came from. They see a string of indentations in the ground and follow it, hoping they lead back out. \nThey walk and walk and walk, only feeling like they’re getting more lost, when suddenly the trail goes cold. \"Wait, look,\" "+otherName+" says, pointing in front of them. \nWhat does " +otherName+ " see?")
#asks what to do
    userThree=input("Is it a snake? (Type: SNAKE)\n\nIs it a bear? (Type: BEAR)\n\nIs it a huge rock? (Type: ROCK)")
#sets up for choices
    if userThree=="SNAKE":
        firstEndingThree(userThree)
    elif userThree=="BEAR":
        secondEndingThree(userThree)
    elif userThree=="ROCK":
        thirdEndingThree(userThree)
        
    else:
        while userThree!="SNAKE" and userThree !="BEAR" and userThree !="ROCK":
            userThree=(input("That's not an option, please enter the correct word that represents your choice. "))
            if userThree=="SNAKE":
                firstEndingThree(userThree)
            elif userThree=="BEAR":
                secondEndingThree(userThree)
            elif userThree=="ROCK":
                thirdEndingThree(userThree) 
                
#ending one for option three
def firstEndingThree(responseThree):
    print("A snake stands in the way of their path. "+name+" is frozen, cautious not to aggravate it, but "+otherName+" attempts to boldly step around it. The snake lunges out and strikes "+otherName+". \nIt slithers away and "+otherName+" writhes in pain, clutching their ankle.\n\"Help me! Do something, please!\" "+otherName+" cries.\n\"What am I supposed to do!?\" "+name+" responds, panicked.\n\"Aren’t you supposed to suck out the venom or something??\"\n"+name+" reluctantly bends down and raises "+otherName+"'s leg to their mouth. Disgusted, they attempt to get the venom out, but once they’re finished, they both feel more exhausted and sick than before.\n\"Did it work?\" "+name+" breathes, wiping spit from the corner of their mouth.\n\"I don’t know, let’s just rest for a second,\" "+otherName+" responds.\nAs the night passes, "+name+" falls sick and "+otherName+" seems to only grow worse.\nBy dawn the two have succumbed to their infections, starving, rotting, unable to move, and fading from consciousness, they regret ever coming to these woods.")
    
#ending two for option three
def secondEndingThree(responseThree):
    print("\"Oh god…\" "+name+" whispers.\nA large bear glares at the two, standing guard in front of her cubs. \n\"What do we do?\" \n\"Make ourselves bigger? Isn’t that what people say to do?\" "+otherName+" offers.\nThey try to puff up and slowly raise their arms above their heads, but the bear growls and swipes at them. They flinch suddenly, which triggers her and she pounces on them.\nShe tears them apart and calls her babies over to serve them their meal of blood and bones. \nThe happy ending belongs to the family with warm, full stomachs this time around. ")
    
#ending three for option three
def thirdEndingThree(responseThree):
    print("\"Woah…big rock,\" "+name+ " says.\n\"Yeah, great observation,\" "+otherName+ " retorts. \"Come on, let’s find out what we can see from up there.\"\nThey scale the boulder and once at the top, they scan the tree tops around them.\n\"Wait, look there, \" "+otherName+" points to the horizon where the trees begin to thin out, suggesting the edge of the forest.\n\"If we just go that direction we should get out, right?\" "+name+ " offers.\n\"Yeah, it looks like it\" "+otherName+ " agrees.\nThe two climbed down and set out towards home. They finally got out of the woods.")



#MAIN

name = input("What is your name? ")
otherName = input("Give me another name. ")
print("It's nice to meet you, "+ name+ ". ")

print("\n\n"+name+ " and "+otherName+ " have wandered into a forest. They are surrounded by "+str(num1)+" trees, and "+ str(num2)+ " " +anim+" dash by. \n"+name+" and "+otherName+" are unsure what to do, and the sun is beginning to set. \n"+otherName+" asks "+name+ ", \"I think we’re lost! What are we going to do?\" \n"+name+" pauses to think. ")
roadmap()

answer=input("\nShould they continue deeper into the forest? (Type: 1) \n\nShould they find a shelter to stay in for the night? (Type: 2) \n\nShould they retrace their steps? (Type: 3) ")
choice(answer)


print("\n\nThe End")






