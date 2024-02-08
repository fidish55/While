# declare control variables
total=0
count=0
# ask the user to continuously input a number
while True:
    num = float(input("Please enter any number of your choice:"))
    
    #introduce the condition for -1 input
    if num == -1:
        break

    #increase the control variables in the loop
    total += num
    count += 1

#calculate the average
if count > 0:
    average = total/count
    print(f"the average of entered numbers (excluding -1) is: {average:.2f}")
else:
    print("No numbers entered (excluding -1) ")
