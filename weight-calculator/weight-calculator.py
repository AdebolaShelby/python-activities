# to get a user input so we can calculate weight in kg or lbs

user_input_weight = input('Enter your weight: ')
user_input_lbs_kg = input('(L)bs or (K)g: ')

if user_input_lbs_kg == "kg":
    converted = float(user_input_weight) * 2.2
    print(f"Your weight in lbs is, {converted}")
elif user_input_lbs_kg == "lbs":
    converted_2 = float(user_input_weight) * 0.45
    print(f"Your weight in kg is, {converted_2}")
else:
    print("Invalid input")
