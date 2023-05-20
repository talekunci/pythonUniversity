a = input()
name = ""

if a == "Hello World":
    print("Hi!")
    print("What's your name?")
    name = input(name)
    print("Hello " + name + "!")
else:
    print("Be polite! First, you have to say greetings!")
    a = input()
    if a == "Hello World":
        print("Hi!")
    else:
        print("You are a pig!")
        exit(1)
