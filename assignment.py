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

def plot_points(coord_list, connections):
    from matplotlib.collections import LineCollection

    x = coord_list[:,0]
    y = coord_list[:,1]
    plt.scatter(x,y)
    #plt.show()

    segs = []
    cnt = 0
    for i in connections:

        seg = [coord_list[connections[cnt,0]], coord_list[connections[cnt,1]]]
        seg = [coord_list[connections[cnt][0]], coord_list[connections[cnt][1]]]
        cnt = cnt + 1
        #print coord_list
        #segs = segs + seg
        segs.append(seg)
    #print connections
    #for l in range(0,len(segs)):
        #print (segs[l])
#behver fr varje unik siffra
    line_segments = LineCollection(segs, linewidths=(0.5, 1, 1.5, 2), linestyle='solid')

    ax = plt.axes()
    ax.add_collection(line_segments)

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
                #print('check')

                if n != m:
                    ind = [n, m,]
                    diff = [diff]
                    indlist.append(ind)
                    difflist.append(diff)

            m = m + 1
        n = n + 1
    indlist = np.asarray(indlist)
    difflist = np.asarray(difflist)
    #print difflist, indlist
    return difflist, indlist


def construct_graph(data, index, N):
    from scipy.sparse import csr_matrix
    noll = np.zeros ((N, N))
    nmr = 0
    for line in data:
        #print line
        i = index[nmr,:]
        nmr = nmr + 1
        #print i
        #print line
        noll[i[0],i[1]] = line

    #print noll
    ny = csr_matrix(noll)
    #print ny
    return ny

#bor man importa i funktioner?

def short_path(smatrix):
    from scipy.sparse.csgraph import dijkstra, shortest_path

    #pred = shortest_path(smatrix,method='D',return_predecessors=True,indices=(i,j))

    dist, pred = dijkstra(smatrix,return_predecessors=True)
    return pred

#def compute_path(prem, strt, end):



rfile = read_coordinate_file('SampleCoordinates.txt')

#print( rfile[:,1] )
#print (rfile)
#plot_points(rfile)

radius = 0.08
#radius = 7
#print rfile

dists, inds = construct_graph_connections(rfile, radius)

#print (dists, inds)

#plot_points(rfile, inds)

smat = construct_graph(dists, inds, len(rfile))
#print smat
lol = short_path(smat)
print lol