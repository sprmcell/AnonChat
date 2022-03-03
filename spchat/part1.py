answer_yes = ["A", "a"]
answer_no = ["B", "b"]

print("""
Welcome to SPCHAT chat to all your friends
Maybe make some new ones

USERNAME="anon"
PASSWORD="*********"

Login? (A/B)
""")

ans1 = input(">>")

if ans1 in answer_yes:
    print("\nMessage from: Mia <3\nHey anon, its me Mia, from math class, i hope this is anon hehe\n")

    ans2 = input("A = Hey Mia, yes its me anon, sorry for being so weird xD\nB = Sorry you have the wrong person LOL\n>>>")

    if ans2 in answer_yes:
        print("\nMessage from: Mia <3\nHehe i dont think you are weird, i find you funny, was wondering if you want to come to a party? X\n")

    elif ans2 in answer_no:
        print("\nOh, sorry\nMia <3 has blocked you")

    ans3 = input("A = I mean sure, whats the address, would like to see you again\nB = Damn sorry Mia i will be installing gentoo this weekend\n>>>")

    if ans3 in answer_yes:
        print("\nyay thx, the address is 29 ********* Street, cant wait to see you, i have to go to hockey practise, talk later anon\n### Mia has logged off")

    elif ans3 in answer_no:
        print("Oh damn, you nerd, ok then, bye i guess...\n### Mia has logged off")

    else:
        print("\nServer crashed or your hardened firefox broke the website, reload it")

elif ans1 in answer_no:
    print("\nDamn alright anon thx for being so funny and not taking the obvious answer\n")

else:
    print("\nBooted for api abuse, reload the page")
