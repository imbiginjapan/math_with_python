from matplotlib import pyplot as plt
from re import sub
import datetime
from time import strftime

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('Time')
    plt.xticks(range(0,25,3))
    plt.ylabel('Temperature')
    plt.title('Hourly Temperatures')
    
    
def get_data():
    temps = {}
    cities = []
    hours = []
    
    for h in range(0,24):
        print(h)
        time = (1,1,1,h,0,0,0,0,0)
        hours.append(sub('^0+',"",strftime('%I %p',time)))
        
    temps["Providence RI"] = [51,51,51,50,50,50,51,52,53,56,58,59,61,62,63,64,63,63,61,59,57,54,53,52]
    temps["Medford OR"] = [50,49,49,48,48,48,47,46,48,50,51,53,56,57,56,56,56,57,56,56,54,52,50,49]
    for k in temps:
        cities.append(k)
        draw_graph(hours,temps[k])
    plt.legend(cities)
    
if __name__ == '__main__':
        get_data()
        plt.show()
        

