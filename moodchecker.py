mood = input("What's your mood today? ")

if mood.upper() == "HAPPY":
    print("It is great to see you happy!")
elif mood.upper() == "NERVOUS":
    print("Take a deep breath 3 times.")
elif mood.upper() == "SAD":
    print("Everything will be better tomorrow!")
elif mood.upper() == "EXCITED":
    print("What are you so excited about?")
elif mood.upper() == "RELAXED":
    print("Wow, the perfect mood for the weekend!")
else:
    print("I don't recognize this mood. I'm sorry!")