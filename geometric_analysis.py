import math
import matplotlib.pyplot as plt

def calculate_area(x1, y1, x2, y2, x3, y3, x4, y4):
    A1 = 0.5 * ((x1 * y2 + x2 * y3 + x3 * y4 + x4 * y1) - (x2 * y1 + x3 * y2 + x4 * y3 + x1 * y4))
    return A1

def calculate_z_c(A, f, s):
    z_c = math.sqrt((f ** 2) * (s ** 2) / A)
    return z_c

def calculate_angle(x1, y1, x2, y2, x3, y3, x4, y4):
    m1 = (y2 - y1) / (x2 - x1)
    m2 = (y3 - y2) / (x3 - x2)
    m3 = (y4 - y3) / (x4 - x3)
    m4 = (y1 - y4) / (x1 - x4)
    th_1 = math.degrees(math.atan((m2 - m1) / (1 + m1 * m2)))
    th_2 = math.degrees(math.atan((m3 - m2) / (1 + m2 * m3)))
    th_3 = math.degrees(math.atan((m4 - m3) / (1 + m3 * m4))
    th_4 = math.degrees(math.atan((m1 - m4) / (1 + m1 * m4))
    return [th_1, th_2, th_3, th_4]

def draw_lines(x1, y1, x2, y2, x3, y3, x4, y4):
    x = [x1, x2, x3, x4, x1]
    y = [y1, y2, y3, y4, y1]
    plt.plot(x, y)

def main():
    x0, y0, z0 = 0, 0, 0

    x1, y1, z1 = int(input("x1 = ")), int(input("y1 = ")), int(input("z1 = "))
    x2, y2, z2 = int(input("x2 = ")), int(input("y2 = ")), int(input("z2 = "))  # End effector
    x3, y3, z3 = int(input("x3 = ")), int(input("y3 = ")), int(input("z3 = "))  # New position of end effector

    OA = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2 + (z1 - z0) ** 2)
    AB = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    OC = math.sqrt((x3 - x0) ** 2 + (y3 - y0) ** 2 + (z3 - z0) ** 2)
    AC = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2 + (z3 - z1) ** 2)

    A1 = calculate_area(x1, y1, x2, y2, x3, y3, x4, y4)
    f_value = int(input("Focal length: "))
    s_value = int(input("Scale: "))
    z_c_value = calculate_z_c(A1, f_value, s_value)
    
    angles = calculate_angle(x1, y1, x2, y2, x3, y3, x4, y4)
    
    if OC > (OA + AB):
        print("Translate to O' so that O'C = OA + AB, then rotate so that B meets C")
    elif OC == (OA + AB):
        print("Rotate until B meets C")
    else:
        if AC > AB:
            print("Rotate OA inwards and then rotate AB until B meets C")
        elif AC == AB:
            print("Rotate AB until B meets C")
        else:
            print("Rotate OA outwards and then rotate AB until B meets C")

    draw_lines(x1, y1, x2, y2, x3, y3, x4, y4)
    plt.show()

if __name__ == "__main__":
    main()