print("Arcade Day Pass Tracker - Challenge Steps")

customer_name = "Jacob"
number_of_passes = 50
tokens_per_pass = 2
price_per_pass = 5.00
currency = "USD"
tokens_required_per_game = 2

#Caculations
total_tokens = number_of_passes * tokens_per_pass
total_cost = number_of_passes * price_per_pass
games_playable = total_tokens // tokens_required_per_game

#Summary
print("Summary" + "\nArcade Day Pass Tracker - Receipt")
print("Customer Name: " + customer_name)
print("Number of Passes Purchased: " + str(number_of_passes))
print("Tokens per Pass: " + str(tokens_per_pass))
print("Total Tokens: " + str(total_tokens))
print("Total Cost: " + str(total_cost) + " " + currency)
print("Games Playable: " + str(games_playable))