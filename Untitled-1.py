string = input("Enter binary string to compress ")
badnumbers = ["2","3","4","5","6","7","8","9"]
comp = 1
m = 0
if (string.isnumeric() == False or string in badnumbers):
    print("Invalid binary string, exiting...")
else:
    for n in string:
        print(string[m+1:m+2])
        