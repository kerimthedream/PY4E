
num = 0
tot = 0.0

while True:
    sval=input("Enter Number: ")
    if sval=="done":
        break
    try:
        fval=float(sval)
    except:
        print("Invalid Input")
        continue
    num = num + 1
    tot = tot + fval

print(tot,num,tot/num)






#try:
#    float(Numbers)
#except:
#    print("Invalid input")
