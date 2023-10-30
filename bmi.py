def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height*height)
    print("BMI =" + str(bmi))
    if(bmi>25):
        classif= "Overweight, +1"
    if(bmi>=18.5):
        classif="Normal, 0"
    else:
        classif="Underweight, -1"
    print("Your BMI classification is " + classif)
calculate_bmi(weight=57, height=1.73)