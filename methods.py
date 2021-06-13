import sys
import math
from timeit import default_timer as timer
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import algorithms
import generate


def solve(bin_, boxes):
    algorithms_dict = {}
    algorithms_dict["naive with sort"] = algorithms.naive_sort(bin_, boxes)
    algorithms_dict["naive without sort"] = algorithms.naive(bin_, boxes)
    if len(boxes) <= 5:
        algorithms_dict["systematic search"] = algorithms.systematic_search(bin_, boxes)
    algorithms_dict["search with layers"] = algorithms.layer_search(bin_, boxes)
    algorithms_dict["search with tree"] = algorithms.tree_search(bin_, boxes)

    for key, value in algorithms_dict.items():
        sys.stdout.write("The final height for " + key + " is " + str(value) + "\n")


def method_1():
    boxes = []
    for line in sys.stdin.readlines():
        edges = line.strip().split(',')
        edges = [float(edge) for edge in edges]
        boxes.append(edges)
    bin_ = [1000, 1000, 0]
    solve(bin_, boxes)


def method_2(args):
    n = args.number_of_boxes
    bin_, boxes = generate.generate(n, args.avg_number_boxes_width, args.avg_number_boxes_length)
    solve(bin_, boxes)


def method_3(args):
    median = args.number_of_problems // 2
    times_naive_sort = []
    times_naive = []
    times_sys_search = []
    times_layers = []
    times_tree = []
    theoretical_times_naive_sort = []
    theoretical_times_naive = []
    theoretical_times_sys_search = []
    theoretical_times_layers = []
    theoretical_times_tree = []

    for i in range(args.number_of_problems):
        n = args.number_of_boxes + i * args.step
        bin_, boxes = generate.generate(n, args.avg_number_boxes_width, args.avg_number_boxes_length)

        # print("Naive with sort:")
        start = timer()
        algorithms.naive_sort(bin_, boxes)
        end = timer()
        times_naive_sort.append((end - start) * 1000)
        theoretical_times_naive_sort.append(n * np.log(n) + n + 1)

        # print("Naive without sort:")
        start = timer()
        algorithms.naive(bin_, boxes)
        end = timer()
        times_naive.append((end - start) * 1000)
        theoretical_times_naive.append(n + 1)

        if n < 10:
            # print("Systematic search:")
            start = timer()
            algorithms.systematic_search(bin_, boxes)
            end = timer()
            times_sys_search.append((end - start) * 1000)
            theoretical_times_sys_search.append(math.factorial(n))

        # print("Search with layers:")
        start = timer()
        algorithms.layer_search(bin_, boxes)
        end = timer()
        times_layers.append((end - start) * 1000)
        theoretical_times_layers.append(n + n * np.log(n) + n ** 2 + 1)

        # print("Search with tree:")
        start = timer()
        algorithms.tree_search(bin_, boxes)
        end = timer()
        times_tree.append((end - start) * 1000)
        theoretical_times_tree.append(n + n * np.log(n) + n ** 2 + 1)

    # calculating q(n) for naive
    times = [times_naive_sort, times_naive, times_layers, times_tree]
    theoretical_times = [theoretical_times_naive_sort, theoretical_times_naive, theoretical_times_layers,
                         theoretical_times_tree]
    algorithms_names = ['Naive method with sorting', 'Naive method without sorting', 'Method with layers', 'Method with tree']

    for i in range(len(times)):
        t_median = times[i][median]
        theoretical_median = theoretical_times[i][median]
        q = []

        print(algorithms_names[i])
        for el in range(len(times[i])):
            q.append((times[i][el] * theoretical_median) / (theoretical_times[i][el] * t_median))

        for el in range(len(times[i])):
            print(args.number_of_boxes + el * args.step, times[i][el], q[el])
        print(" ")
