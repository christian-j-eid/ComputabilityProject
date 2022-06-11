from Testing.TSP_reader import read
from Algorithms.TSP.Kruskal import Kruskal
from Algorithms.TSP.MinTSP_2Approx import MinTSP
from time import perf_counter as pc

file1 = '../Files/TSP_Instances/pr76.tsp'
opt1 = '../Files/TSP_Tours/pr76.opt.tour'

file2 = '../Files/TSP_Instances/ch150.tsp'
opt2 = '../Files/TSP_Tours/ch150.opt.tour'

file3 = '../Files/TSP_Instances/bayg29.tsp'
opt3 = '../Files/TSP_Tours/bayg29.opt.tour'

file4 = '../Files/TSP_Instances/att48.tsp'
opt4 = '../Files/TSP_Tours/att48.opt.tour'


def tsp_test(file, opt):
    g, opt = read(file, opt)
    time1 = pc()
    A = MinTSP(g)
    time2 = pc()
    print(time2-time1)


    # print(opt.tours)
    opt_tour_val = g.trace_tour(opt.tours)

    print('Optimal Tour: ', opt_tour_val[0])


def run_test(files, opt,names):
    for i in range(len(files)):
        print('Test for TSP instance ', names[i])
        tsp_test(files[i], opt[i])

names = ['pr76', 'ch150', 'bayg29', 'att48']
files = [file1, file2, file3, file4]
opt = [opt1, opt2, opt3, opt4]
run_test(files, opt, names)