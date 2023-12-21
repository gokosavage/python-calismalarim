temp = int(input("What is the tempeture outside?: "))

if not (temp >= 0 and temp <= 30):
    print("The tempeture is bad today!")
    print("Stay inside!")

elif not (temp < 0 or temp > 30):
    print("The tempeture is good today!")
    print("Go outside!")
