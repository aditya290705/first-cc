
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
sign = input("Enter operation(+, -, *, /): ")
o = sign.strip()

if o == "+":
  print(a,"+",b,"=",(a-b))
elif o == "-":
  print(a,"-",b,"=",(a-b))
elif o == "*":
  print(a,"*",b,"=",(a*b))
elif o == "/":
  print(a,"/",b,"=",(a/b))
else:
  print("Wrong Input!!")
