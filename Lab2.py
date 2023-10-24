print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def display_main_menu():
    print("display_main_menu")
def calc_average(list):
    avg=sum(list)/len(list)
    print("Average temperature is:" + str(avg))
def calc_min_max(list):
    print("The minimum value is ")
    print(min(list))
    print("The maximum value is ")
    print(max(list))
print("Enter temp values separated by commas and press 'Enter'  e.g: 5,8,9,3")
tempstring=input()
tempstringList=tempstring.split(",")
print(tempstringList)
tempfloatlist=list(map(float,tempstringList))
print(str(tempfloatlist))
calc_average(tempfloatlist)
calc_min_max(tempfloatlist)