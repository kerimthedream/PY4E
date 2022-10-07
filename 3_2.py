Hrs=input('Enter Hours\n')
Rte=input('Enter Rate\n')
try:
    Hours=float(Hrs)
    Rate=float(Rte)
    Overtime= Hours-40
    OvertimeRate=1.5*Rate

    if Hours > 40:
        Pay=40*Rate+Overtime*OvertimeRate
    else:
        Pay=Hours*Rate

    print("Pay",Pay)

except:
    print("Error,please enter a numeric input")
