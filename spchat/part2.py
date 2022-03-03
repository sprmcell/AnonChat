ansa = ["A", "a"]
ansb = ["B", "b"]

print("""
Welcome back to SPCHAT, this website got a bit popular
Help me keep the website up at https://discord.gg/CYxzJvK8Cc

Login:
USERNAME="anon"
PASSWORD="**********"

""")

ans1 = input("$ Login? (A/B)")

if ans1 in ansa:
    print("$ Mia <3: Heyy anon, in English you looked really tired, everything okay?")

    ans2 = input("\nA = Yea lol, thx for asking, how are you\nB = im not sure, i feel empty and lonely, i dont fit in anywhere\n$")

    if ans2 in ansa:
        print("Glad you're doing well anon, im always here if you need me")
    if ans2 in ansb:
        print("Sorry you feel that way anon, if it means anything i care about you, talk to me please!!")

    ans3 = input("\nA = screw feelings, ask about the PARTYY\nB = Open up to her\n$")

    if ans3 in ansa:
        print("Hm alright anon, well i already told you the address, it starts after school on friday, and until the host chases us away im tired, night\n### Mia has logged off")

    if ans3 in ansb:
    # lol i would just vent out my feelings but thats kinda gay, maybe i will put it in a hidden file somewhere, idk, i like to drop suttle hints to my suicidal thoughts
        print("Wow anon, Im so sorry you are going through this, i really hope you get the needed help, i feel so bad for you, if i see you at school imma hug you <3\n### Mia has logged off")

    ans4 =  input("\nA = i think i have feelings for you\nB = i really like you, you are so kind to me \n$")

    if ans4 in ansa:
        print("\ni just want you to love me\nERROR: cant send messages to offline users")
    if ans4 in ansb:
        print("\nWhy not me, i love you so much\nERROR: cant send messages to offline users")

    else:
        print("\nWebsite api error, please reload the website")


