def main():

    n = int(input("Enter Size of Array:"))
    arr = input("Enter The Array:").split(" ")
    
    tmp = 0
    res = 0
    for x in arr:
        res = res + int(x)
    
    if res % 2 == 0:
        print(res)
        
    else:
        for y in range(0,len(arr)):
            if(int(arr[y]) % 2 == 1 and (tmp ==0 or int(arr[y]) < tmp)):
                res += tmp
                res -= int(arr[y])
                tmp = int(arr[y])
    
        print(res)      
            
    
    
main()