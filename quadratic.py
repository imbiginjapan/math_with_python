from matplotlib import pyplot as plt
from random import randint


def quad(x):
    return x ** 2 + 2*x + 1

def draw_graph(x):
    print (x)
    for n in x:
        plt.plot(n, quad(n), marker = 'o')

def get_vals(max):
    x  = []
    i = {}
    c = 0
    while c < max:
        n = randint(0 - max,max)
        if n not in i:
            c += 1
            x.append(n)
            i[n]= True
    return x
    

if __name__ == '__main__':
    max = int(input("# of values to plot: " ))
    x = sorted(get_vals(max))
    draw_graph(x)
    plt.show()
        

