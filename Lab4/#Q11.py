#Q11

song = """Hiya, Barbie\n
Hi, Ken\n
You wanna go for a ride?\n
Sure, Ken\n
Jump in\n
\n
I'm a Barbie girl in the Barbie world\n
Life in plastic, it's fantastic\n
You can brush my hair, undress me everywhere\n
Imagination, life is your creation\n
Come on, Barbie, let's go party\n
I'm a Barbie girl in the Barbie world\n
Life in plastic, it's fantastic\n
You can brush my hair, undress me everywhere\n
Imagination, life is your creation\n
\n
I'm a blonde bimbo girl in a fantasy world\n
Dress me up, make it tight, I'm your dolly\n
You're my doll, rock and roll, feel the glamor in pink\n
Kiss me here, touch me there, hanky-panky\n
\n
You can touch, you can play\n
If you say I'm always yours, ooh woah\n
\n
I'm a Barbie girl in the Barbie world\n
Life in plastic, it's fantastic\n
You can brush my hair, undress me everywhere\n
Imagination, life is your creation\n
\n
Come on, Barbie, let's go party\n
Ah, ah, ah, yeah\n
Come on, Barbie, let's go party\n
Ooh woah, ooh woah\n
Come on, Barbie, let's go party\n
Ah, ah, ah, yeah\n
Come on, Barbie, let's go party\n
Ooh woah, ooh woah\n
\n
Make me walk, make me talk, do whatever you please\n
I can act like a star, I can beg on my knees\n
Come jump in, bimbo friend, let us do it again\n
Hit the town, fool around, let's go party\n
\n
You can touch, you can play\n
If you say I'm always yours\n
You can touch, you can play\n
If you say I'm always yours\n
\n
Come on, Barbie, let's go party\n
Ah, ah, ah, yeah\n
Come on, Barbie, let's go party\n
Ooh woah, ooh woah\n
Come on, Barbie, let's go party\n
Ah, ah, ah, yeah\n
Come on, Barbie, let's go party\n
Ooh woah, ooh woah\n
\n
I'm a Barbie girl in the Barbie world\n
Life in plastic, it's fantastic\n
You can brush my hair, undress me everywhere\n
Imagination, life is your creation\n
I'm a Barbie girl in the Barbie world\n
Life in plastic, it's fantastic\n
You can brush my hair, undress me everywhere\n
Imagination, life is your creation\n
\n
Come on, Barbie, let's go party\n
Ah, ah, ah, yeah\n
Come on, Barbie, let's go party\n
Ooh woah, ooh woah\n
Come on, Barbie, let's go party\n
Ah, ah, ah, yeah\n
Come on, Barbie, let's go party\n
Ooh woah, ooh woah\n
\n
Oh, I'm having so much fun\n
Oh, I love you Ken\n\n
Well, Barbie, we're just getting started\n"""

charCount = 0

for i in range(len(song)):
    if song[i] == "\\":
        charCount -= 1
    elif song[i] == " ":
        charCount += 0
    else:
        charCount += 1

print(f"Character count: {charCount}")