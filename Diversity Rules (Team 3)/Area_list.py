from area import *

Area1 = Area(1)
Area1.intro = "You go around Hyatt, talking to the people you know, having fun - both with colleagues from DSK, and both with new acquintances you made during the visit from OTP Group. Time flies fast - however, you do not notice and decide to take a quick break from the fun to \"powder your nose\". What harm could it do? Well, apparently, more than you anticipated - by the time you are finished, you cannot find anyone. Instead of panicking however, you quickly look around to figure out your option - you cannot miss this football match!\n"
Area1.choices = ["\nYou try to call one of your colleagues, but the lines seem to be broken. Now you might start to panic - but instead, you can always decide to walk to the stadium and figure out from there. Should not take more than 10 minutes, so you are sure to arrive on time! You are not taking any chances - who wants to go to Kar… in case you pick the wrong option?\n", 
                 "\nYou also see a standard looking bus, the one you would take to a regular business-like trip - you recall someone telling you the group goes together by bus. Maybe this is the best choice? But what if not? Unfortunately, the windows are darkened, so you cannot judge who is inside. The driver is urges you to enter - but what if the bus goes to Kardjali... and you are stuck on it?\n", 
                 "\nBehind the first bus, you notice a second one as well - but this one looks more secure. Could it be the bulletproof one the Chairman requested? From the looks of it - most probably. There are also more policemen sorrounding this bus.\n", 
                 "\nYou also notice an empty white Mercedes with the plate number …-777U. You remember seeing the same vehicle across all events today. Maybe the group left, but they recognized you were left behind, and this car is here to quickly take you to the location? You know there are no bulletproof buses in Sofia, and for sure this car is here to help you out. Seems logical - why else would it have followed the whole delegation for a full day, and why would not single one of your colleagues come to pick you up, if they were on the other bus?\n"]
Area1.outros = ["\nYou start walking towards the stadium with an increased speed, frequently checking your phone for the time. You are almost there when you receive a text message from Tamas: - Where are you? We are about to depart from the hotel!!! After quickly replying, you understand that you are more ahead than the rest of the group - you push away your thought of angering anyone with your behaviour, so start to feel your pulse getting calmer and calmer for a minute, before you are stopped by a group of protesters.\n", 
                "\nYou are very nervous as you rush toward the bus, but as you get closer and closer, you start hearing familiar voices - Bencsik, Wolf, Becsei, DSK colleagues… After a long sight, you take your place next to DSK Board members. You joke around a bit where you were - but all is fine. Unless you lost your ticket :) The bus closes the door immediately and you start heading to the stadium with police escort.\n", 
                "\nYou notice the door of the first bus closing as you walk by - maybe you also heard some familiar voices? Anyway, that is water under the bridge, you can always walk as worst case scenario. You confidently enter the bus from the front.\n", 
                "\nYou confidently open the door of the Mercedes. The driver welcomes you, and once checking your ticket, you head to the stadium.\n"]
Area1.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}, {"health": 0, "alcohol": 0, "chairman": 0}, {"health": 0, "alcohol": 0, "chairman": 0}, {"health": 0, "alcohol": 0, "chairman": 0}]
Area1.next_area = [2,6,3,5]

#Walking to the stadium
Area2 = Area(2)
Area2.intro = "\nThe protesters smile at you, but you notice they are dressed as standard football hooligans. Probably they are here to join the riot - however, your thoughts are stopped, as one of them addresses you directly, while the rest sorround you in a circle. - Hello stranger! Where are you heading? Everything is locked due to the match. Come, let's have some fun together, you are anyway stuck here, unable to enter the park. As he finishes his sentence, he pulls out a can of Kamenitsa from under his black leather jacket and hands it over to you. \n"
Area2.choices = ["\nAfter a quick thought, you decide to take the beer. Anyway you have time, the others are just about to depart - and this also seems to be the safer choice. Who knows what would happen if you reject? \n", 
                 "\nYou are not here to talk to some football rioters. Anyways, you do not even have a strong clue what this whole topic is about, so you do not want to run into some unfavourable discussions. You reject the beer and try to move forward. \n", 
                 ]
Area2.outros = ["\nYou open the can of beer and say cheers to all the rioters. They are smiling, and you are having fun. You discuss the Bulgarian and Hungarian political situation. Who thought they are a fan of Orban as well? You also manage to convince them to walk with you to the stadium as much as possible. You show your ticket to the guards, once you arrive - just on time, as the others arrive as well.  \n", 
                "\nTheir faces darken, as you reject the beer. The park also seems to go darker immediately, while you see the person putting the beer away. - So, you think you are too fancy for us? How nice. Let us teach you the other way! Before you could react, he spits at you and then immediately also punches you in the stomach. Humiliated, you rush towards the stadium. \n", 
                ]
Area2.attribute_updates = [{"health": 0, "alcohol": 1, "chairman": 0}, {"health": -1, "alcohol": 0, "chairman": 0}]
Area2.next_area = [6,6]

#Bulletproof bus
Area3 = Area(3)
Area3.intro = "\nAs you enter the bus from the front, you immediately notice that it is empty. The front is fully lighted, while the back of the bus is dark. Clearly, noone wants to sit anyone there. As you wonder if you are at the right bus at all, the driver asks you: - Are you heading to the football match? Can I see your ticket? Showing your ticket, he invites you to sit down - but where? \n"
Area3.choices = ["\nYou decide to sit in the front - anyway that it the only place where there is light. You prefer the window, maybe you can also see some policemen and protesters fighting on the way… \n", 
                 "\nOr, as you think further - maybe the bus is not bulletproof - it would be safer to sit close to the corridor. \n", 
                 "\nOr, maybe, there are also others coming with this bus? Even though, at this stage you are convinced everyone else was at the other bus. You go to the back of the bus, trying to dissappear in the pitch black area, and try to find a place there near the window. \n", 
                 ]
Area3.outros = ["\nAs you settle to your chair, the Chairman arrives. He looks at you with a questionmark on his face - you are sitting at his place! He looks back behind his back. Ivaylo Hadjiev - and some others - arrive, and ask you to leave the bus. You are rushed to the other bus, which was stopped just on the way to the stadium. Running in embarassment, you also trip, injuring yourself, before sitting down next to your colleagues on the bus. Their embarassing jokes are the highlight of the journey to the stadium. \n", 
                "\nAs you settle to your chair, the Chairman arrives. He looks at you with a questionmark on his face and then proceeds to sit next to you.\n"
                "\nYou notice the Chairman arriving. As it is dark, he almost did not even recognize you are there. He looks at you with a dissappointed look but otherwise - you dodged a bullet. \n", 
                ]
Area3.attribute_updates = [{"health": -1, "alcohol": 0, "chairman": -5}, {"health": 0, "alcohol": 0, "chairman": -3}, {"health": -1, "alcohol": 0, "chairman": -1}]
Area3.next_area = [6,4,6]

#QnA with Chairman on the bus
Area4 = Area(4)
Area4.intro = "\nFollowing a quick introduction with the Chairman, he accepts your presence. Now is your time to shine! Who cares about OKRs, when you can have 10 uninterrupted minutes with one of the most influential Hungarians??? As you start talking, the discussion quickly shifts towards football and the Hungarian's performance and history. The Chairman looks at you with a serious face and asks you: Who passed the ball to Ádám Szalai, who then scored Hungary's first Euro2016 goal against Austria? \n"
Area4.choices = ["\nLászló Kleinheisler \n", 
                 "\nBalázs Dzsudzsák \n", 
                 "\nZoltán Gera \n", 
                 ]
Area4.outros = ["\nThe Chairmans nods with a maybe even impressed look on his face. You did great and managed to turn the events into something maybe even advantageous! You hide a smile as you look out the window, surpassing the rioters. \n", 
                "\nThe face of the Chairman darkens - this was clearly not the right answer. You try to save the situation but what's done is done. For the rest of the trip, you sit in silence and you contemplate your life choices. This is the longest 5 minutes of your life. \n", 
                "\nThe face of the Chairman darkens - this was clearly not the right answer. You try to save the situation but what's done is done. For the rest of the trip, you sit in silence and you contemplate your life choices. This is the longest 5 minutes of your life. \n", 
                ]
Area4.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 5},{"health": 0, "alcohol": 0, "chairman": -5},{"health": 0, "alcohol": 0, "chairman": -5}]
Area4.next_area = [6,6,6]

#Drive with the Mercedes
Area5 = Area(5)
Area5.intro = "\nYou notice there is very fancy champagne and caviar on ice platter offered in the car. The driver looks back at you: - Those are very nice drinks prepared just for you. Enjoy the ride and don't let those go to waste! We will be there in 5 minutes tops, catching up to the bus. \n"
Area5.choices = ["\nYou decide to try the champagne and the caviar - they look really fancy and appetizing! \n", 
                 "\nYou reject the champagne and the caviar, to the visible dismay of the driver. \n", 
                 ]
Area5.outros = ["\nAs you exit the car, the others also just arrive, including the Chairman. He looks at you with a non-pleasant look as you exit the car, and you notice him whispering something to the person standing next to him. \n", 
                "\nAs you exit the car, the others also just arrive, including the Chairman. He looks at you with a non-pleasant look as you exit the car, and you notice him whispering something to the person standing next to him. \n", 
                ]
Area5.attribute_updates = [{"health": 0, "alcohol": 1, "chairman": -3}, {"health": 0, "alcohol": 0, "chairman": -3}]
Area5.next_area = [6,6]

#Sitting down in the stadium
Area6 = Area(6)
Area6.intro = "\nYou enter the stadium and after some security checks, you are in the Hungarian VIP lounge with everyone else. You look around, but decide to play it safe for now and stay with DSK colleagues, until you are rushed to sit down in the stadium to experience the match. You follow the orders and head outside to the cold. You also remember from the security checks your allocated seat - row 1, seat 1. However, both the stadium and the VIP section are empty. There is plenty of space! You see Tamas sitting with some Hungarians (clearly not on his assigned spot), and some DSK colleagues head to sit also in the middle in a different row. \n"
Area6.choices = ["\nRegardless, you decide to go to your assigned space alone. Better safe than sorry! \n", 
                "\nYou join some of the DSK colleagues who headed to sit in the middle - you are here to see the match and you prefer to enjoy it in nice company. \n", 
                "\nYou notice there are some leather chairs in the middle - they seem more comfortable than any other option, and noone is around securing the space or trying to sit there. Comfort first, the cold is enough to tolerate! \n", 
                "\nNoone seem to notice your presence, and you are alone, and it is cold. Maybe it is better to go back and enjoy the match from the warmth of the VIP lounge? For sure, some other people must have stayed there as well! \n"]
Area6.outros = ["\nSome other rule-abiding colleagues from DSK also arrive! You smile - this match will be fun! \n", 
                "\nAs you settle down, you notice the Chairman and some Bulgarian football association people approaching. They sit down in the leather chairs in front of you. You start to smile - you will be in TV probably! Though, maybe the Chairman wanted someone else to sit there? You will never know... \n", 
                "\nAs you settle down, you notice the Chairman and some Bulgarian football association people approaching, looking at you with a not so happy face. Before you could do anything, a few security people approach you and escort you to your assigned seat.  \n", 
                "\nYou have fun in the VIP zone with some random people, who convince you to take also some alcohol - anyway, anyone important to judge is watching the match, so what harm could it do? Nonetheless, after 2 shots, you decide not to continue with them and you join your colleagues in your allocated space, just in time to see live the first goal. \n"]
Area6.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}, {"health": 0, "alcohol": 0, "chairman": -1}, {"health": 0, "alcohol": 0, "chairman": -5}, {"health": 0, "alcohol": 2, "chairman": -3}]
Area6.next_area = [7,7,7,7]

#First goal (Hungary)
Area7 = Area(7)
Area7.intro = "\nThe Hungarian team scored the 1st goal! This is amazing - you should be happy, regardless of nationality - rights? \n"
Area7.choices = ["\nYou are impartial - did not even notice that the goal happened. You continue playing with your phone.\n",
                "\nYou decide to celebrate this event! And what better tool to do so, then to take a shot with some other happy fans, when they approach you? It is a great networking opportinity to be with people close to the Chairman!!! Cheers! \n", 
                "\nYou (maybe fake?) cheer with everyone else for the success of the Hungarian team - even if you do not care deep-down about the results. \n", 
                "\nThe Bulgarians just received a goal… you let out a slight boo and dissappointed voice. \n", 
                "\nYou start cheering very loud - the stadium is empty but you are here to ensure there is some mood, right? \n",
                "\nYou are so enthusiastic about this goal that you decide to run into the stadium - you even manage to steal a flag that you can wave along the way. Let's make this event fun!!! "]
Area7.outros = ["\nNothing happens... you were never even paying attention...\n",
                "\nYou shiver a bit from the shot but you are satisfied. You continue watching the game with your new friends for a while, before going back to your colleagues. \n", 
                "\nThe Chairman hears you shouting and cheering - he seems happy to have a new fan in the club. \n", 
                "\nThe Charman notices your reaction and lack of cheering: you are part of OTP Group, remember? \n", 
                "\nThe Chairman hears you shouting and cheering - he seems happy to have a new fan in the club. \n",
                "\nWell, this was not one of the best ideas. Not only you hurt yourself jumping down the stairs, you also drew a lot of police attention, who were already nervous due to the riots. They don't give you any chance to explain: you are taken to JAIL."]
Area7.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": -1}, {"health": 0, "alcohol": 1, "chairman": 1}, {"health": 0, "alcohol": 0, "chairman": 1}, {"health": 0, "alcohol": 0, "chairman": -3}, {"health": 0, "alcohol": 0, "chairman": 3}, {"health": 0, "alcohol": 0, "chairman": -100}]
Area7.next_area = [8,8,8,8,8,8]

Area2 = Area(2)
Area2.intro = "\n \n"
Area2.choices = ["\n \n", 
                 "\n \n", 
                 "\n \n", 
                 "\n \n"]
Area2.outros = ["\n \n", 
                "\n \n", 
                "\n \n", 
                "\n \n"]
Area2.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}]
Area2.next_area = [6,7,8,9]

Area2 = Area(2)
Area2.intro = "\n \n"
Area2.choices = ["\n \n", 
                 "\n \n", 
                 "\n \n", 
                 "\n \n"]
Area2.outros = ["\n \n", 
                "\n \n", 
                "\n \n", 
                "\n \n"]
Area2.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}]
Area2.next_area = [6,7,8,9]

Area2 = Area(2)
Area2.intro = "\n \n"
Area2.choices = ["\n \n", 
                 "\n \n", 
                 "\n \n", 
                 "\n \n"]
Area2.outros = ["\n \n", 
                "\n \n", 
                "\n \n", 
                "\n \n"]
Area2.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}]
Area2.next_area = [6,7,8,9]

Area2 = Area(2)
Area2.intro = "\n \n"
Area2.choices = ["\n \n", 
                 "\n \n", 
                 "\n \n", 
                 "\n \n"]
Area2.outros = ["\n \n", 
                "\n \n", 
                "\n \n", 
                "\n \n"]
Area2.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}]
Area2.next_area = [6,7,8,9]

Area2 = Area(2)
Area2.intro = "\n \n"
Area2.choices = ["\n \n", 
                 "\n \n", 
                 "\n \n", 
                 "\n \n"]
Area2.outros = ["\n \n", 
                "\n \n", 
                "\n \n", 
                "\n \n"]
Area2.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}]
Area2.next_area = [6,7,8,9]

Area2 = Area(2)
Area2.intro = "\n \n"
Area2.choices = ["\n \n", 
                 "\n \n", 
                 "\n \n", 
                 "\n \n"]
Area2.outros = ["\n \n", 
                "\n \n", 
                "\n \n", 
                "\n \n"]
Area2.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}]
Area2.next_area = [6,7,8,9]

Area2 = Area(2)
Area2.intro = "\n \n"
Area2.choices = ["\n \n", 
                 "\n \n", 
                 "\n \n", 
                 "\n \n"]
Area2.outros = ["\n \n", 
                "\n \n", 
                "\n \n", 
                "\n \n"]
Area2.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}]
Area2.next_area = [6,7,8,9]

Area2 = Area(2)
Area2.intro = "\n \n"
Area2.choices = ["\n \n", 
                 "\n \n", 
                 "\n \n", 
                 "\n \n"]
Area2.outros = ["\n \n", 
                "\n \n", 
                "\n \n", 
                "\n \n"]
Area2.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}]
Area2.next_area = [6,7,8,9]

Area2 = Area(2)
Area2.intro = "\n \n"
Area2.choices = ["\n \n", 
                 "\n \n", 
                 "\n \n", 
                 "\n \n"]
Area2.outros = ["\n \n", 
                "\n \n", 
                "\n \n", 
                "\n \n"]
Area2.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}]
Area2.next_area = [6,7,8,9]

Area2 = Area(2)
Area2.intro = "\n \n"
Area2.choices = ["\n \n", 
                 "\n \n", 
                 "\n \n", 
                 "\n \n"]
Area2.outros = ["\n \n", 
                "\n \n", 
                "\n \n", 
                "\n \n"]
Area2.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}]
Area2.next_area = [6,7,8,9]

Area2 = Area(2)
Area2.intro = "\n \n"
Area2.choices = ["\n \n", 
                 "\n \n", 
                 "\n \n", 
                 "\n \n"]
Area2.outros = ["\n \n", 
                "\n \n", 
                "\n \n", 
                "\n \n"]
Area2.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}]
Area2.next_area = [6,7,8,9]

Area2 = Area(2)
Area2.intro = "\n \n"
Area2.choices = ["\n \n", 
                 "\n \n", 
                 "\n \n", 
                 "\n \n"]
Area2.outros = ["\n \n", 
                "\n \n", 
                "\n \n", 
                "\n \n"]
Area2.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}]
Area2.next_area = [6,7,8,9]

Area2 = Area(2)
Area2.intro = "\n \n"
Area2.choices = ["\n \n", 
                 "\n \n", 
                 "\n \n", 
                 "\n \n"]
Area2.outros = ["\n \n", 
                "\n \n", 
                "\n \n", 
                "\n \n"]
Area2.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}]
Area2.next_area = [6,7,8,9]

Area2 = Area(2)
Area2.intro = "\n \n"
Area2.choices = ["\n \n", 
                 "\n \n", 
                 "\n \n", 
                 "\n \n"]
Area2.outros = ["\n \n", 
                "\n \n", 
                "\n \n", 
                "\n \n"]
Area2.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}]
Area2.next_area = [6,7,8,9]

Area2 = Area(2)
Area2.intro = "\n \n"
Area2.choices = ["\n \n", 
                 "\n \n", 
                 "\n \n", 
                 "\n \n"]
Area2.outros = ["\n \n", 
                "\n \n", 
                "\n \n", 
                "\n \n"]
Area2.attribute_updates = [{"health": 0, "alcohol": 0, "chairman": 0}]
Area2.next_area = [6,7,8,9]

#do this for all 21 areas

area_list = [Area1, Area2, Area3, Area4]
# to switch between areas: this can be imported into the main.py and use area_list as a normal variable with list indexing