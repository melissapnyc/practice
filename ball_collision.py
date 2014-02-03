# 3.2- Collision Dection of Balls

# ball# = [x, y, r]

# 2D
"""
def ball_collide(ball1, ball2):
    x1 = ball1[0]
    x2 = ball2[0]
    y1 = ball1[1]
    y2 = ball2[1]
    max = ball1[2] + ball2[2]
    z = (((x2-x1)**2)+((y2-y1)**2))**0.5
    if z >= max:
        return False
    else:
        return True

red = [0, 0, 1]
blue = [5, 5, 0]
yellow = [0, 3, 4]
green = [1, 1, 5]

print ball_collide(red, blue)
print ball_collide(yellow, green)
"""

# 3D

def ball_collide(ball1, ball2):
    x1 = ball1[0]
    x2 = ball2[0]
    y1 = ball1[1]
    y2 = ball2[1]
    max = ball1[2] + ball2[2]
    z = ((((x2-x1)**2)+((y2-y1)**2)) + (ball1[3] - ball2[3])**2)**0.5
    if z >= max:
        return False
    else:
        return True

red = [0, 0, 0, 1]
blue = [5, 5, 5, 2]
yellow = [0, 3, 1, 4]
green = [1, 1, 2, 5]

print ball_collide(red, blue)
print ball_collide(yellow, green)
