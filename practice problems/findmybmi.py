'''
BMI
id bmi =18.5 or less under weight
18.5 to 24.5 healthy weight
24.5 and29.5 over weight
30 and above obesity
weight/height^2 height should be in meters convert from feet to cm to meters bmi
'''
while True:
    print("============================")
    print("enter height in centimeters")
    height=float(input())/100
    weight=float(input("enter your weight"))
    bmi=weight/pow(height,2)
    if bmi <=18.5:
        print("under weight")
    elif bmi>18.5 and bmi<=24.5:
        print("ideal weight")
    elif bmi>24.5 and bmi<30:
        print("over weight")
    else:
        print("obese")
    
