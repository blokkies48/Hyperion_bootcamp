#Print used here for better orginization
print("Please enter all 3 times in minutes of each event")
#Float used because there can be . minutes as well
swimming = float(input("Swimming: "))
cycling = float(input("Cycling: "))
running = float(input("Running: "))

#Calculate total time
total_time = swimming + cycling + running
#Qualifying time set to variable so you can change it easily throughout the code if needed
qualifying_time = 100


#Checks done to find reward
if total_time <= qualifying_time:
    print("Provicial Colours")

elif total_time <= qualifying_time + 5 and total_time > qualifying_time:
    print("Provincial Half Colours")

elif total_time <= qualifying_time + 10 and total_time > qualifying_time:
    print("Provincial Scroll")
#No need for another check because all posible outcomes that don't meet the above criteria will result in no reward. 
else:
    print("No reward")