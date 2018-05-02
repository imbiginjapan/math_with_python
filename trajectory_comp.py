import math
from matplotlib import pyplot as plt

def draw_graph(x, y, u, deg):
    traj = plt.plot(x, y, label=str(u) + 'm/s @' + str(deg) + 'deg')
    plt.legend()
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')
    
def frange(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + increment
        
    return numbers
    
def draw_trajectory(u, theta):
    deg = theta
    theta = math.radians(theta)
    g = 9.8
    
    # Time of flight
    t_flight = 2*u*math.sin(theta)/g
    # Time intervals
    intervals = frange(0,t_flight,0.001)
    
    # List of x and y coordinates
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*(t**2))
    
    draw_graph(x,y,u,deg)

if __name__ == '__main__':
    
    try:
        n = int(input('Enter the number of trajectories: '))
    except ValueError:
        print('Invalid Input')
    
    i = 0
    while i < n:
        try:
            u = float(input('Enter the initial velocity (m/s): '))
            theta = float(input('Enter the angle of projection (degrees): '))
            draw_trajectory(u, theta)
            i += 1
        except ValueError:
            print('Invalid Input')
        
    plt.show()