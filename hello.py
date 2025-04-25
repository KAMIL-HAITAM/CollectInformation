# Collect information on the user
firstName = input("What's your first name? ").strip().lower().title()
lastName = input("What's your last name? ").strip().upper()
birthYear = int(input("What year were you born? (Number) "))
birthMonth = int(input("What month were you born? "))
birthDay = int(input("What day were you born? "))
birthDay = str(birthDay).zfill(2)
birthDate = f"{birthYear}-{birthMonth}-{birthDay}"
# Asks the user to input his email
email = input("What's your email? ").strip().lower()
# Asks the user to input his phone number
phone = input("What's your phone number? ").strip()
# Asks the user to input his address
address = input("What's your address? ").strip()
# Asks the user to input his city
city = input("What's your city? ").strip()
# Asks the user to input his state
state = input("What's your state? ").strip()
# Asks the user to input his country
country = input("What's your country? ").strip()
# Asks the user to input his postal code
postalCode = input("What's your postal code? ").strip()
# Asks the user to input his favorite color
color = input("What's your favorite color? ").strip().lower()
# Asks the user to input his favorite food
food = input("What's your favorite food? ").strip().lower()
# Asks the user to input his favorite movie
movie = input("What's your favorite movie? ").strip().lower()
# Asks the user to input his favorite music
music = input("What's your favorite music? ").strip().lower()
# Asks the user to input his favorite sport
sport = input("What's your favorite sport? ").strip().lower()
# Asks the user to input his favorite book
book = input("What's your favorite book? ").strip().lower()
# Asks the user to input his favorite animal
animal = input("What's your favorite animal? ").strip().lower()
# Asks the user to input his favorite hobby
hobby = input("What's your favorite hobby? ").strip().lower()
# Asks the user to input his favorite season
season = input("What's your favorite season? ").strip().lower()
# Asks the user to input his favorite holiday
holiday = input("What's your favorite holiday? ").strip().lower()
# Asks the user to input his favorite place
place = input("What's your favorite place? ").strip().lower()
# Asks the user to input his favorite time of day
timeOfDay = input("What's your favorite time of day? ").strip().lower()
# Asks the user to input his favorite quote
quote = input("What's your favorite quote? ").strip().lower()
# Asks the user to input his favorite song
song = input("What's your favorite song? ").strip().lower()
# Asks the user to input his favorite game
game = input("What's your favorite game? ").strip().lower()
# Asks the user to input his favorite website
website = input("What's your favorite website? ").strip().lower()
# Asks the user to input his favorite app
app = input("What's your favorite app? ").strip().lower()
# Asks the user to input his favorite social media
socialMedia = input("What's your favorite social media? ").strip().lower()
print("Thank you for your answers!")
# Print the information collected
print(f"First Name: {firstName}")
print(f"Last Name: {lastName}")
print(f"Birth Date: {birthDate}")
print(f"Email: {email}")
print(f"Phone: {phone}")
print(f"Address: {address}")
print(f"City: {city}")
print(f"State: {state}")
print(f"Country: {country}")
print(f"Postal Code: {postalCode}")
print(f"Favorite Color: {color}")
print(f"Favorite Food: {food}")
print(f"Favorite Movie: {movie}")
print(f"Favorite Music: {music}")
print(f"Favorite Sport: {sport}")
print(f"Favorite Book: {book}")
print(f"Favorite Animal: {animal}")
print(f"Favorite Hobby: {hobby}")
print(f"Favorite Season: {season}")
print(f"Favorite Holiday: {holiday}")
print(f"Favorite Place: {place}")
print(f"Favorite Time of Day: {timeOfDay}")
print(f"Favorite Quote: {quote}")
print(f"Favorite Song: {song}")
print(f"Favorite Game: {game}")
print(f"Favorite Website: {website}")
print(f"Favorite App: {app}")
print(f"Favorite Social Media: {socialMedia}")
# Save the information to a file
with open("favorites.txt", "w") as file:
    file.write(f"First Name: {firstName}\n")
    file.write(f"Last Name: {lastName}\n")
    file.write(f"Birth Date: {birthDate}\n")
    file.write(f"Email: {email}\n")
    file.write(f"Phone: {phone}\n")
    file.write(f"Address: {address}\n")
    file.write(f"City: {city}\n")
    file.write(f"State: {state}\n")
    file.write(f"Country: {country}\n")
    file.write(f"Postal Code: {postalCode}\n")
    file.write(f"Favorite Color: {color}\n")
    file.write(f"Favorite Food: {food}\n")
    file.write(f"Favorite Movie: {movie}\n")
    file.write(f"Favorite Music: {music}\n")
    file.write(f"Favorite Sport: {sport}\n")
    file.write(f"Favorite Book: {book}\n")
    file.write(f"Favorite Animal: {animal}\n")
    file.write(f"Favorite Hobby: {hobby}\n")
    file.write(f"Favorite Season: {season}\n")
    file.write(f"Favorite Holiday: {holiday}\n")
    file.write(f"Favorite Place: {place}\n")
    file.write(f"Favorite Time of Day: {timeOfDay}\n")
    file.write(f"Favorite Quote: {quote}\n")
    file.write(f"Favorite Song: {song}\n")
    file.write(f"Favorite Game: {game}\n")
    file.write(f"Favorite Website: {website}\n")
    file.write(f"Favorite App: {app}\n")
    file.write(f"Favorite Social Media: {socialMedia}\n")
# Print a message to indicate that the information has been saved
print("Your information has been saved to favorites.txt.")
# Ask the user if they want to see their information
seeInfo = input("Do you want to see your information? (y/n) ").strip().lower()
if seeInfo == "y":
    with open("favorites.txt", "r") as file:
        print(file.read())
else:
    print("Goodbye!")
# Ask the user if they want to update their information
updateInfo = input("Do you want to update your information? (y/n) ").strip().lower()
if updateInfo == "y":
    # Ask the user for the new information
    firstName = input("What's your first name? ").strip().lower().title()
    lastName = input("What's your last name? ").strip().upper()
    birthYear = int(input("What year were you born? (Number) "))
    birthMonth = int(input("What month were you born? "))
    birthDay = int(input("What day were you born? "))
    birthDay = str(birthDay).zfill(2)
    birthDate = f"{birthYear}-{birthMonth}-{birthDay}"
    email = input("What's your email? ").strip().lower()
    phone = input("What's your phone number? ").strip()
    address = input("What's your address? ").strip()
    city = input("What's your city? ").strip()
    state = input("What's your state? ").strip()
    country = input("What's your country? ").strip()
    postalCode = input("What's your postal code? ").strip()
    color = input("What's your favorite color? ").strip().lower()
    food = input("What's your favorite food? ").strip().lower()
    movie = input("What's your favorite movie? ").strip().lower()
    music = input("What's your favorite music? ").strip().lower()
    sport = input("What's your favorite sport? ").strip().lower()
    book = input("What's your favorite book? ").strip().lower()
    animal = input("What's your favorite animal? ").strip().lower()
    hobby = input("What's your favorite hobby? ").strip().lower()
    season = input("What's your favorite season? ").strip().lower()
    holiday = input("What's your favorite holiday? ").strip().lower()
    place = input("What's your favorite place? ").strip().lower()
    timeOfDay = input("What's your favorite time of day? ").strip().lower()
    quote = input("What's your favorite quote? ").strip().lower()
    song = input("What's your favorite song? ").strip().lower()
    game = input("What's your favorite game? ").strip().lower()
    website = input("What's your favorite website? ").strip().lower()
    app = input("What's your favorite app? ").strip().lower()
    socialMedia = input("What's your favorite social media? ").strip().lower()
    # Save the updated information to a file
    with open("favorites.txt", "w") as file:
        file.write(f"First Name: {firstName}\n")
        file.write(f"Last Name: {lastName}\n")
        file.write(f"Birth Date: {birthDate}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Phone: {phone}\n")
        file.write(f"Address: {address}\n")
        file.write(f"City: {city}\n")
        file.write(f"State: {state}\n")
        file.write(f"Country: {country}\n")
        file.write(f"Postal Code: {postalCode}\n")
        file.write(f"Favorite Color: {color}\n")
        file.write(f"Favorite Food: {food}\n")
        file.write(f"Favorite Movie: {movie}\n")
        file.write(f"Favorite Music: {music}\n")
        file.write(f"Favorite Sport: {sport}\n")
        file.write(f"Favorite Book: {book}\n")
        file.write(f"Favorite Animal: {animal}\n")
        file.write(f"Favorite Hobby: {hobby}\n")
        file.write(f"Favorite Season: {season}\n")
        file.write(f"Favorite Holiday: {holiday}\n")
        file.write(f"Favorite Place: {place}\n")
        file.write(f"Favorite Time of Day: {timeOfDay}\n")
        file.write(f"Favorite Quote: {quote}\n")
        file.write(f"Favorite Song: {song}\n")
        file.write(f"Favorite Game: {game}\n")
        file.write(f"Favorite Website: {website}\n")
        file.write(f"Favorite App: {app}\n")
        file.write(f"Favorite Social Media: {socialMedia}\n")
    # Print a message to indicate that the information has been updated
    print("Your information has been updated.")
else:
    print("Goodbye!")
# Ask the user if they want to delete their information
deleteInfo = input("Do you want to delete your information? (y/n) ").strip().lower()
if deleteInfo == "y":
    # Delete the file
    import os
    os.remove("favorites.txt")
    # Print a message to indicate that the information has been deleted
    print("Your information has been deleted.")
else:
    print("Goodbye!")
# Ask the user if they want to exit
exitProgram = input("Do you want to exit the program? (y/n) ").strip().lower()
if exitProgram == "y":
    print("Goodbye!")
else:
    print("Goodbye!")
# Ask the user if they want to restart the program
restartProgram = input("Do you want to restart the program? (y/n) ").strip().lower()
if restartProgram == "y":
    # Restart the program
    import os
    os.execv(__file__, ['python'] + sys.argv)
else:
    print("Goodbye!")
# The End