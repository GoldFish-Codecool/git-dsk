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