# program to create a graph

def get_max_values(nums):
    max_x=max_y=0
    for list_item in nums:
        if list_item[0]> max_x:
            max_x = list_item[0]
        if list_item[1]> max_y:
            max_y = list_item[1]
    return max_x, max_y

def format_points(nums):
    if (nums[0][0] != 0):
        nums.insert(0, (0,0))
    formatted_points = []
    for counter in range(len(nums)):
        formatted_points.append((nums[counter]))
        if counter < len(nums)-1:
            y = nums[counter][1]
            x = nums[counter][0]
            x_diff = nums[counter+1][0] - nums[counter][0] 
            y_diff = nums[counter+1][1] - nums[counter][1] 
            print(x_diff, y_diff)
            for i in range(x_diff-1):
                x += 1
                y = y + (y_diff/x_diff)
                formatted_points.append((x,int(y)))
    return formatted_points

def format_out_string(max_x, max_y, formatted_points):
    res = ""
    last_line = "-"*(max_x*3+5)
    while max_y >0:
        res = res + str(max_y).zfill(3) + "| "
        for i in range(1, max_x+1):
            if (i, max_y) in formatted_points:
                res += " # "
            else:
                res += " . "
        res += "\n"
        max_y -=1
    res = res +last_line +"\n  "
    for num in formatted_points:
        res = res +" "+ str(num[0]).zfill(2)
    return res
def main(nums):
    max_x, max_y = get_max_values(nums)
    formatted_points = format_points(nums)
    res = format_out_string(max_x, max_y, formatted_points)
    return res
    

if __name__=="__main__":
    # print(main([(2,2), (3,3), (5,5)]))
    # print(main([(2,3), (3,7), (5,13), (10,26)]))
    print(main([(2,3), (3,5), (5,8), (10, 26), (15, 18), (20,4)]))