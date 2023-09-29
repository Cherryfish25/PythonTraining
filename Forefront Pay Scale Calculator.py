employeeName = input("Enter employee's name ")
skillLevel = input("Enter skill level ")
respLevel = input("Enter responsibility level ")
hourlyPay = 0
annualSalary = 0

skillList = [0, 0.50, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50, 5.00, 5.50, 6.00, 6.50, 7.00, 7.50]
respList = [0, 0.50, 1.00, 1.50, 2.00, 3.00, 4.00]

basePay = 15.5
skillPay = skillList[int(skillLevel)]
respPay = respList[int(respLevel)]

hourlyPay = (basePay + skillPay + respPay)
format_hourlyPay = "{:.2f}".format(hourlyPay)
annualSalary = 2080 * hourlyPay

print("Hourly pay = " + str(hourlyPay))
print("Annual pay = " + str(annualSalary))
