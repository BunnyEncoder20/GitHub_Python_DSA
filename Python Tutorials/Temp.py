import math
def cost_of_trip (flightCost, hotelCost, weeklyCarCost, duration) :
    '''
        Function to calc cost of a trip 
        flightCost = return Flight cost ($) 
        HotelCost = Hotel per day ($)
        weeklyCarCost = Weekly Car Rental ($)
        duration = of trip in days
    '''

    try : 
        result = flightCost + (duration*hotelCost) + (math.ceil(duration/7)*weeklyCarCost)
    except ZeroDivisionError:
        print("Duration of the holiday must be at least 1 Day")
        result = 0
    
    return result;

Paris = ['Paris',100, 20, 200]
London = ['London',250, 30, 120]
Dubai = ['Dubai',370, 15, 80]
Mumbai = ['Mumbai',450, 10, 70]
destinations = [Paris, London, Dubai, Mumbai]
results = {}


# duration = 7 days cause 1 week trip
for destination in destinations : 
    costOfThisTrip = cost_of_trip(destination[1],destination[2],destination[3],duration=7)
    print(destination[0]+" will cost ₹{} for a week".format(costOfThisTrip))
    results[destination[0]]=costOfThisTrip

leastCost = 50000
leastCostKey = '' ;
for key in results : 
    if results[key]< leastCost: 
        leastCost = results[key]
        leastCostKey = key
print("The least cost destination would be :\n {} for {} ".format(leastCostKey,results[leastCostKey]))


# How the results change when the duration changes 
# durations = 4 days , 10 days, 2 weeks 



