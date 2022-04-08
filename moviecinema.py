def welcome():
    #Welcome message
    print("Welcome to Michelle's Cinema! Nice to meet you.")
    #ask user for their information
    user_name= input("What is your name?")
    user_phone=''
    #validate the phone number
    while not user_phone.isnumeric():
        user_phone=input("Please enter a valid phone number:")
        if not user_phone.isnumeric():
            print("That is not a valid phone number.")
welcome()

print ("1 = The Batman")
print ("2 = Secrets of Dumbledore")
print ("3 = Doctor Strange")
def movies (movie):
    movie = movie.lower()
    match movie:
        case '1':
            return 'The Batman'
        case '2':
            return 'Secrets of Dumbledore'
        case '3':
            return 'Doctor Strange'
        case _:
            return 'Unnamed movie'
        
movie = input("Which movie would you like to watch today? ")
print (movies(movie))

while (movies(movie)) == 'Unnamed movie':
            if (movies(movie)) != 'Unnamed movie':
                print("information is correct")
                break
            else:
                print(" ")
                print("error, input is not accepted. please try again")
                print ("1 = The Batman")
                print ("2 = Secrets of Dumbledore")
                print ("3 = Doctor Strange")
                movie = input("Please choose a movie you'd like to view: ")
                print (movies(movie))
#choosing which theater different theatres have different times
def theater() :
    print("which screen do you want to watch movie: ")
    print("1,SCREEN 1")
    print("2,SCREEN 2")
    print("3,SCREEN 3")
    a = int(input("Please choose your screen: "))
    movie_ticket = int(input("How many tickets would you like to buy?: "))
    timing(a)

a = int(input("Please choose your time:"))

print ("1 = Morning")
print ("2 = Noon")
print ("3 = Evening")
def timing(a):
    time1 = {
        "1": "Morning 10:00-1:00",
        "2": "Noon 12:00 - 2:00"
    }
    time2 = {
        "1": "Morning 10:30-1:30",
        "2": "Evening 6:00-8:00"
    }
    time3 = {
         "1": "Evening 6:40-8:20",
        "2": "Noon 12:10 - 2:20"
    }
if a == 1:
    print ("Time:")
    print(time1)
    t = input ("Choose your time:")
    x = time1 [t]



available_seats = ['(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', '(8)', '(9)', '(10)',]
print (available_seats)
def seats(seat):
    seat = seat.lower()
    match seat:
        case '1':
                    return 0
        case '2':
                    return 1
        case '3':
                    return 2
        case '4':
                    return 3
        case '5':
                    return 4
        case '6':
                    return 5
        case '7':
                    return 6
        case '8':
                    return 7
        case '9':
                    return 8
        case '10':
                    return 9
        case _:
                    return 'Invalid seat'

seat = input("Which seat would you like? ")
if (seats(seat)) == 'Invalid seat':
    while (seats(seat)) == 'Invalid seat':
        seat = input("Which seat would you like? ")
        if (seats(seat)) != 'Invalid seat':
            available_seats[seats(seat)] = "(X)"
            break
        else:
            print(" ")
            print("error, input not accepted.")
            print(" ")
            print (available_seats)
            seat = input("Which seat would you like? ")
            print(" ")
            seat.append()

#confirm the booking
print('confirm order: movies:', (movies(movie)),  ", time:", (timing(a)), ", seats:", (available_seats),)
confirm = input("confirm the order? Y/N")

if confirm == "Y":
    print("You seat has been confirmed, please enjoy your movie!")
    if confirm == "N":
    break
elif confirm == "N":
    while confirm == "N":
        print()
        confirm = input ("Would you like to book again?")
        if confirm =="N":
            confirm == "Y"
            print ("Thank you for choosing Michelle's Cinema, please come again!")
            break
        elif confirm == "Y":
            break
        else:
            print ("Invalid")

    else: 
        print ("Invalid")
        confirm = input("Confirm order?")
