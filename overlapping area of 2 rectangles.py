# Although I have commented as much as I could, but still the logic used in this code maybe a bit confusing since there is no graphical presentation, so check out https://www.jasoncoelho.com/2021/10/finding-area-of-intersection-of-two.html if you got stuck. They have shown the similar logic in a graphical way.

'''
Given two rectangles on a 2D graph, return the area of their intersection.If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
and

{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
return 6.
'''

rectangle1 = {
    "top_left": (1, 4),
    "dimensions": (3, 2) # width, height
}

rectangle2 = {
    "top_left": (-4, 5),
    "dimensions": (9, 3) # width, height
}

# x values of width of rectangle 1, that is, left most x value and right most x value of rectangle 1
X_of_width1 = (rectangle1["top_left"][0], rectangle1["top_left"][0] + rectangle1["dimensions"][0])

# x values of width of rectangle 2, that is, left most x value and right most x value of rectangle 2
X_of_width2 = (rectangle2["top_left"][0], rectangle2["top_left"][0] + rectangle2["dimensions"][0])

# y values of height of rectangle 1, that is, top most y value and buttom most y value of rectangle 1
Y_of_height1 = (rectangle1["top_left"][1], rectangle1["top_left"][1] - rectangle1["dimensions"][1])

# y values of height of rectangle 2, that is, top most y value and buttom most y value of rectangle 2
Y_of_height2 = (rectangle2["top_left"][1], rectangle2["top_left"][1] - rectangle2["dimensions"][1])

def func(x1,x2, y1, y2):

    # Finds x and y values of overlapping area
    X_overlap = (max(x1[0], x2[0]), min(x1[1], x2[1]))
    Y_overlap = (min(y1[0], y2[0]), max(y1[1], y2[1]))


    # If the left most value of overlapping area is greater than the right most value, it contradicts with the fact that it is the left most value, this happens only when there is no actual overlap in x direction. Similiarly if the top most value of the overlapping area is lesser than buttom most value, then it woudln't be considered as the top most value, and again such a thing only happens when no overlap is present in y direction. So when any or both of these conditions are present, it means the overlapping area is 0.
    if (X_overlap[0] < X_overlap[1]) and (Y_overlap[0] > Y_overlap[1]):
        return abs((X_overlap[0] - X_overlap[1])) * abs((Y_overlap[0] - Y_overlap[1]))
    else:
        return 0

print(func(X_of_width1, X_of_width2, Y_of_height1, Y_of_height2))




