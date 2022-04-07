confirm = "N"
doot = "Y"
while confirm == "N":
    while doot == "Y":
        def welcomemessage():
            #Welcome message
            print("Welcome to Michelle's Cinema")

            #ask user for their info
            user_name= input("What is your name? ")
            user_phone= ''

            #validate their phone number
            
            while not user_phone.isnumeric():
                user_phone= input("Please enter a valid phone number? ")
                if not user_phone.isnumeric():
                    print("That is not a valid phone number.") 
        welcomemessage()  

        #movie selection
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
                print("error, input is not accepted.")
                print ("1 = The Batman")
                print ("2 = Secrets of Dumbledore")
                print ("3 = Doctor Strange")
                movie = input("Please choose a movie you'd like to view: ")
                print (movies(movie))

        #Picking the time of the movie

        print ("1 = Morning")
        print ("2 = Noon")
        print ("3 = Evening")
        def times (time):
            mtime = time.lower()
            match time:
                case '1':
                    return 'Morning'
                case '2':
                    return 'Noon'
                case '3':
                    return 'Evening'
                case _:
                    return 'Invalid time'
                                
        time = input("What time would you like to choose? ")
        print (times(time))

        while (times(time)) == 'Invalid time':
            if (times(time)) != 'Invalid time':
                print("info correct")
                break
            else:
                print(" ")
                print("error, input not accepted.")
                print ("1 = Morning")
                print ("2 = Noon")
                print ("3 = Evening")
                time = input("What Time? ")
                print (times(time))

        #booking the movie seat
        available_seats = ['(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', '(8)', '(9)', '(10)', ]
        print (available_seats)
        def seats (seat):
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
                    
        #seat validation            
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
                    
        available_seats[seats(seat)] = "(X)"
        print(available_seats)

        #confirming the booking
        print('confirm order: movies: ', (movies(movie)), ", time:", (times(time)), ", seats:", (available_seats), )
        confirm = input("confirm? Y/N ")
        
        if confirm == "Y":
            print("Your seat has been confirmed!")
            """ doot = input("book seat? Y/N ")
            if doot == "N":"""
            break
        elif confirm == "N":
            while confirm == 'N':
                print()
                doot = input("Would you like to book again? Y/N ")
                if doot == "N":
                    confirm == "Y"
                    print("Thank you for choosing Michelle's cinema")
                    break
                elif doot == "Y":
                    break
                else:
                    print("invalid input")
        else: 
            print("Invalid input")
            confirm = input("confirm? Y/N ")
