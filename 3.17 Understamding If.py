def question():
    role = input("what is your status? ")
    if(role == "root"):
        return print("Welcome mblo!!!")
    else: print("------------")
    age = input("How old are you? ")
    if(int(age) < 19):
        return print("You are not allowed")
    else: print("-------------")
    name = input('Whats your name? ')
    return print("Welcome, " + name)

question()