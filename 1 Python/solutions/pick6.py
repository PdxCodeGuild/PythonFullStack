import random

# Generate a list of 6 random numbers representing the winning tickets
# Start your balance at 0
# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance    


def random_lottery_number(num):
    ''' generates lottery ticket based on six random numbers 1-99'''
    output = []
    for i in range(num):
        output.append(random.randint(1,99))
    return output


def calculate_payout(ticket, winning_ticket):
    ''' calculates the payout per ticket'''
    matches = 0
    for i in range(len(ticket)):
        if ticket[i] == winning_ticket[i]:
            matches += 1
    ticket_payout = {
        0:0,
        1:4,
        2:7,
        3:100,
        4:50000,
        5:1000000,
        6:25000000,
    }
    return ticket_payout[matches]     


winning_ticket = random_lottery_number(6)   
number_of_plays = 100000
tickets = []
for i in range(1,(number_of_plays +1)):
    tickets.append(random_lottery_number(6))

# for ticket in tickets:
# if get_rich(ticket,winning_ticket) > 0:
# print(ticket, winning_ticket, get_rich(ticket,winning_ticket))
earning = 0
for ticket in tickets:
    earning += calculate_payout(ticket, winning_ticket)

expenses = number_of_plays * 2
final_earnings = earning - expenses
roi = final_earnings / expenses
print(roi)

    