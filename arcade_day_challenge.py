print("Arcade Day Pass Tracker - Challenge Steps")

customer_name = "Jacob"
number_of_passes = 5
tokens_per_pass = 30
price_per_pass = 12.50
currency = "USD"
tokens_required_per_game = 4

#Caculations
total_tokens = number_of_passes * tokens_per_pass
total_cost = number_of_passes * price_per_pass
games_playable = total_tokens // tokens_required_per_game

#Summary
print("============ Summary ==========" + "\n========Arcade Day Pass Tracker - Receipt=============")
print("Customer Name: " + customer_name)
print("Number of Passes Purchased: " + str(number_of_passes))
print("Tokens per Pass: " + str(tokens_per_pass))
print("Total Tokens:", total_tokens)
print(f"Total Cost: ${total_cost:.2f} {currency}")
print("Games Playable: " + str(games_playable))