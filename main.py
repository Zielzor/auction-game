import art

def add_to_dict(name,bid):
    auction_dict = {}    
    auction_dict["Name"] = name
    auction_dict["Bid"] = bid
    auction_list.append(auction_dict)
    

logo = art.logo
print(logo)

auction_list = []

auction_go = True
while auction_go == True:
    name = str(input("What is your name?\n:>"))
    bid = str(input("How high is your bid?\n:>"))
    add_to_dict(name,bid)
    go_on = str(input("Are there any other bidders? y/n \n:>"))
    go_on = go_on.lower()
    if go_on == "n":
        auction_go = False

bids_list = []
for i in range(0, len(auction_list)):
    bids_list.append(auction_list[i]["Bid"])

highest_bid = bids_list.index(max(bids_list))
highest_bid_holder = auction_list[highest_bid]["Name"]

print(f"The hoghest bid holder name is : {highest_bid_holder}")
