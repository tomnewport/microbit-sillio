from microbit import *

order = [19,14,9,4,3,2,1,0,5,10,15,20,21,22,23]

vals = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

while vals[23] < 9:
    for a in order:
        vals[a] += 1
        display.show(Image("{}{}{}{}{}:{}{}{}{}{}:{}{}{}{}{}:{}{}{}{}{}:{}{}{}{}{}".format(*vals)))

while True:
    a = button_a.is_pressed()
    b = button_b.is_pressed()
    if a and b:
        display.show(Image(":".join([
            "99999",
            "99099",
            "90909",
            "99099",
            "99990"
        ])))
    elif a:
        display.show(Image(":".join([
            "99999",
            "99099",
            "90009",
            "99099",
            "99990"
        ])))
        sleep(500)
    elif b:
        display.show(Image(":".join([
            "99999",
            "90009",
            "90909",
            "90009",
            "99990"
        ])))
        sleep(500)
    else:
        display.show(Image(":".join([
            "99999",
            "90009",
            "90009",
            "90009",
            "99990"
        ])))
    sleep(100)
