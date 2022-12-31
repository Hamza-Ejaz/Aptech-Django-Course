user_call = int(input("enter a month's number: "))

month = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}

if user_call>0 and user_call<13 :
    print(month[user_call])
else:
    print("you have entered a wrong command...")