class C:
    def __init__(self, points):
        self.points = points

    def m(self, n):
        # Return True if at least n points are in the first quadrant, otherwise False
        count = 0
        for point in self.points:
            # Check if both x and y coordinates are greater than 0
            if point[0] > 0 and point[1] > 0:
                count += 1
        
        # Return True if the count of points in the first quadrant is >= n
        return count >= n

c = C([[2, 3], [1, 8], [-6, 4], [3, -7]])

print(c.m(2))  
print(c.m(3))