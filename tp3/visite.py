import numpy
import random
from random import randrange
import sys
import time
from math import ceil, log

ex_path = "./instances/PCT_20_50" #sys.argv[1]

# file data
n_sites = 0
adj_matrix = [] # row will be start point, while column will be endpoint
max_time = 0
popularity = []

# probabilistic
I_HOTEL = 0
POP_HOTEL = 0

# travel attributes
travel = [] # list, tuple index, popularity, time
cumul_time = 0
total_popularity = 0

# greedy
density_adj = []
avail_popularity = []

def extractData(file_name):
    global n_sites
    global max_time
    global popularity
    global adj_matrix
    
    # obtain every line as int list
    with open(file_name,'r') as ex:
        for line in ex:
            line = line.strip()
            if len(line) > 1:
               adj_matrix.append([int(a) for a in line.split()])
           
    # collect data
    n_sites = adj_matrix[0][0]
    max_time = adj_matrix[-2][0]
    popularity = adj_matrix[-1]
    
    # delete first, second to last and last rows
    adj_matrix.remove(adj_matrix[0])
    adj_matrix.remove(adj_matrix[-2])
    adj_matrix.remove(adj_matrix[-1])


# greedy with density
def calculateDensityAdj():
    global density_adj
    global adj_matrix
    
    density_adj = [[0.0 for x in range(n_sites)] for y in range(n_sites)]
    
    for i in range(n_sites):
        for j in range (n_sites):
            if (i != j | adj_matrix[i][j] != 0):
                density_adj[i][j] = popularity[j] / adj_matrix[i][j]
            else:
                density_adj[i][j] = 0 # prevent division by 0

# probabilist algorithm
def randomBeginTravel():
    global travel
    global cumul_time
    global avail_popularity
    
    # generate n_sites*0.35 random indexes for the beginning of the travel
    n_random_sites = int( (n_sites)*0.35 ) # *27/31)-5) )
    i_random_sites = random.sample(range(1, n_sites), n_random_sites)
    
    cumul_time = 0
    
    # choose random sites
    for i in range(1, n_random_sites):
        if (cumul_time <= max_time):
            i_previous_site = travel[i-1][0]
            new_time = adj_matrix[i_previous_site][i_random_sites[i]]
            
            # add the next random site.
            # index, popularity, travel time
            if (cumul_time + new_time <= max_time):
                travel.append((i_random_sites[i], popularity[i_random_sites[i]], new_time))
                cumul_time += new_time
            else: # max_time reached
                break
        else:
            break
    
    # copy popularity, and remove visited sites in the copy
    # visited is reversed, so we delete elements in decreasing order of index
    visited = sorted(i_random_sites, key=int, reverse=True)
    avail_popularity = []
    
    for i in range(len(popularity)):
        avail_popularity.append((i, popularity[i]))
    
    for i in range(len(visited)):
        j = visited[i]
        avail_popularity.remove(avail_popularity[j])

def calculate_cumul(trav):
    total = 0
    for i in range(len(trav)):
        total += trav[i][2]
    return total

def calculate_pop(trav):
    total = 0
    for i in range(len(trav)):
        total += trav[i][1]
    return total
    
# THE MAIN
extractData(ex_path);
start_time = time.time()
calculateDensityAdj();

# start probabilistic
travel.append((I_HOTEL, POP_HOTEL, adj_matrix[0][0])) # go to hotel
randomBeginTravel();

#print(avail_popularity)
#print(cumul_time)
#print(adj_matrix)
#print(density_adj)

#if(cumul_time <= max_time):

# END OF THE MAIN






def calculateDensityLine():
    d_line = [] # [0 for x in range(n_sites)]
    i_current_site = travel[-1][0]
    for i in range(n_sites):
        if (adj_matrix[i_current_site][i] != 0):
            d_line.append( (popularity[i]/adj_matrix[i_current_site][i], i) )
        else:
            d_line.append( (0, i) )
    return d_line
    
    
density_line = []

avail = len(avail_popularity)
for i in range(avail):
    if(calculate_cumul(travel) <= max_time):
        density_line = calculateDensityLine()
        
        i_current_site = travel[-1][0]
        max_density = density_line.index(max(density_line))
        i_max_density = density_line[max_density][1]
        
        new_time = adj_matrix[i_current_site][i_max_density]
        
        # add the next random site.
        # index, popularity, travel time
        if (cumul_time + new_time <= max_time):
            travel.append((i_max_density, popularity[i_max_density], new_time))
            cumul_time += new_time
            avail
        else: # max_time reached
            break
    else:
        break
        
        

# Determine if should continue
optimal = sum(popularity)
#print(optimal)

value = 0
for i in range(len(travel)):
    value += travel[i][1]
#print(cumul_time)
#print(value)
#print(travel)

# TODO: close travel. Temporary : go to hotel (wrong time from previous to hotel)
travel.append((I_HOTEL, POP_HOTEL, adj_matrix[0][0]))
#print(travel)

end_time = time.time()
runtime = end_time - start_time
#print(runtime);
