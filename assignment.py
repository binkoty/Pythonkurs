import numpy as np
from math import tan, pi, log, sqrt
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
    indlist = []
    difflist = []
    n = 0

    for line in coord_list:
        m = 0
        #print (line)

        for row in coord_list:
            diff = line - row
            diff = sqrt(diff[0]**2 + diff[1]**2)

            if diff < radius:
                print('alfred suger getpenis')

                if n != m:
                    ind = [n, m,]
                    diff = [diff]
                    indlist.append(ind)
                    difflist.append(diff)

            m = m + 1
        n = n + 1
    indlist = np.asarray(indlist)
    difflist = np.asarray(difflist)
    print indlist
    print difflist

x = read_coordinate_file('SampleCoordinates.txt')
#print( x[:,1] )
#print (x)
#plot_points(x)
radius = 0.07
construct_graph_connections(x, radius)

