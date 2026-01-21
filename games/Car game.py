command= ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("car started")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("car stopped ")
    elif command == "help":
        print(""" 
start_ to start the car
stop_ to stop the car
help_ to see the menu 
quit_ to quit
""")
    elif command== "quit":
        break
    else:
        print("Sorry, i do not understand that")
