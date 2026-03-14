name = input("What is your name? ")
fancy_name = name.capitalize() 

# 2. Get the distance and turn it into a number
distance_km = input("How far did you run today (in Kilometers)? ")
distance_km = float(distance_km)

# 3. Do the math (Distance divided by 1.609)
mile_unit = 1.60934
distance_in_miles = distance_km / mile_unit

# 4. Print the final message
# We use the 'distance_in_miles' variable so we show them the right answer!
print(f"Hi {fancy_name}! You ran {distance_in_miles:.2f} miles today! Great job! That's what {distance_km} kilometers gets you!")