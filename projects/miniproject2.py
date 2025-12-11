def GPA():
    grade1 = input('please type in your number grade : ') 
    print(grade1)

    if int(grade1) > 90 and int(grade1) < 101:
        print('congrats you have an A')
    else:
        print('you do not have an A')

GPA()

i = 1
while i < 18:
  print(i)
  i += 1