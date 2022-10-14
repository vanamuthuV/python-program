# Quadratic equations using function.

from cmath import sqrt
from math import fabs

def forequal(b,a):
      r1=r2=(-b)/(2*a)
      print("roots are real and equal")
      print("r1= ",r1)
      print("r2= ",r2)
def forunequal(b,a,d):
      r1=((-b)+(d))/(2*a)
      r2=((-b)-(d))/(2*a)
      print("roots are real and distinct")
      print("r1= ",r1)
      print("r2= ",r2)
def complexnum(b,a,d):
      rp=(-b)/(2*a)
      ip=(d)/(2*a)
      print("roots are real and imaginary")
      print('r1 ={0}+i{1}'.format(rp,ip))
      print('r2 ={0}-i{1}'.format(rp,ip))

a=float(input("enter the value of the variable a : "))
b=float(input("enter the value of the variable b : "))
c=float(input("enter the value of the variable c : "))
if a==0:
      print("roots can't be determined")

else:
      disc=(b*b)-(4*a*c)
      d=sqrt(fabs(disc))
      if disc==0:
            forequal(b,a)
      elif disc>0:
            forunequal(b,a,d)
      else :
            complexnum(b,a,d)

'''

OUTPUT-1 :

enter the value of the variable a : 1
enter the value of the variable b : -1
enter the value of the variable c : 1
roots are real and imaginary
r1 =0.5+i(0.8660254037844386+0j)
r2 =0.5-i(0.8660254037844386+0j)

OUTPUT-2 :

enter the value of the variable a : 1
enter the value of the variable b : 5
enter the value of the variable c : 6
roots are real and distinct
r1=  (-2+0j)
r2=  (-3+0j)

'''