from art import logo

print(logo)
continue_auc = True
biddersList = []
print("Welcome to the secret auction, first thing we need your name")
while continue_auc:
    name = input("please enter the name")
    bid = int(input("how much will you bid?"))
    biddersList.append({
        "name": name,
        "bid": bid
    })
    answer = input("do you wish to enter another name? yes/no").lower()
    if answer == 'no':
        continue_auc = False
maxBidder = biddersList[0]
for bidder in range(0, len(biddersList)):
    if biddersList[bidder]["bid"] > maxBidder["bid"]:
        maxBidder = biddersList[bidder]
print(f'the highest bid is {maxBidder["bid"]} by {maxBidder["name"]}')