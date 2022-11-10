largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        sval = int(num)
        if smallest is None or sval < smallest :
            smallest = sval
        if largest is None or sval > largest :
            largest = sval
    except:
        print('Invalid input')
        continue


print("Maximum is", largest)
print('Minimum is', smallest)
