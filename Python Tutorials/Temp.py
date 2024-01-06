import math

def calc_EMI(amt, rate, time, downpayment=0) : 
    amt2pay = amt - downpayment
    emi = (amt2pay * rate * ((1+rate)**time)) / (((1+rate)**time)-1)
    return math.ceil(emi)

house_emi = calc_EMI(800000,.07/12,6*12,800000*.25)
car_emi = calc_EMI(60000,.12/12,1*12)

print("Total Monthly EMI payments = ",(house_emi+car_emi))
     