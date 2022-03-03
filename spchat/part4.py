ansa = ["A", "a"]
ansb = ["B", "b"]
from pyfiglet import figlet_format
import webbrowser
print(figlet_format("SPCHAT", font= "standard"))
print("""
The boards feature has been removed due to spam and illegal content
You are loved

Please login to continue

USERNAME: anon
PASSWORD: "**********"
""")

ans1 = input("\nLogin? A/B\n$ ")
if ans1 in ansa:
    print("Welcome back anon its been a while\n$ ")
if ans1 in ansb:
    webbrowser.open("https://www.youtube.com/watch?v=F-rfUwNxhdw")
ans2 = input("\nYou have 2 messages from Mia <3, would you like to read them? A/B")
if ans2 in ansa:
    print("""
    - Hey anon, i heard that you like me?? i told you i dont see you like that! now my boyfriend thinks im cheating
      whatever anon, this is your fault, you will never be able to date anyone, you are weird, ugly and boring
      all you do is sit in your room all day and use that stupid linux thing or whatever its called, change or nobody will want you
    
    - No anon, im not sorry, i dont like you, you were a decent friend until u told me u liked me, were u just nice to me because you thought
      that would give you a chance? you are so gross, dont talk to me ever again, irl and on any social medias, just leave me alone, please
      you make me feel uncomfortable, you will never be able to maintain a relationship, im done with you and all of your shit. BYE!!
   """)
if ans2 in ansb:
    print("$ hey anon, website admin here, she doesnt like you and for your mental health, dont read it.")

ans3 = input("\n$ logout or reply?\nA logut B reply\n$ ")
if ans3 in ansb:
    print("""
    Mia, i dont think you can possibly understand how much you meant to me, i woke up just to see your smile went to school to see you up close
    you made me happy, made me feel loved and cared for, im crying, i dont know how to live without, you and i were meant for eachother
    you messed with that retard jock, i was better, i am better, i hope you read this, you will never find someone like me, who respects you
    and treats you like the queen you are, i wont be coming back to school, he has came to take me, he has finally came, he made me do it
    he will take me, away, i need a self sacrifice, all for you, i love you, why did  u waste your time with that jock, goodbye forever
    """)

if ans3 in ansa:
    exit
