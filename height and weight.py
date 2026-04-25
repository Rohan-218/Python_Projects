total =0
for i in range(1,6):
    height,weight=map(int,input("Height and Weight of person "+str(i)+" :").split())
    if height>170 and weight<50:
        total+=1
print("Person passed =",total)