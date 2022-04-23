def main():

    integerA = int(input("Enter integer a:"))
    integerB = int(input("Enter integer b:"))
    
    sum = 0
    for x in range(integerA,integerB+1):
        for y in str(x):
            sum = sum+int(y);
    
    print(sum)  
    
    
main()