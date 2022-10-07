
Max=0.0
Min=None


while True:
    sval=input("Enter Number: ")
    if sval=="done":
        break
    try:
        fval=float(sval)
    except:
        print("Invalid Input")
        continue
    if Min is None:
        Min=fval

    elif fval > Max :
        Max= fval

    elif fval < Min:
         Min= fval

print(Max,Min)











#try:
#    float(Numbers)
#except:
#    print("Invalid input")
