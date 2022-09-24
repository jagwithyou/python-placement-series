#Write a Python program which accepts the radius of a circle from the user and compute the area
def calculate_area(radious):
    return 2*3.14*radious
    
if __name__=="__main__":
    area = calculate_area(2)
    print(area)