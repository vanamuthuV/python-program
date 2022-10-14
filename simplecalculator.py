#  SIMPLE CALCULATOR IN PYTHON.

a=float(input("Enter the value of a : "))
b=float(input("Enter the value of b : "))
print("Press\n\n+ for Addition.\n- for Subraction.\n* for Multiplication.\n/ for Division.\n% for remainder.\n\n")
choice=input("Enter the choice : ")

if(choice=='+'):
    {
      print(a+b)
    }
elif(choice=='-'):
    {
      print(a-b)
    }
elif(choice=='*'):
    {
      print(a*b)
    }
elif(choice=='/'):
   {
      print(a/b)
   }
elif(choice=='%'):
    {
      print(int(a)%int(b))
    }
else:
     {
      print("ERROR")
     }


'''
NOTE : Enter  python -m py_compile filename.py to compile the code.
       Enter  python filename.py to execute the program.

OUTPUT-1 :

Enter the value of a : 72.34
Enter the value of b : 27.66
Press

add for Addition.
sub for Subraction.
mul for Multi[lication.
div for Division.
remainder for Remainder


Enter the choice : add
100.0

OUTPUT-2 :

Enter the value of a : 23.3333
Enter the value of b : 10.
Press

add for Addition.
sub for Subraction.
mul for Multi[lication.
div for Division.
remainder for Remainder


Enter the choice : remainder
3

'''
