# -*- coding: utf-8 -*-
def p(text):
    rew = text.split("\n")
    for i in rew:
        newstr = '<p>'+i+"</p>"
        print newstr

p("""Major: Materials Science and Engineering
When not studying I like kickin it at the house and playing on the MIT basketball team
I have alot of favorite movies, basically most heist movies, James Bond, the Prestige, Batman, and most comedies with seth rogen or michael cera... or older will ferrel stuff... and lately steve carill's gotten alot funnier too.
Dream date= Emmanuelle Chriqui. Wish I could be on entourage
I want to be remembered for always having fun and getting the most out of life (this is a dumb question, you should live your life not worried about how other people will think of you)
In ten years, I'll be sitting on a California beach with my beautiful wife while serving as the head of an energy research lab at Sandia National Laboratories
Quote: "I don't know how to put this but I'm kind of a big deal." -Ron Burgundy/Will Tashman """)
