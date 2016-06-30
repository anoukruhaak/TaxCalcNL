def taxes_payable(inc):
    low_box = 0.36
    mid_box = 0.42
    high_box = 0.52
    limit_low = 19645
    limit_high = 56531
    income = inc - 2000
    taxes = 0

    if income >= limit_high:
        taxes += (income - limit_high) * high_box + low_box * limit_low + mid_box * (limit_high - limit_low)
    elif income >= limit_low:
        taxes += (income - limit_low) * mid_box + low_box * limit_low
    elif income > 0:
        taxes += income * low_box
    else:
        taxes = 0
    print "Total taxes %i, income per month after taxes: %i" % (taxes, (inc - taxes)/12)


print "Enter hourly rate:"
my_rate = raw_input()
annual_income = int(my_rate) * 45 * 40
print "annual income for 45 week year, 40h week: %i" %(annual_income)

print "Enter your income:"
my_income = raw_input()
taxes_payable(int(my_income))