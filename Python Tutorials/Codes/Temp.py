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


def finding_best_price(days) : 
    '''Function that takes in number of days and gives back which destination would cost the least for that number of days'''
    costs = []

    for destination in destinations : 
        costOfThisTrip = cost_of_trip(destination[1],destination[2],destination[3],duration=days)
        print(destination[0]+" will cost ₹{} for a week".format(costOfThisTrip))
        costs.append((destination[0],costOfThisTrip))

    return min(costs, key=lambda x: x[1])

# duration = 7 days cause 1 week trip
bestDeal = finding_best_price(7)
print("The least cost destination for {} would be :\n {} for {} ".format(7,bestDeal[0],bestDeal[1]))


# How the results change when the duration changes 
# durations = 4 days , 10 days, 2 weeks 
bestDeal = finding_best_price(4)
print("The least cost destination for {} would be :\n {} for {} ".format(4,bestDeal[0],bestDeal[1]))

bestDeal = finding_best_price(10)
print("The least cost destination for {} would be :\n {} for {} ".format(10,bestDeal[0],bestDeal[1]))

bestDeal = finding_best_price(14)
print("The least cost destination for {} would be :\n {} for {} ".format(14,bestDeal[0],bestDeal[1]))




        



    