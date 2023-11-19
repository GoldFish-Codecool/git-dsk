from area import *

Area1 = Area(1)
Area1.intro = "\nAT HYATT\nYou go around Hyatt, talking to the people you know. Time flies fast - however, you do not notice and decide to take a quick break to \"powder your nose\". However, by the time you are finished, you cannot find anyone and your phone has no reception. You cannot miss this football match!\nWhat do you do?\n"
Area1.choices = ["\n 🚶 You decide to walk to the stadium and figure out from there. Should not take more than 10 minutes, so you are sure to arrive on time!\n", 
                 "\n 🚌 You also see a standard looking bus with darkened windows - you recall the group going together by bus. Maybe this is the best choice? But what if the bus goes to Kardjali... and you are stuck on it?\n", 
                 "\n 🚛 You notice a second bus as well - but this one looks more secure. Could it be the bulletproof one the Chairman requested? There are also more policemen sorrounding this bus.\n", 
                 "\n 🚗 You also notice an empty white Mercedes with the plate number …-777U. You remember seeing the same vehicle across all events today. Maybe the group left, but they recognized you were left behind, and this car is here to quickly take you to the location?\n"]
Area1.outros = ["\nYou start walking towards the stadium with an increased speed. You are certain that you are ahead than the rest of the group, so you start to feel calmer, before you are stopped by a group of protesters.\n", 
                "\nAs you get closer and closer, you start hearing familiar voices - Bencsik, Wolf, Becsei, DSK colleagues… After a long sight, you take your place next to DSK Board members. \n", 
                "\nYou notice the door of the first bus closing as you walk by - maybe you also heard some familiar voices? No other choice left: you confidently enter the bus from the front.\n", 
                "\nYou open the door of the Mercedes. The driver welcomes you and you head to the stadium.\n"]
Area1.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}, {"health": 0, "alcohol": 0, "chairman": 0}, {"health": 0, "alcohol": 0, "chairman": 0}, {"health": 0, "alcohol": 0, "chairman": 0}]
Area1.next_area = [2,6,3,5]

#Walking to the stadium
Area2 = Area(2)
Area2.intro = "\nWALK TO THE STADIUM\nThe protesters smile at you, however, probably they are here to join the riot. One of them addresses you directly, while the rest sorround you in a circle. After a few nice sentences, he pulls out a can of Kamenitsa from under his black leather jacket and hands it over to you. \n"
Area2.choices = ["\n 🍺 You decide to take the beer. Anyway you have time, the others are just about to depart - you are also unsure what would happen if you reject? \n", 
                "\n ❌ You are not here to talk to some football rioters. You reject the beer and try to move forward. \n"
                ]
Area2.outros = ["\n 🍺 You open the can of beer and say cheers to all the rioters. They are smiling, and you are having fun. You discuss the Bulgarian and Hungarian political situation. Who thought they are a fan of Orban as well? You arrive just on time, as the others arrive as well.  \n", 
               "\n 🤕 Their faces darken, as you reject the beer. You see the person putting the beer away. - So, you think you are too fancy for us? How nice. Let us teach you the other way! Before you could react, he punches you in the stomach. Humiliated, you rush towards the stadium. \n" 
               ]
Area2.attribute_updates = [{"health": 0, "alcohol": 1, "chairman": 0}, {"health": -1, "alcohol": 0, "chairman": 0}]
Area2.next_area = [6,6]

#Bulletproof bus
Area3 = Area(3)
Area3.intro = "\nAT BULLETPROOF BUS\nAs you enter the bus from the front, you immediately notice that it is empty. The front is fully lighted, while the back of the bus is dark. Clearly, noone wants anyone to sit back there. The driver invites you to sit down - but where? \n"
Area3.choices = ["\n 💺 You decide to sit in the front - anyway that it the only place where there is light. You prefer the window, maybe you can also see some policemen and protesters fighting on the way… \n", 
                "\n 💺 Or, as you think further - maybe the bus is not bulletproof - it would be safer to sit close to the corridor. \n", 
                "\n 🪑 Or, maybe, there are also others coming with this bus? You go to the back of the bus, trying to dissappear in the pitch black area. \n"
                ]
Area3.outros = ["\nAs you settle to your chair, the Chairman arrives. He looks at you with a questionmark on his face - you are sitting at his place! He looks back behind his back. Security arrives, and ask you to leave the bus. You also fell in embarassment on your way to the other bus.\n", 
                "\nAs you settle to your chair, the Chairman arrives. He looks at you with a questionmark on his face and then proceeds to sit next to you.\n",
                "\nYou notice the Chairman arriving. As it is dark, he almost did not even recognize you are there. He looks at you with a dissappointed look but otherwise - you dodged a bullet. \n"
                ]
Area3.attribute_updates = [{"health": -1, "alcohol": 0, "chairman": -5}, {"health": 0, "alcohol": 0, "chairman": -3}, {"health": -1, "alcohol": 0, "chairman": -1}]
Area3.next_area = [6,4,6]

#QnA with Chairman on the bus
Area4 = Area(4)
Area4.intro = "\n ❓ QNA WITH THE CHAIRMAN\nFollowing a quick introduction with the Chairman, now is your time to shine! 10 uninterrupted minutes with one of the most influential Hungarians??? \n\nAs you start talking, the discussion quickly shifts towards football and the Hungarian's performance and history. The Chairman looks at you with a serious face and asks you: \nWho passed the ball to Ádám Szalai, who then scored Hungary's first Euro2016 goal against Austria? \n"
Area4.choices = ["\nLászló Kleinheisler \n", 
                "\nBalázs Dzsudzsák \n", 
                "\nZoltán Gera \n", 
                ]
Area4.outros = ["\nThe Chairmans nods with a maybe even impressed look on his face. You did great and managed to turn the events into something maybe even advantageous! You hide a smile as you look out the window, surpassing the rioters. \n", 
                "\nThe face of the Chairman darkens - this was clearly not the right answer. For the rest of the trip, you sit in silence and you contemplate your life choices. \n", 
                "\nThe face of the Chairman darkens - this was clearly not the right answer. For the rest of the trip, you sit in silence and you contemplate your life choices. \n"
                ]
Area4.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 5},{"health": 0, "alcohol": 0, "chairman": -5},{"health": 0, "alcohol": 0, "chairman": -5}]
Area4.next_area = [6,6,6]

#Drive with the Mercedes
Area5 = Area(5)
Area5.intro = "\nDRIVE WITH THE MERCEDES\nYou notice there is very fancy champagne and caviar on ice platter offered in the car. The driver looks back at you, encouraging you to enjoy those items.\n"
Area5.choices = ["\n 🍷 You decide to try the champagne and the caviar - they look really fancy and appetizing! \n", 
                "\n ❌ You reject the champagne and the caviar, to the visible dismay of the driver. \n"
                ]
Area5.outros = ["\nAs you exit the car, the others also just arrive, including the Chairman. He looks at you with a non-pleasant look, and you notice him whispering something to the person standing next to him. \n", 
                "\nAs you exit the car, the others also just arrive, including the Chairman. He looks at you with a non-pleasant look, and you notice him whispering something to the person standing next to him. \n"
                ]
Area5.attribute_updates = [{"health": 0, "alcohol": 1, "chairman": -3}, {"health": 0, "alcohol": 0, "chairman": -3}]
Area5.next_area = [6,6]

#Sitting down in the stadium
Area6 = Area(6)
Area6.intro = "\nSITTING IN STADIUM\nYou enter the stadium and arrive to the Hungarian VIP lounge. After a while, you are rushed to sit down in the stadium to experience the match, so you head outside to the cold. \nYou remember your allocated seat - row 1, seat 1. However, both the stadium and the VIP section are empty. There is plenty of space! You see some DSK colleagues head to sit also in the middle in a different row. \n"
Area6.choices = ["\n 🪑 Regardless, you decide to go to your assigned space alone. Better safe than sorry! \n", 
                "\n 🪑 You join some of the DSK colleagues who headed to sit in the middle - you are here to see the match and you prefer to enjoy it in nice company. \n", 
                "\n 💺 You notice there are some leather chairs in the middle - they seem more comfortable than any other option, and noone is around securing the space or trying to sit there. Comfort first, the cold is enough to tolerate! \n", 
                "\n 🍷 It is cold. Maybe it is better to go back and enjoy the match from the warmth of the VIP lounge? For sure, some other people must have stayed there as well! \n"
                ]
Area6.outros = ["\nSome other rule-abiding colleagues from DSK also arrive! You smile - this match will be fun! \n", 
                "\nAs you settle down, you notice the Chairman and some Bulgarian football association people approaching. They sit down in the leather chairs in front of you. You start to smile - you will be in TV probably! Though, maybe the Chairman wanted someone else to sit there? You will never know... \n", 
                "\nAs you settle down, you notice security approaching. Before you could do anything, they escort you to your assigned seat.  \n", 
                "\nYou have fun in the VIP zone with some random people, who convince you to take also some alcohol. After 2 shots, you decide to join your colleagues in your allocated space, just in time to see live the first goal. \n"]
Area6.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}, {"health": 0, "alcohol": 0, "chairman": -1}, {"health": 0, "alcohol": 0, "chairman": -5}, {"health": 0, "alcohol": 2, "chairman": -3}]
Area6.next_area = [7,7,7,7]

#First goal (Hungary)
Area7 = Area(7)
Area7.intro = "\n ⚽ FIRST HUNGARIAN GOAL\nThe Hungarian team scored the 1st goal! This is amazing - you should be happy, regardless of nationality - rights? \n"
Area7.choices = ["\n 📱 You are impartial - did not even notice that the goal happened. You continue playing with your phone.\n",
                "\n 🍺 You decide to celebrate this event! You take a shot with some other happy fans, when they approach you. Cheers! \n", 
                "\n 🙋 You cheer with everyone else for the success of the Hungarian team. \n", 
                "\n 😥 You let out a slight boo in a dissappointed voice. \n", 
                "\n 🗣️ You start cheering very loud - the stadium is empty but you are here to ensure there is some mood, right? \n",
                "\n 🏃‍♂️ You are so enthusiastic about this goal that you decide to run into the stadium - you even manage to steal a flag that you can wave along the way!!! "]
Area7.outros = ["\nNothing happens... you were never even paying attention... Maybe someone noticed your lack of enthusiasm?\n",
                "\nYou shiver a bit from the shot but you are satisfied. After a few minutes, you go back to your colleagues. \n", 
                "\nThe Chairman hears you shouting and cheering - he seems happy to have a new fan in the club. \n", 
                "\nThe Charman notices your reaction and lack of cheering: you are part of OTP Group, remember? \n", 
                "\nThe Chairman hears you shouting and cheering - he seems happy to have a new fan in the club. \n",
                "\nWell, this was not one of the best ideas. Not only you hurt yourself jumping down the stairs, you also drew a lot of police attention, who were already nervous due to the riots. They don't give you any chance to explain: you are taken to JAIL."]
Area7.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": -1}, {"health": 0, "alcohol": 1, "chairman": 1}, {"health": 0, "alcohol": 0, "chairman": 1}, {"health": 0, "alcohol": 0, "chairman": -3}, {"health": 0, "alcohol": 0, "chairman": 3}, {"health": 0, "alcohol": 0, "chairman": -100}]
Area7.next_area = [8,8,8,8,8,23]

#Second goal (Bulgaria)
Area8 = Area(8)
Area8.intro = "\n ⚽ FIRST BULGARIAN GOAL\nThe Bulgarian team scored a goal! This is not so amazing - but a tie is still fine for Hungary, so it not all hope is lost. \n"
Area8.choices = ["\n 📱 You are impartial - did not even notice that the goal happened. You continue playing with your phone.\n",
                "\n 🍺 You decide to cheer up your mood with some alcohol. Cheers! \n", 
                "\n 🙋 You chant with everyone else to energize the Hungarian team. \n", 
                "\n 😥 You let out a quiet cheer in a happy voice. \n", 
                "\n 🗣️ You start chanting very loud RIA-RIA-HUNGARIA - the stadium is empty but you are here to ensure there is some mood, right? \n",
                "\n 🏃‍♂️ You are so enthusiastic about this goal that you decide to run into the stadium - you even manage to steal a flag that you can wave along the way!!! "]
Area8.outros = ["\nNothing happens... you were never even paying attention...\n",
                "\nYou shiver a bit from the shot but you are satisfied. \n", 
                "\nThe Chairman hears you chanting - even if the results are not great, he seems happy to have such a committed fan in the club. \n", 
                "\nThe Charman notices your reaction - he understands you might be from non-Hungarian nationality: but you are part of OTP Group, remember? \n", 
                "\nThe Chairman hears you chanting - he seems happy to have a new fan in the club. \n",
                "\nWell, this was not one of the best ideas. Not only you hurt yourself jumping down the stairs, you also drew a lot of police attention, who were already nervous due to the riots. They don't give you any chance to explain: you are taken to JAIL."]
Area8.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": -1}, {"health": 0, "alcohol": 1, "chairman": 1}, {"health": 0, "alcohol": 0, "chairman": 1}, {"health": 0, "alcohol": 0, "chairman": -3}, {"health": 0, "alcohol": 0, "chairman": 3}, {"health": 0, "alcohol": 0, "chairman": -100}]
Area8.next_area = [9,9,9,9,9,23]

#Half-time break
Area9 = Area(9)
Area9.intro = "\nHALF-TIME BREAK\nThe first half of the game is over. One more half to go. You head to the Hungarian VIP lounge with everyone else, with some chit-chats along the way. Once you arrive to the VIP zone, you look around, wondering what to do? \n"
Area9.choices = ["\n 🍺 Have a drink - the ones they serve seem to be really fancy! \n", 
                "\nYou decide to socialize with some people. You are here to network and build relations, if possible. \n", 
                "\nGo back to the stadium - you have some emails to read - and anyway, you are not in the mood to chitchat during such a short break. \n" 
                ]
Area9.outros = ["\nYou chat with a few people while having your drink. Afterwards, you head back to your place in the stadium. \n", 
                "\nYou look around, wondering who is free - you take a second to decide and think through what should be the best move. \n", 
                "\nYou work through the whole break, answering emails - however, it is very cold outside to be sitting for more than 90 mins overall in one place. You for sure will get a sore throat the next day! \n"
                ]
Area9.attribute_updates = [{"health": 0, "alcohol": 1, "chairman": 0}, {"health": 0, "alcohol": 0, "chairman": 0}, {"health": -1, "alcohol": 0, "chairman": 0}]
Area9.next_area = [13,10,13]

#With who to socialize with?
Area10 = Area(10)
Area10.intro = "\nSOCIALIZE\nYou see many people engaged in conversations already, some closer to the bar, some more further away. \n"
Area10.choices = ["\n 📱 You decide to stay with your colleagues - better safe than sorry! \n", 
                 "\nYou see an opportunity to talk with some Supervisory board members - this is your chance! You advance towards them. \n", 
                 "\nYou notice the Chairman - to everyone's surpise is standing alone. Can you maybe make a perfect impression now during the break? \n"
                 ]
Area10.outros = ["\nYou are having fun with all of them - such a nice bunch :) \n", 
                "\nYou approach Mr. Bencsik, who is with some other members of the Supervisory Board. You smile as you arrive at their table - this is your chance to shine! \n", 
                "\nYou approach the Chairman, maybe slightly nervous, thinking of what to do next. \n" 
                ]
Area10.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}, {"health": 0, "alcohol": 0, "chairman": 0}, {"health": 0, "alcohol": 0, "chairman": 0}]
Area10.next_area = [13,11,12]

#Talking with Supervisory board
Area11 = Area(11)
Area11.intro = "\nWITH THE SUPERVISORY BOARD\nYou feel maybe a but unwelcomed. This does not disturb you though, as you confidently initiate a conversation about what else, than football? All is fine, up to a point when you have to answer a question about Hungarian football: \nWho was Hungary's last opponent in the 2018 FIFA World Cup qualifiers? (as of February 2017) \n"
Area11.choices = ["\nLatvia \n", 
                 "\nAndorra \n", 
                 "\nSwitzerland \n" 
                 ]
Area11.outros = ["\nThe smile of the people at the table fade… you clearly acted more knowledable then you were. You try to stand your ground, as the table dismantles and everyone heads back to the match. \n", 
                "\nThey all smile as you confidently say out loud the right answer - sometimes it takes luck, sometimes knowledge. This discussion may help you in your carreer! \n", 
                "\nThe smile of the people at the table fade… you clearly acted more knowledable then you were. You try to stand your ground, as the table dismantles and everyone heads back to the match. \n"
                ]
Area11.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": -3}, {"health": 0, "alcohol": 0, "chairman": 3}, {"health": 0, "alcohol": 0, "chairman": -3}]
Area11.next_area = [13,13,13]

#Talking with the Chairman
Area12 = Area(12)
Area12.intro = "\nTALKING WITH CHAIRMAN\nThere is no chance now to second guess. You address the Chairman directly and try to steer the conversation into pleasant grounds - like football. It is going relatively fine, before he asks you: \nIn which city did Hungary lose against Belgium at Euro2016 Round of 16? \n"
Area12.choices = ["\nTouluse \n", 
                 "\nParis \n", 
                 "\nNice \n", 
                 "\nMarseille \n"]
Area12.outros = ["\nHe nods in silence, acknowledging your answer. You are relieved - this was a tough one to pass indeed! You manage to say a few more words, before someone takes the Chairman away. \n", 
                "\nHis face stays like a statue - unreadble. He leaves you, not even giving you a chance to wonder if your answer was right - your instincts show a clear direction though. \n", 
                "\nHis face stays like a statue - unreadble. He leaves you, not even giving you a chance to wonder if your answer was right - your instincts show a clear direction though. \n", 
                "\nHis face stays like a statue - unreadble. He leaves you, not even giving you a chance to wonder if your answer was right - your instincts show a clear direction though. \n"]
Area12.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 5}, {"health": 0, "alcohol": 0, "chairman": -5}, {"health": 0, "alcohol": 0, "chairman": -5}, {"health": 0, "alcohol": 0, "chairman": -5}]
Area12.next_area = [13,13,13,13]

#3rd goal for Bulgaria
Area13 = Area(13)
Area13.intro = "\n ⚽ SECOND BULGARIAN GOAL\nThe Bulgarian team scored a goal! This is not so amazing - Bulgaria is in the lead. Maybe not all hope is lost though... there is still some time left. \n"
Area13.choices = ["\n 📱 You are impartial - did not even notice that the goal happened. You continue playing with your phone.\n",
                "\n 🍺 You decide to cheer up your mood with some alcohol. Cheers! \n", 
                "\n 🙋 You chant with everyone else to energize the Hungarian team. \n", 
                "\n 😥 You let out a quiet cheer in a happy voice. \n", 
                "\n 🗣️ You start chanting very loud RIA-RIA-HUNGARIA - the stadium is empty but you are here to ensure there is some mood, right? \n",
                "\n 🏃‍♂️ You are so enthusiastic about this goal that you decide to run into the stadium - you even manage to steal a flag that you can wave along the way!!! "]
Area13.outros = ["\nNothing happens... you were never even paying attention...\n",
                "\nYou shiver a bit from the shot but you are satisfied. \n", 
                "\nThe Chairman hears you chanting - even if the results are not great, he seems happy to have such a committed fan in the club. \n", 
                "\nThe Charman notices your reaction - he understands you might be from non-Hungarian nationality: but you are part of OTP Group, remember? \n", 
                "\nThe Chairman hears you chanting - he seems happy to have a new fan in the club. \n",
                "\nWell, this was not one of the best ideas. Not only you hurt yourself jumping down the stairs, you also drew a lot of police attention, who were already nervous due to the riots. They don't give you any chance to explain: you are taken to JAIL."]
Area13.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": -1}, {"health": 0, "alcohol": 1, "chairman": 1}, {"health": 0, "alcohol": 0, "chairman": 1}, {"health": 0, "alcohol": 0, "chairman": -3}, {"health": 0, "alcohol": 0, "chairman": 3}, {"health": 0, "alcohol": 0, "chairman": -100}]
Area13.next_area = [14,14,14,14,14,23]

#Fourth goal (Hungary)
Area14 = Area(14)
Area14.intro = "\n ⚽ SECOND HUNGARIAN GOAL\nThe Hungarian team scored its second goal just last minute! This is amazing - you should be happy, regardless of nationality - rights? A tie is definitely better than a loss! \n"
Area14.choices = ["\n 📱 You are impartial - did not even notice that the goal happened. You continue playing with your phone.\n",
                "\n 🍺 You decide to celebrate this event! You take a shot with some other happy fans, when they approach you. Cheers! \n", 
                "\n 🙋 You cheer with everyone else for the success of the Hungarian team. \n", 
                "\n 😥 You let out a slight boo in a dissappointed voice. \n", 
                "\n 🗣️ You start cheering very loud - the stadium is empty but you are here to ensure there is some mood, right? \n",
                "\n 🏃‍♂️ You are so enthusiastic about this goal that you decide to run into the stadium - you even manage to steal a flag that you can wave along the way!!! "]
Area14.outros = ["\nNothing happens... you were never even paying attention... Maybe someone noticed your lack of enthusiasm?\n",
                "\nYou shiver a bit from the shot but you are satisfied. After a few minutes, you go back to your colleagues. \n", 
                "\nThe Chairman hears you shouting and cheering - he seems happy to have a new fan in the club. \n", 
                "\nThe Charman notices your reaction and lack of cheering: you are part of OTP Group, remember? \n", 
                "\nThe Chairman hears you shouting and cheering - he seems happy to have a new fan in the club. \n",
                "\nWell, this was not one of the best ideas. Not only you hurt yourself jumping down the stairs, you also drew a lot of police attention, who were already nervous due to the riots. They don't give you any chance to explain: you are taken to JAIL."]
Area14.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": -1}, {"health": 0, "alcohol": 1, "chairman": 1}, {"health": 0, "alcohol": 0, "chairman": 1}, {"health": 0, "alcohol": 0, "chairman": -3}, {"health": 0, "alcohol": 0, "chairman": 3}, {"health": 0, "alcohol": 0, "chairman": -100}]
Area14.next_area = [15,15,15,15,15,23]

#End of the game
Area15 = Area(15)
Area15.intro = "\nEND OF THE MATCH\nUhh… this was close. No matter your nationality, you are happy (at least partially) that the game did not end with a Bulgarian win. People stand up and start leaving the stadium. You follow the crowd, until you see some stairs going downstairs, just in front of where you could enter the VIP lounge. What do you do? \n"
Area15.choices = ["\nYou see Tamas going down the stairs - he must know better! You decide to follow him without any questions asked. \n", 
                "\nAfter some elaboration you go with the crowd to the VIP zone. \n", 
                "\nYou notice a press conference is about to start in a room they just opened. It might be interesting and worth checking out. \n" 
                ]
Area15.outros = ["\nYou leave the stadium safe. Maybe you missed to say Good Bye to a few Hungarians, but probably noone will notice. \n", 
                "\nAs you enter the VIP zone for at least the 3rd time, you feel the excited buzz of the room - this game was close! \n", 
                "\nAs you enter the press conference, you anticipate to feel the vibe of the room - many people running around, people waiting to interview, some professional setup. However, none of this happens, it is very empty. \n"
                ]
Area15.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}, {"health": 0, "alcohol": 0, "chairman": 0}, {"health": 0, "alcohol": 0, "chairman": 0}]
Area15.next_area = [18,16,17]

#VIP lounge after the game
Area16 = Area(16)
Area16.intro = "\nVIP LOUNGE\nPeople are already packing and preparing to leave. You can tell the Hungarians might be eager to get to the airport and head home soon. However, you notice some people saying cheers and congrats with beers and whiskeys. \n"
Area16.choices = ["\nYou decide to celebrate with the Hungarians - a nice cheers never hurt, right? You might even build new connections! \n", 
                "\nYou politely say goodbye to the visitors you met during the day and leave relatively quickly. \n"
                ]
Area16.outros = ["\nYou have fun for 10-15 minutes, meeting a few people from the Hungarian football assosiaction. You cannot even count how many times you raised your glass of alcohol to say cheers. \n", 
                "\nYou leave the room, just in time to see people gathering for the bus that took them to the stadium. \n"
                ]
Area16.attribute_updates = [{"health": 0, "alcohol": 1, "chairman": 0}, {"health": 0, "alcohol": 0, "chairman": 0}]
Area16.next_area = [18,18,18]

Area17 = Area(17)
Area17.intro = "\nPRESS CONFERENCE\nBefore you could leave, a nice young lady approaches you, with a camera guy closely following and shoves the microphone in your face once she realizes that you are from the Hungarian lounge. Before you have any change to react, you are looking face-to-face with a camera, a microphone and all the lightning. You try to do your best saying the most positive and generic answers you can ever come up with. However, this attempt is most noticable and the reporter also catches is, so she tries to get you out of your comfort zone in a nice way and ask you a question about the match: \nDo you think the referee was fair, or not? \n"
Area17.choices = ["\nYes \n", 
                 "\nNo \n" 
                 ]
Area17.outros = ["\nFor a second, you think you got the answer right - the interviewer and the colleagues start smiling. However, soon you realize that this was more of a petty smile than anything else. As you quickly leave the stadium, you will never be sure where this interview will be published, and if it is, where and to whom… God forbid you become the next meme of the Hungarian football fans! \n", 
                "\nFor a second, you think you got the answer right - the interviewer and the colleagues start smiling. However, soon you realize that this was more of a petty smile than anything else. As you quickly leave the stadium, you will never be sure where this interview will be published, and if it is, where and to whom… God forbid you become the next meme of the Hungarian football fans! \n" 
                ]
Area17.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": -5}, {"health": 0, "alcohol": 0, "chairman": -3}]
Area17.next_area = [18,18]

Area18 = Area(18)
Area18.intro = "\nON THE WAY HOME\nAfter leaving the stadium, you feel very close to getting to the end of your day. However, suddenly everyone you know from DSK dissappeared, there is noone to follow anymore. What do you do? \n"
Area18.choices = ["\nIt was a long day - you decide to walk home. \n", 
                "\nYou see the Hungarian people boarding the VIP bus - probably the others are on it already as well. \n", 
                "\nYou see and hear fans close to you celebrating - you decide that the night is young, it is time for a well-deserved celebration! \n"
                ]
Area18.outros = ["\nYou expect an uneventful yourney home, as you quickly start walking in the cold. \n", 
                "\nYou approach the bus, smiling at the familiar Hungarian faces. \n", 
                "\nYou head toward the fans - you will see soon, which country they cheered for. \n"
                ]
Area18.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}, {"health": 0, "alcohol": 0, "chairman": 0}, {"health": 0, "alcohol": 0, "chairman": 0}]
Area18.next_area = [19,20,21]

Area19 = Area(19)
Area19.intro = "\nWALKING HOME\nAfter a while, you come up to 2 path to get to your car. \n"
Area19.choices = ["\nThere is chance to go straight ahead - seems well lit, without any people in sight. However, there are many garbage on the ground and you might also smell something burning in that direction - maybe a trash bin? \n", 
                "\nYou are aware there is an alternative - a little bit longer, but all across darker areas. \n"
                ]
Area19.outros = ["\nYou meet the rioters for a short second. In order to avoid any further interaction with them, you decide to run for a few hundred meters - however, at the end of the part you trip, falling on your knees. You pick yourself back up, and arrive home safely. \n", 
                "\nYou walked a bit longer than needed maybe - you will never know. You get home safe. \n" 
                ]
Area19.attribute_updates = [{"health": -1, "alcohol": 0, "chairman": 0}, {"health": 0, "alcohol": 0, "chairman": 0}]
Area19.next_area = [22, 22]

Area20 = Area(20)
Area20.intro = "\nBOARDING THE VIP BUS\nAs you onboard the bus, you notice people looking at you with a strange face, wondering if you are Hungarian or Bulgarian? \n"
Area20.choices = ["\nBulgarian \n", 
                 "\nHungarian \n"
                ]
Area20.outros = ["\nThey explain you that this bus is for Hungarians heading to the airport only. They drop you off at Eagle's bridge, where you fall out of the bus in embarrasment, hurting your knee. \n", 
                "\nThey explain you that this bus is for Hungarians heading to the airport only. They drop you off at Eagle's bridge, where you fall out of the bus in embarrasment, hurting your knee. \n"
                ]
Area20.attribute_updates = [{"health": -1, "alcohol": 0, "chairman": -3}, {"health": -1, "alcohol": 0, "chairman": -5}]
Area20.next_area = [22,22]

Area21 = Area(21)
Area21.intro = "\nJOINING THE FANS\nThe fans rooted for Bulgaria, so they are drinking in dissappointment. You might also see a few familiar faces, you met earlier tonight as well? Nonetheless, they welcome you with open arms, offering you a drink. \n"
Area21.choices = ["\nYou take the drink, which looks like a weathered can of low-quality beer. You start discussing the match passionately. \n", 
                "\nYou reject the drink, and decide it might be more wiser to head home \n", 
                ]
Area21.outros = ["\nOne beer follows the next and next and next ones... you get drunk - maybe that's the reason how they managed to convince you to join the still ongoing small riot against the President of the Bulgarian Football assosiaction. You finish the night at JAIL. \n", 
                "\nThe fans are not happy that you do not join them, especially after they learn you also do not wish to riot further with them. They punch you in the stomach - after which you quickly rush home to safety. \n"
                ]
Area21.attribute_updates = [{"health": 0, "alcohol": 100, "chairman": 0}, {"health": -1, "alcohol": 0, "chairman": 0}]
Area21.next_area = [23,22]

#END GAME
Area22 = Area(22)
Area22.intro = "\nYou arrived home safely! \n"
Area22.choices = ["\nWhat happens next? Press 1 to find out."]
Area22.outros = ["\nLet's see..."]
Area22.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}]
Area22.next_area = [22]

#JAIL
Area23 = Area(23)
Area23.intro = "\nYOU WERE TAKEN TO JAIL \n"
Area23.choices = ["\nWhat happens next? Press 1 to find out."]
Area23.outros = ["\nLet's see..."]
Area23.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}]
Area23.next_area = [23]

area_list = [Area1, Area2, Area3, Area4, Area5, Area6, Area7, Area8, Area9, Area10, Area11, Area12, Area13, Area14, Area15, Area16, Area17, Area18, Area19, Area20, Area21, Area22, Area23]
# to switch between areas: this can be imported into the main.py and use area_list as a normal variable with list indexing

