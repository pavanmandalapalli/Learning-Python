
print("====== CALCULATOR PROJECT ======") 
while True:
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modular\n6.Exit(Type Q)\n")
    num = input("Enter Your Choice : ")
    if num.lower() == 'q':
        print("Thamks for Using My Calsi")
        break
    else:
        print() 
        a,b = input("Enter Two Numbers : ").split()
        a ,b = int(a),int(b)
        cur_sum = 0
        if num ==  "1":
            cur_sum = a+b
            print("Sum = ",cur_sum)
        elif num == "2":
            cur_sum = a-b
            print("difference = ",cur_sum)
        elif num == "3":
            cur_sum = a*b
            print("mul =",cur_sum)
        elif num == "4":
            cur_sum = a/b
            print("div = ",cur_sum)
        elif num == "5":
            cur_sum = a%b
            print('mod = ',cur_sum)
        else:
            print("Invalid Input")
        res += cur_sum  
print("Your Final Sum = ",res)
    
    
# while True:
#     print(eval(input(">>>")))