def hotelcost(nights):
    return 140*nights
def flightcost(city):
    if city =="mumbai":
        return 112
    if city =="japan":
        return 230
    if city=="pittsburg":
        return 400
def rentalcost(days):
    if days>=7:
        return 40*days-50
    elif days>=3:
        return 40*days-20
    else :
        return 40*days
    
def totalcost(days,city):
    spendingmoney=int(input("enter the total amount u have spent on food etc"))
    return rentalcost(days)+hotelcost(days)+flightcost(city)+spendingmoney
print(f"{rentalcost(8)} total cost of rental car")
print(f"{hotelcost(8)} total cost of hotel")
print(f"{flightcost("pittsburg")} total cost of flight")

print(rentalcost(8)+hotelcost(12)+flightcost("pittsburg"))