# get user input
string = input("Enter binary string to compress ")
# create list of numbers the string cannot be
badnumbers = ["2","3","4","5","6","7","8","9"]
# set variables
digitscompressed = 1
index = 0
# c is the empty string
c = ""
#first, check is the string is valid
if (string.isnumeric() == False or string in badnumbers):
    print("Invalid binary string, exiting...")
else:
    #create a for loop, iterating through the string
    for n in string:
        #if the loop finds a 1, it will check to see if the next number is one and add to the compression counter
        if string[index:index+1] == "1":
             if string[index+1:index+2] == "1":
                  digitscompressed += 1
                  index += 1
                #if the compression count is greater than 1, the compression will happen and is added to substring c
             elif digitscompressed > 1:
                 c = c + str(digitscompressed) + "1"
                 digitscompressed = 1
                 index += 1
                #if it is not, compression doesn't happen and the number is added to the substring c
             else: 
                 c = c + "1"
                 index += 1
                 
        else:
             #same as above
             if string[index+1:index+2] == "0":
                  digitscompressed += 1
                  index += 1
             elif digitscompressed > 1:
                 c = c + str(digitscompressed) + "0"
                 digitscompressed = 1
                 index += 1
             else: 
                 c = c + "0"
                 index += 1

print(f"Compressed Result: {c} (length = {len(c)})")
print(f"Original Data: {string} (length = {len(string)})")
print(f"The compression saved {(len(string) - len(c)) / len(string):.1f}% of the original data's length.")
                 
            
    
              
