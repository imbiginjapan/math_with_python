import matplotlib.pyplot as mpl

def draw_graph(x, y):
    mpl.plot(x, y, marker = 'o')
    mpl.xlabel('Distance in meters')
    mpl.ylabel('Gravitational force in newtons')
    mpl.title('Gravitational force and distance')
    mpl.show()
    
    
def generate_F_r():
    # Generate values for r
    r = range(100,1001,50)
    F = []
    
    # constant, G
    G = 6.675 * (10**-11)
    
    # masses
    m1 = 0.5
    m2 = 1.5
    
    # Calculate force and add it to the list
    for dist in r:
        force = G * (m1*m2) / (dist**2)
        F.append(force)
        
    draw_graph(r,F)
    
if __name__ == '__main__':
    generate_F_r()