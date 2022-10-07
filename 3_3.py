Score=input("Enter score between 0 and 1\n")
try:
    Score=float(Score)
except:
    print("Bad Score")
    quit()

if Score > 1 or Score < 0:
    print("Bad Score")
    quit()
if Score >= 0.9 :
    print("A")
elif Score >= 0.8:
    print("B")
elif Score >=0.7:
    print("C")
elif Score >= 0.6:
    print("D")
elif Score < 0.6:
    print("F")
