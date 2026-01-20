import math
import sys
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

def cross_product(v1, v2):
    x = v1.y * v2.z - v1.z * v2.y
    y = v1.z * v2.x - v1.x * v2.z
    z = v1.x * v2.y - v1.y * v2.x
    return Point(x, y, z)

def dot_product(v1, v2):
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

def magnitude(v):
    return math.sqrt(v.x**2 + v.y**2 + v.z**2)
def solve():
    coords = []
    try:
        lines_read = 0
        while lines_read < 4:
            line = sys.stdin.readline()
            if not line:
                break
            parts = line.strip().split()
            if len(parts) == 0:
                continue
            for p in parts:
                coords.append(float(p))
            if len(coords) >= (lines_read + 1) * 3:
                lines_read += 1                
    except ValueError:
        return
    if len(coords) < 12:
        return
    points = []
    for i in range(0, 12, 3):
        points.append(Point(coords[i], coords[i+1], coords[i+2]))
    A, B, C, D = points[0], points[1], points[2], points[3]
    vec_AB = B - A
    vec_BC = C - B
    vec_CD = D - C
    n1 = cross_product(vec_AB, vec_BC)
    n2 = cross_product(vec_BC, vec_CD) 
    dot = dot_product(n1, n2)
    mag_n1 = magnitude(n1)
    mag_n2 = magnitude(n2)
    if mag_n1 == 0 or mag_n2 == 0:
        print("0.00")
        return
    try:
        cos_phi = abs(dot) / (mag_n1 * mag_n2)
        if cos_phi > 1.0: cos_phi = 1.0
        if cos_phi < -1.0: cos_phi = -1.0
        
        angle_rad = math.acos(cos_phi)
        angle_deg = math.degrees(angle_rad)
        
        print(f"{angle_deg:.2f}")
    except ZeroDivisionError:
        print("0.00")

if __name__ == "__main__":
    solve()