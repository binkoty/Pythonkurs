import numpy as np
from math import tan, pi, log, sqrt
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from scipy.sparse.csgraph import dijkstra, shortest_path
from matplotlib.collections import LineCollection
from scipy.sparse import csr_matrix
from scipy.spatial import cKDTree, KDTree

import time


time_base = time.time()
def read_coordinate_file(filename):

                #read file with coordinates and convert form longitude/latitude to x/y
                #returns array as [[x1 y1][x2 y2]..]

    read = open(filename, 'r')
    cordin = []
    for line in read:
        line = line.strip('{} \t\n\r')
        #print line
        lat, long = line.split(',')
        #print lat, long
        lat = float(lat)
        long = float(long)
        R = 1
        x = R * ((long*pi)/180)
        y = R * log(tan((pi/4)+(pi*lat)/360))
        cordin.append((x, y))

    cordin = np.asarray(cordin)
    #print(cordin)
    #print(type(cordin))
    global time_1
    time_1 = time.time() - time_base
    return(cordin)
    read.close()

def plot_points(coord_list, connections, path):

                #plot connections and shortest path on graph
                #coord_list = [[x1 y1][x2 y2]..]  connections = [[i1 j1][i2 j2]..]        path = [a1, a2, a3,..]
                #                                 where i1 and i2 are connecting cities

    x = coord_list[:,0]
    y = coord_list[:,1]
    plt.scatter(x,y)
    #plt.show()

                # create array for line-coordinates (all connections)
    segs = []
    cnt = 0
    for i in connections:

        seg = [coord_list[connections[cnt][0]], coord_list[connections[cnt][1]]]

        #print coord_list
        #segs = segs + seg
        segs.append(seg)
        cnt = cnt + 1

                #create array for line-coordinates (shortest path)
    #print 'ritat'

    seg2 = []
    cun = 0
    for i in path:
        seg = coord_list[path[cun]]
        seg2.append(seg)
        # print (seg)
        cun = cun + 1

    #print 'sp ritat'
    segs2 = [seg2]

    #print connections
    #for l in range(0,len(segs)):
    #    print (segs[l])
    #behver fr varje unik siffra
    line_segments = LineCollection(segs, linewidths=(0.5, 1, 1.5, 2),colors='grey', linestyle='solid')
    line_segments2 = LineCollection(segs2, linewidths=(1, 2, 3, 4),colors='blue', linestyle='solid')
    ax = plt.axes()
    #print (segs)
    #print (segs2)
    #print (line_segments2)
    ax.add_collection(line_segments)
    ax.add_collection(line_segments2)
    #print 'bara plt.show kvar'
    plt.show()


def construct_graph_connections(coord_list, radius):


    indlist = []
    difflist = []
    n = 0

    for n, line in enumerate(coord_list):
        #print (line)

        for m, row in enumerate(coord_list):
            diff = line - row
            diff = sqrt(diff[0]**2 + diff[1]**2)

            if diff < radius:
                #print('check')

                if n < m:
                    ind = [n, m,]
                    diff = [diff]
                    indlist.append(ind)
                    difflist.append(diff)

    indlist = np.asarray(indlist)
    difflist = np.asarray(difflist)
    #print difflist, indlist
    return difflist, indlist


def construct_fast_graph_connections(coord_list, radius):

    nbrsfinal = []
    co_tree = cKDTree(coord_list)

    for i in coord_list:
        n = 0
        nbrs = []
        for x in co_tree.query_ball_point((i), radius):

            nbrs.append(x)
            #print x
            n = n + 1

        nbrsfinal.append(nbrs)

    #print (nbrsfinal)

    dists = []
    inds = []

    cons = []

    cntr = 0
    for nbrs in nbrsfinal:
        for nbr in nbrs:
            cord = (coord_list[nbr])

            if cntr != nbr:
                inds.append([cntr, nbr])
                dists.append([sqrt(cord[0]**2 + cord[1]**2)])

        cntr = cntr + 1

    inds = np.asarray(inds)
    dists = np.asarray(dists)

    return dists, inds


def construct_graph(data, index, N):

    #print data
    #print index
    row = []
    col = []
    dat = []

    for i, n in enumerate(index):
        #print n[0]
        row.append(n[0])
        #print n[1]
        col.append(n[1])
        dat.append(data[i][0])

    col = np.asarray(col)
    row = np.asarray(row)
    dat = np.asarray(dat)

    #print (dat)
    #print (row)
    #print (col)

    ny = csr_matrix((dat, (row, col)), shape=(N, N))
    #print ny
    return ny


#def short_path(smatrix):
#
#                #create predecessor array
#    global dist
#    dist, pred = dijkstra(smatrix,return_predecessors=True)
#    return dist, pred

def compute_path(prem, strt, end):
    path = []
    disttot = []
    i = end
    while i != strt:
        if i == end:
            path.append(i)
            #disttot.append(dist[strt, i])

        i = prem[i]
        path.append(i)
        #disttot[0] += dist[strt, i]

    # print dist
    #print disttot
    #print disttot

    return disttot, path

strt = 1573
end = 10584

#strt = 0
#end = 5



#r = 0.08       #sample
#r = 0.005      #hungary
r = 0.0025      #germany

#rfile = read_coordinate_file('SampleCoordinates.txt')
#rfile = read_coordinate_file('HungaryCities.txt')
rfile = read_coordinate_file('GermanyCities.txt')

time_1 = time.time() - time_base
#print(1)

dists, inds = construct_fast_graph_connections(rfile, r)

#print(2)
#print dists,inds

#dists, inds = construct_graph_connections(rfile, r)
time_2 = time.time() - time_base - time_1

#print (dists)
#print (len(rfile))
#print len(dists)
#print len(inds)

smat = construct_graph(dists, inds, len(rfile))
#smat2 = construct_graph(dists2, inds2, len(rfile))
time_3 = time.time() - time_base - time_1 - time_2
#print smat
#print(3)


distmat, pred = dijkstra(smat, directed=False, indices=strt, return_predecessors=True)

#print (pred)
#print (distmat)

time_4 = time.time() - time_base - time_1 - time_2 - time_3
#print(4)

disttot, path = compute_path(pred, strt, end)
time_5 = time.time() - time_base - time_1 - time_2 - time_3 - time_4
#print(5)

plot_points(rfile, inds, path)
time_6 = time.time() - time_base - time_1 - time_2 - time_3 - time_4 - time_5
#print(6)
print ('tider for resp. uppgift')
print (time_1, time_2, time_3, time_4, time_5, time_6, time_base)
print ('Total tid:')
print (disttot)
#print(path)
print('klar')


