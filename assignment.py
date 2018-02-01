import numpy as np
from math import tan, pi, log
import matplotlib.pyplot as plt

def read_coordinate_file(filename):
    read = open(filename, 'r')
    cordin = []
    for line in read:
        line = line.strip('{} \t\n')
        lat, long = line.split(',')
        lat = float(lat)
        long = float(long)
        R = 1
        x = R * ((long*pi)/180)
        y = R * log(tan((pi/4)+(pi*lat)/360))
        cordin.append((x, y))

    cordin = np.asarray(cordin)
    #print(cordin)
    #print(type(cordin))
    return(cordin)
    read.close()
#uppgift1

def plot_points(coord_list):
    x = coord_list[:,0]
    y = coord_list[:,1]
    plt.scatter(x,y)
    plt.show()

#uppgift2

def construct_graph_connections(coord_list, radius):

    for x in coord_list:

        for row in coord_list:
            diff = x - row
            diff = diff[:,0]
            print (diff)


x = read_coordinate_file('SampleCoordinates.txt')
#print( x[:,1] )
#print (x)
#plot_points(x)
radius = 999
construct_graph_connections(x, radius)

