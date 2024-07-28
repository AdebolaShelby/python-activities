# car game with limit
user_count = 0
user_limit = 6
started = False
stopped = False


while user_count < user_limit:
    user_input = input("> ").lower()
    user_limit += 1

    if user_input == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    if user_input == "start":
        if started:
            print("car already started")
        else:
            started = True
            print("Car started, ready to go")
    elif user_input == "stop":
        if stopped:
            print("car already stopped")
        else:
            stopped = True
            print("Car Stopped")
    elif user_input == "quit":
        break
    else:
        print("I don't understand")



