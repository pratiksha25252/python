print("Welcome to the Custom Affirmations Generator!")

user_name = input("What's your name? ").strip()
current_day = input("What day of the week is it? ").strip().lower()
print("Now, tell me three of your favorite things.")
favorite_1 = input("Favorite thing 1: ").strip()
favorite_2 = input("Favorite thing 2: ").strip()
favorite_3 = input("Favorite thing 3: ").strip()

user_name = user_name.capitalize()

if current_day == "monday":
    affirmation = "Hey " + user_name + ", it�s Monday! Start your week with the magic of " + favorite_1 + ". You�ve got this!"
elif current_day == "tuesday":
    affirmation = "Hello " + user_name + ", happy Tuesday! Remember, like " + favorite_2 + ", you are vibrant and full of energy."
elif current_day == "wednesday":
    affirmation = user_name + ", it's Wednesday! Midweek is the perfect time to shine bright like " + favorite_3 + "!"
elif current_day == "thursday":
    affirmation = "Hi " + user_name + ", it�s Thursday! Keep moving forward, just like your love for " + favorite_1 + " keeps inspiring you."
elif current_day == "friday":
    affirmation = "Happy Friday, " + user_name + "! End the week on a high note with the joy of " + favorite_2 + " surrounding you."
elif current_day == "saturday":
    affirmation = "Hey " + user_name + ", it's Saturday! Relax and enjoy life�s little treasures, like " + favorite_3 + "."
elif current_day == "sunday":
    affirmation = user_name + ", it's Sunday! Recharge your spirit with the comfort of " + favorite_1 + " as you prepare for the week ahead."
else:
    affirmation = "Oops, " + user_name + ", I didn�t recognize the day '" + current_day + "'. Enjoy every moment with " + favorite_1 + "!"

print("\nYour custom affirmation for today:")
print(affirmation)

