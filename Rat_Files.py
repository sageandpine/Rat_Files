# import the exit function from the sys module
from sys import exit



# Kill character and exit game
def dead(why):
    print(why, "No book deal....you dead.")
    exit(0)

def mad_sci_room():
    print("""
            You enter the room. It feels like the last room.

            It is dark except for a single pulsing Jacobs ladder in a far corner.
            A rotten egg stench fills your delicate nostrils.
            Scratching at the wall for a light switch, a thunderous laugh fills the room
            and a green light begins to fill the room. A large dark shadow is outlined, looming.

            From the evil maw a rumbling growl says, "You have come for the syrum of life!
            You will not be successful! You want to finish this program!
            You will FAIL!
            You have one chance to defeat me.
            Give me your cutest pose!
            If you sway me with your cuteness, then you will win the game
            and get the life extending liquid and the recipe to
            replicate it!"
                                  You have 2 options for poses to strike Pancake
                                              1: Wiggle Butt
                                              2: Pancake Shake
                                                           choose wisely.....
    """)
    move_me = input("> ")
    if 1 or 2 in move_me:
        print("""
                The laughs of the scientist are quieted. All the lights come up.
                "You win! Congratulations!"
                He runs to the window and let's the fresh breeze in the room!

                Birds fly in, rats rush into the room and he hands over a bag.
                "Pancake," he says "You fought hard!
                I would like to give you anything you want.
                First, though, this bag contains the yogis of life.
                Also found inside are the recipes as well.
                Now you can live as long as your human counterparts!
                Spread the love and the word!"

                You are so happy but there's one thing missing.....

                "Sir, I'm not sure why all of this happened,
                but im still human size and I need to be able to
                cuddle in my moms special spot!" you plea,
                "What can be done for me?"

                A smile breaks over his suddenly jovial face.
                "Step over to my shrink ray and we'll fix that!"

                You step under the shrink ray and
                                                   >>>ZAP!<<<
                                                          You're small again.
                Just when you think it couldn't get any better,
                your soul mate walks though the door!

                "PANCAKE!" She shouts, running over and scooping you up
                Holding you close with tears of joy flowing she says,
                "I've missed you so and I'm never going to let you go!!!!"

                Book Deal is signed.
                
                We are all bruxing and boggling.

                All is well in the universe.

                Congratulations

                Love and cuteness have prevailed!


                                                     Thanks for playing!
                                                                 -sage&pine-
        """)
        exit(0)

#-----combine rat cage and statue room-----------------------------------------------------------------------

def statue_room():
    print("""
            Statues of animals line the walls of the west,
            while statues of humans in lab coats line the east.
            The North East wall has a large door with a
            grouping of cages next to it.
    """)
    move_me = input("> ")
    if "east" in move_me:
        print("""
                As you approach the door you notice that the cages are filled with sad skinny rats.
                There is a box of yogi treats just out of their reach!
                In a fit of rage, you rip open the cages and set the rats free!

                They thank you as they engourge themselves on yogis.
                Dissappearing, into holes in the wall, one stops and says,
                "Pancake, you are the savior we've been waiting for!
                You must wrestle the yogis of life from the mad scientist!
                I must go but the rattie spirit is with you!
        """)
        mad_sci_room()
    elif "west" in move_me:
        print("""
                Going back so soon?
        """)
        sci_lab()
    else:
        print("""
                It's sad that you are forgetting how to use your words.
        """)
        dead("You were nicked by the scientists poison.")

#------------------------------------------------------------------------------
#
def sci_lab():
    print("""
            A scientist has their back to you at a small desk.
            He is next to the only door in the room. He is muttering
            incoherently to himmself.

            Bumbing a small red solo cup on the ground with your foot,
            the scientist jumps up with a start. Menace in his eyes,
            he quickly snatches a syringe with a sinister looking liquid in it.

            "I'm not here for trouble," you say, trying to keep the peace
            "I'm simply trying to find my way back to my perfect person, my soul mate,
            Stevie".

            The scientist laughs making it clear that you are in trouble.
            So what's it going to be....
                                        'Fight' or 'Flight' Pancake?
    """)
#north south
    move_me = input("> ")
    if "fight" in move_me:
        print("""
                Prepared for a fight you remember the rope in your belt.
                As the villian lunges at you, you move just in time to avoid the poison
                held in the dripping needle tip.
                Falling back on your haunches, you are able to grip the rope in one hand
                while swiping his legs with your tail!

                Off balance, he falls back but recovers quickly.
                You think it might be too late for you, he's too quick!
                Just then, your small hand swings the rope Indiana Jones style
                and it wraps tightly around his neck!

                As he struggles to free himself from the ropes restrictions,
                you grab the syringe from the air as it falls from his fingers.
                Plunging it deep into his neck, he let's out a scream.
                You empty all of the contents into him, feeling a moment of remorse
                that quickly abates as the evil in his eyes flash once more at you
                in disbelief.

                He slumps over. Dead? Asleep? Either way,
                it doesn't seem like he's moving any time soon.

                The door behind him is now unobstructed.
                You go North through the door to your next challenge.
        """)
        statue_room()
    elif "flight" in move_me:
        dead("""
                Turn around to run but trip over your tail.
                As your consciousness fades you see the scientist looming over you with a
                syringe...
        """)
    elif "north" in move_me:
        dead("""
            You make an attempt to distract him by flicking the solo cup
            across the room with your tail, but he's not distracted....he's clearly cooked up
            his own amphetamine. He lunges at you and catches you in the rump with the syringe. You feel
            warm all over as your vision fades to black....
        """)
    else:
        print("""
                You took too long to think about it!
        """)
        dead("The scientist injects you with a deadly syrum and you feel your body go limp...at least you don't feel a thing.")


def long_hall():
    print("""
            You are in a poorly lit corridor that is made of wet stone.
            It is like you are descending while staying on flat.
            You recall seeing a river flow uphill in your distant memory.
            The memory is a flash and then it is gone.

             You come to the end of the hallway and step into a room filled with the clicking
             of a keyboard.""")
    sci_lab()





#-----------------------------------------------------------------------
def north_rope_room():
    print("""
            The door is open and leads North.
    """)
    move_me = input("> ")
    if "north" in move_me:
        print("""
                You walk towards the North door.
        """)
        long_hall()
    elif "south" in move_me:
        print("""
                About face! You turn the hell around!
        """)
        rope_room()
    else:
        print("""
                Ya gotta do somethin here!
        """)
        north_rope_room()

#------------------------------------------------------------------------------
def rope_room():
    print("""
            After swinging the creaky door open on it's hinges,
            you step into a room with a small table directly in front of you.
            A small desk lamp emits an eerie yellow light into the room.
            You almost trip over a pile of rope!
            Better throw that on your belt for later!

            On the North wall there is a door.
            South, there is a bad rendition of the Mona Lisa on the wall.
    """)
# north south west
    move_me = input("> ")
    if "north" in move_me:
        print("""
                You walk towards the north door.
        """)
        north_rope_room()
    elif "south" in move_me:
        print("""
                There's not much to look at. Definitely a forgery!
                In fact it makes you queezy the closer you get.
                You rethink this and go back over to the door you
                came in through to re-evaluate things.
        """)
        rope_room()
    elif "west" in move_me:
        print("""
                You turn around and walk back through the door.
        """)
        tv_room()
    else:
        dead(0)



#------------------------------------------------------------------------------
def south_basement():
    print("""
            On the table there is a crate full of cheese!
            You are hungry too!
            You start to eat it.
            That's when you notice the note on the table...
    """)
    action = input("> ")
    if "note" in action:
        print("""
                The note is on stationary from 'Beakmans Gas Station'.
                It says in scrawled text
                                   ---'Live long....
                                       free the rats from the burden....
                                       long live Pancake!'---
                The cheese is gone. You have the cryptic note.

                Now which direction?
            """)
        print("                    ")
        action = input("> ")
        if "north" in action:
            print("""
                    You choose North.
            """)
            basement_2()
        else:
            print("""
                    You said anything but North.
            """)
            dead("Don't be silly.")
    elif "north" in action:
        print("""
                You chose North.
        """)
        basement_2()
    else:
        print("""
                You said anything but North.
        """)
        dead("Don't be silly.")
#------------------------------------------------------------------------------
def basement_2():
    print("""
            The basement is dark.
            Looking South, you see a table that has a wooden crate.
            North there is a brick wall you can touch.
            Behind you is the staircase that goes back up.
    """)
    move_me = input("> ")
    if "south" in move_me:
        print("""
                You go South!
        """)
        south_basement()
    elif "up" in move_me:
        print("""
                So Soon? Okay I guess.
        """)
        tv_room()
    elif "north" in move_me:
        print("""
                You are already North ya dork.
                            But hey you're pancake.
                                         Do what you want,
                                                     you're cute!
        """)
        basement_2()
    else:
        print("""
                Okay. That's cool. You're cool.
        """)
        basement_2()

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------#
def basement():
    print("""
            The basement is dark but on the floor is a toolbelt.
            As you pick it up and slide it around your waist,
            a key falls to the floor with a clink. Dope!
            You pick it up!

                Looking South, you see a table that has a wooden crate.
                North, there is a brick wall you can touch.
                Behind you is the staircase that goes back up.
    """)
    move_me = input("> ")
# behind, South, North
    if "south" in move_me:
        print("""
                You go South!""")
        south_basement()
    elif "up" in move_me:
        print("""
                So Soon? Okay I guess.""")
        tv_room()
    elif "north" in move_me:
        print("""
                You are already North ya dork.
                But hey, you're Pancake.
                Do what you want,
                             you're cute!""")
        basement_2()
    else:
        print("""
                okay, that's cool. you're cool.""")
        basement()
#------------------------------------------------------------------------
def tv_room():
    print("""
            You are in a rectangular room that stretches East to West.
            Analog Televisions line the walls and show images of
            rats with wires coming from their exposed brains!

            There is one door on the East wall.
            You notice a single television on the West wall flickering with static.
    """)

    move_me = input("> ")
    if "east" in move_me:
        print("""
                Going East, you arrive at the door.
                You notice the door is very fragile and looks to be coming
                off it's hinges.
        """)
        move_me = input("> ")
        if "open" in move_me:
            print("""
                    The door swings open, creaking
            """)
            rope_room()
        else:
            tv_room()
    elif "west" in move_me:
        print("""
            You approach the West wall and notice the flickering Television
            is the only one with a power button. How strange. Want to push the button?
            Nah probably a bad idea. Okay you push it.....

                The screen goes black and you hear the whirring of
                gears behind the wall. The wall behind the screen slowly swings open
                on unseen hinges revealing a staircase that goes down.
        """)
        move_me = input("> ")
        if "down" in move_me:
            basement()
        elif "east" in move_me:
            print("and back we go....")
            tv_room()
        else:
            dead("playing it safe? ya burnt.")
    elif "south" in move_me:
        start_room_2()
    else:
        print("Try something else")
        tv_room()


#--------------------------------------------------------------------------#
def start_room_2():
    print("""
            You are in a small concrete room.
            A solitary bulb swings overhead.
            There is a door in front of you that your rat whiskers sense
            is due North.
    """)
    move_me = input("> ")
    if "open" in move_me:
        tv_room()
    else:
        print("All right it's not hard, type open and let's go!")
        start_room_2()


#-------------------------------------------------------------------------#
def start_room():
    print("""
            You wake up in a small concrete room.
            A solitary bulb swings overhead.
            You can't recall how you got here.
            Your name is pancake.
                    You are a rat.

            There is a door in front of you
            and your rat whiskers sense it's due North.
            Other than a badass tail, you are naked.
            Naked and Hairless.
                              'I should write a book and that can be the title!'
                               you think, 'As soon as I'm out of here,'

            To move pancake type one of these commands:
            'north' 'south' 'east' 'west' 'up' 'down' 'open'
            or to pick up items:
            'item name'
    """)
    move_me = input("> ")
    if "open" in move_me:
        tv_room()
    else:
        dead("Come on! Don't you want that book deal?")

#---------------------------------------------------------------------#
start_room()


#                                      # END #
