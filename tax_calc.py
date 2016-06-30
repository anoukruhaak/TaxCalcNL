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

def tax_freelance():
    print "Enter expected hourly rate:"
    my_rate = int(raw_input())
    print "Expected hours per week:"
    hours_week = int(raw_input())
    print "Expected weeks per year (norm is 45):"
    weeks = int(raw_input())
    annual_income = my_rate * weeks * hours_week
    print "annual income for %i week year, %ih week: %i" %(weeks, hours_week, annual_income)
    taxes_payable(annual_income)

def tax_annual():
    print "Enter your yearly income:"
    annual_income = int(raw_input())
    taxes_payable(annual_income)

print "Calculate annual income from hourly rate? (Yes | No)"
if raw_input() == "Yes":
    tax_freelance()
else:
    tax_annual()
