from Algorithms.Knapsack.Greedy2Approx import Greedy_2_Approximation as Greedy2
from Algorithms.Knapsack.nW_knapsack import nW
from Algorithms.Knapsack.mincost import minCost
from Algorithms.Knapsack.FTPAS import FTPAS
from Knapsack_Reader import read_instances
from time import perf_counter
from copy import deepcopy


def print_s():
    print('********************')


def run_test():
    instance_list = read_instances()
    greedy_info = [[],[]]
    nw_info = [[],[]]
    mincost_info = [[],[]]
    ftpas_info = [[],[]]
    F = 1.1
    for instance in instance_list:

        time1 = perf_counter()
        greedy_soln = Greedy2(deepcopy(instance))
        time2 = perf_counter()
        greedy_info[0].append(greedy_soln)
        greedy_info[1].append(time2-time1)

        time1 = perf_counter()
        nw_soln = nW(deepcopy(instance))
        time2 = perf_counter()
        nw_info[0].append(nw_soln)
        nw_info[1].append(time2-time1)
        #

        time1 = perf_counter()
        mincost_soln = minCost(deepcopy(instance))
        time2 = perf_counter()
        mincost_info[0].append(mincost_soln)
        mincost_info[1].append(time2-time1)

        time1 = perf_counter()
        ftpas_soln = FTPAS(deepcopy(instance), F)
        time2 = perf_counter()
        ftpas_info[0].append(ftpas_soln)
        ftpas_info[1].append(time2-time1)

    print(nw_info[0])
    print(mincost_info[0])
    print('nW')
    opt = print_info(average(nw_info))
    median(nw_info)
    minMaxTime(nw_info[1])
    print_s()

    print('MinCost')
    print_info(average(mincost_info))
    median(mincost_info)
    minMaxTime(mincost_info[1])
    print_s()

    print('FTPAS')
    val = print_info(average(ftpas_info))
    percent_opt(val, opt)
    median(ftpas_info)
    minMaxVal(ftpas_info[0], nw_info[0])
    minMaxTime(ftpas_info[1])
    print_s()


    print('GREEDY')
    val = print_info(average(greedy_info))
    percent_opt(val, opt)
    median(greedy_info)
    minMaxVal(greedy_info[0], nw_info[0])
    minMaxTime(greedy_info[1])
    print_s()


def average(info_list):
    avg_soln = 0
    avg_time = 0
    for i in range(len(info_list[0])):
        avg_soln += info_list[0][i]
        avg_time += info_list[1][i]

    return [avg_soln/len(info_list[0]), avg_time/len(info_list[0])]

def median(info_list):
    new_list_time = deepcopy(info_list[1])
    new_list_info = deepcopy(info_list[0])
    new_list_time.sort()
    new_list_info.sort()
    n = len(info_list[0])
    time_median = new_list_time[n//2]
    val_median = new_list_info[n//2]
    print('Median Val: ', val_median)
    print('Median Time: ', time_median)
    return val_median, time_median

def minMaxVal(info_list, opt_list):
    percent_opt = []
    for i in range(len(info_list)):
        percent_opt.append(info_list[i]/opt_list[i])
    max_val = max(percent_opt)
    min_val = min(percent_opt)
    print('Max val: ', max_val)
    print('Min val: ', min_val)

def minMaxTime(time_list):
    print('Max time: ', max(time_list))
    print('Min time: ', min(time_list))

def percent_opt(val, opt):
    print('Percent Optimal: ', val/opt)

def print_info(info):
    print('Average Max Val: ', info[0])
    print('Average Time: ', info[1])
    return info[0]

run_test()



