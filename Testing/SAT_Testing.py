from Algorithms.SAT.DPLL import start_DPLL
from Algorithms.SAT.GSAT import GSAT
from Algorithms.SAT.Max3SATApprox import Approx

from Testing.SAT_Reader import read_instances
from time import perf_counter as pc
from statistics import median
from copy import deepcopy


instances = read_instances()
approx_success = []
gsat_success = []
dpll_success = []

approx_time = []
gsat_time = []
dpll_time = []

for instance in instances:


    time1a = pc()
    approx = Approx(instance)
    time2a = pc()

    approx_success.append(approx.checkSuccess())
    approx_time.append(time2a-time1a)



    time1b = pc()
    gsat = GSAT(instance)
    time2b = pc()
    gsat_success.append(gsat.checkSuccess())
    gsat_time.append(time2b-time1b)

    time1c = pc()
    dpll = start_DPLL(instance)
    time2c = pc()
    dpll_time.append(time2c-time1c)
    if dpll != False:
        dpll_success.append(1)
    else:
        dpll_success.append(0)




def print_info(str, success, time):
    print(str, ' info: ')
    print('Success')
    print('Max: ', max(success))
    print('Min: ', min(success))
    average(deepcopy(success))
    med(deepcopy(success))

    print('Time')
    average(deepcopy(time))
    med(deepcopy(time))
    print('Max: ', max(time))
    print('Min: ', min(time))

def print_info_dpll(str, success, time):
    print(str, ' info: ')
    print('Success')
    print('Max: ', max(success))
    print('Min: ', min(success))
    print('Average: ', sum(success), '/', len(success))
    med(deepcopy(success))

    print('Time')
    average(deepcopy(time))
    med(deepcopy(time))
    print('Max: ', max(time))
    print('Min: ', min(time))

def average(l):
    print('Average: ',sum(l)/len(l))

def med(l):
    l.sort()
    print('Median: ',median(l))

print(approx_success)

print_info('Approx', approx_success, approx_time)

print_info('GSAT', gsat_success, gsat_time)
print_info_dpll('DPLL', dpll_success, dpll_time)