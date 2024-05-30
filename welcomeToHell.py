menuHandout = "Flagellation\nSpanking\nSodomy"

print("Hello, welcome to Hell")
name = input("What is your name?\n")

if name == "Ben" or name == "Alex" or name == "Mikey" or name == "Michael":
    evil_status = input("Are you evil?\n")
    good_deeds = int(input("How many good deeds have you done today?\n"))
    if evil_status == "Yes" or evil_status == "yes" and good_deeds > int(4):
        print("You have redeemed yourself!  Come right on in")
    else:
        print("You had better get right the fuck out of here Evil " + name + "!\n")
        exit()
else:
    print("Hello " + name + ", thank you for coming in today\n")

beard_length = int(
    input("We have a special running today for individuals that have a beard longer than 1 inch.  "
          "How long is your beard?\n"))

if beard_length < 1:
    print("Oooh sorry not only do you not qualify for the promotion but you're also going to have to get the fuck out "
          "of here")
    exit()
else:
    print("Fantastic, get the fuck in here you beautiful, bearded fuck! That was actually just a trick to make sure "
          "we keep the right types of people in here.  You get no special treatment whatsoever.\n")

order = input("How may I punish you today?  Here is what we're serving\n\n\n" + menuHandout + "\n")


def calculation():
    return price * float(orderquantity)


if order == "Flagellation" or order == "Spanking" or order == "Sodomy":
    print("Ooooooh fine choice. How many " + order + " would you like?")
    price = 9.0
    orderquantity = float(input())
    try:
        ordertotal = calculation()
    except:
        ordertotal = price * 8
        print("Look, I can see you just want to be difficult so I'm just going to charge you for 8 " + order + "s.")
    print("The total for your order will be " + str(ordertotal))
else:
    price = 69.0
    print("Sounds good but you're straight up getting charged more money because you're picking a non-menu item and "
          "that is just not cool. How many " + order + " would you like?\n")
    orderquantity = float(input())
    try:
        ordertotal = calculation()
    except:
        ordertotal = price * 8
        print("Look, I can see you just want to be difficult so I'm just going to charge you for 8 " + order + "s.")

    print("The total for your order will be " + str(ordertotal))

paymentmethod = input("Would you like to pay by cash or card?\n")

if paymentmethod == "card":
    print("So sorry but your " + paymentmethod + " was declined.  Fortunately for you, we are highly motivated to "
                                                 "provide your " + order + " and today it's going to be on the house.\nPlease drop your pants and await further "
                                                                           "instruction")
elif paymentmethod == "cash":
    print("Right on but I'm not giving you any change so pony up, scum.  Please drop your pants and await further "
          "instruction")

else:
    print("That's not an accepted form of currency but I'll tell you what... I was really looking to give some "
          + order + " today anyway so it's on the house.  Please drop your pants and await further instruction.\n.\n.")
print("GWAHAHAHHA YES RECEIVE THINE " + order + "s, FILTH!")
while True:
    line = input("ARE YOU QUITE FINISHED, FILTH OR SHALL I CONTINUE DELIVERING " + order + "s forth hence?\n")
    if line == "Please sir, stop! I beg you!":
        break
    print("Are you quite done or shall you have more " + order + "s?")
print('Your soul has been relinquished.')
