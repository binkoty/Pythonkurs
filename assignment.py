import numpy as np
from math import tan, pi, log, sqrt
import matplotlib.pyplot as plt
from scipy.sparse.csgraph import dijkstra, shortest_path
from matplotlib.collections import LineCollection
from scipy.sparse import csr_matrix
from scipy import spatial


def read_coordinate_file(filename):

                #read file with coordinates and convert form longitude/latitude to x/y
                #returns array as [[x1 y1][x2 y2]..]

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

def plot_points(coord_list, connections, path):

                #plot connections and shortest path on graph
                #coord_list = [[x1 y1][x2 y2]..]  connections = [[i1 j1][i2 j2]..]  path = [a1, a2, a3,..]
                #                               where i1 and i2 are connecting cities

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
    seg2 = []
    cun = 0
    for i in path:
        seg = coord_list[path[cun]]
        seg2.append(seg)
        # print (seg)
        cun = cun + 1

    segs2 = [seg2]

    #print connections
    #for l in range(0,len(segs)):
    #    print (segs[l])
    #behver fr varje unik siffra
    line_segments = LineCollection(segs, linewidths=(0.5, 1, 1.5, 2), linestyle='solid')
    line_segments2 = LineCollection(segs2, linewidths=(4, 2, 3, 4), linestyle='solid')
    ax = plt.axes()
    #print (segs)
    #print (segs2)
    #print (line_segments2)
    ax.add_collection(line_segments)
    ax.add_collection(line_segments2)

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


def construct_fast_graph_connections(coord_list, radius):

    results = []
    for i in coord_list:
        n = 0
        for result in tree.query_ball_point((coord_list[n]), radius):
            results.append(result)

            n = n + 1

    print (results)

def construct_graph(data, index, N):
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


def short_path(smatrix):

                #create predecessor array [x1, x2, x3,..]

    dist, pred = dijkstra(smatrix,return_predecessors=True)
    return pred

def compute_path(prem, strt, end):
    path = []
    i = end
    while i != strt:
        if i == end:
            path.append(i)
        i = prem[strt, i]
        path.append(i)

    return path

r = 0.08
strt = 0
end = 5

rfile = read_coordinate_file('SampleCoordinates.txt')

#dists, inds = construct_graph_connections(rfile, radius)

#smat = construct_graph(dists, inds, len(rfile))

#pred = short_path(smat)

#path = compute_path(pred, strt, end)

#plot_points(rfile, inds, path)

construct_fast_graph_connections(rfile, r)