print("welcome to the road tax calculator")
bike_cost=int(input("what is the cost of your bike"))
if bike_cost>100000:
    tax_calculated=(bike_cost*15)/100
    total_cost_of_bike=bike_cost+tax_calculated
    print(f"your total cost of the bike is {total_cost_of_bike} ")
elif bike_cost>50000 and bike_cost<=100000:
     tax_calculated=(bike_cost*10)/100
     total_cost_of_bike=bike_cost+tax_calculated
     print(f"your total cost of the bike is {total_cost_of_bike} ")
elif bike_cost<=50000:
    tax_calculated = (bike_cost * 5) / 100
    total_cost_of_bike = bike_cost + tax_calculated
    print(f"your total cost of the bike is {total_cost_of_bike} ")