#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Version 3, removing error when last people has no option but self or previous.

import random
import smtplib
"""
mailList = {
    "Fredrik": "rallyengstrom@gmail.com",
    "Madeleine": "madde_svernedahl@hotmail.com",
    "Ante": "svernedal@hotmail.com",
    "Mats": "mats.svernedahl@telia.com",
    "Anne": "anne.svernedahl@telia.com",
    "Hanna-Maria": "hannamaria_swe@hotmail.com",
    "Hakan": "hakan.rolfjohan@outlook.com",
}

mailList = {
    "Fredrik": "julklappsdragning@gmail.com",
    "Madeleine": "julklappsdragning@gmail.com",
    "Ante": "julklappsdragning@gmail.com",
    "Mats": "julklappsdragning@gmail.com",
    "Anne": "julklappsdragning@gmail.com",
    "Hanna-Maria": "julklappsdragning@gmail.com",
    "Hakan": "julklappsdragning@gmail.com",
}
"""
draw = {
    "Madeleine": "Hanna-Maria",
    "Fredrik": "Madeleine",
    "Hanna-Maria": "Fredrik",
    "Ante": "Anne",
    "Anne": "Hakan",
    "Mats": "Ante",
    "Hakan": "Mats",
}


def christmasDraw(draw):
    """
    Randomly generate who is buying presents to who among individuals.
    It's not allowed to buy to self or the same person as last year.

    draw: dictionary where keys are people, and values who they bought to last year.
    Returns a new dictionary of who's buying to who.
    """
    picked = set()
    thisYear = {}
    for buyer, prev in draw.items():
        buySet = set(draw.values()) - {buyer, prev} - picked
        if len(buySet) == 0:
            return thisYear
        else:
            get = random.choice(list(buySet))
            thisYear[buyer] = get
            picked.add(get)
    return thisYear


keepGoing = True
print("christmasDraw initiated")
while keepGoing:
    newDraw = christmasDraw(draw)
    if len(newDraw) == len(draw):
        keepGoing = False
print("calculation complete")

for buyer, getter in newDraw.items():
    print("{}: {}".format(buyer, getter))
"""

print("Sending email to respective user:")
def send_email():
    email_address = 'julklappsdragning@gmail.com'
    email_password = 'jul2020!'

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(email_address, email_password)
        for buyer, getter in newDraw.items():
            sub = 'Din julklappsdragning 2022!'.format(buyer)
            msg = 'Hej {},\n\nDu ska handla julklapp till: {}!\n\nGod Jul och lycka till!'.format(buyer, getter)
            message = 'Subject: {}\n\n{}'.format(sub, msg)
            server.sendmail(email_address, mailList[buyer], message)
            print('Success: Email sent to {}!'.format(buyer))
        server.quit()
    except:
        print('Email failed to send.')


if __name__ == "__main__":
    send_email()
"""