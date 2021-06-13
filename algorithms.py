import numpy as np
import itertools
import sys
from Node import Node


def naive_sort(bin_, boxes):
    # metoda naiwna z sortowaniem
    bin_copy = bin_.copy()
    # plot_naive_sort = [0]

    volumes = [l * w * h for l, w, h in boxes]
    sortedIndices = np.argsort(volumes).tolist()[::-1]

    # sort a by descending volumes
    boxes_sorted = [boxes[i] for i in sortedIndices]

    for box in boxes_sorted:
        bin_copy[2] += min(box)
        # plot_naive_sort.append(bin_copy[2])

    return bin_copy[2]


def naive(bin_, boxes):
    bin_copy = bin_.copy()
    a_copy = boxes.copy()
    # plot_naive = [0]

    for box in a_copy:
        bin_copy[2] += min(box)
        # plot_naive.append(bin_copy[2])

    return bin_copy[2]


def search(boxes, bin_copy):
    plot = [0]
    left_upper_corner = 0
    previous_max_length = 0
    max_length_in_row = 0
    current_height = 0
    max_height_in_basis = 0

    for box_ in boxes:
        flaga = True

        while flaga:
            if left_upper_corner + box_[0] < bin_copy[0]:
                if previous_max_length + box_[1] < bin_copy[1]:
                    if box_[2] > max_height_in_basis:
                        max_height_in_basis = box_[2]
                    if max_length_in_row < previous_max_length + box_[1]:
                        max_length_in_row = previous_max_length + box_[1]
                    left_upper_corner += box_[0]
                    flaga = False
                else:
                    left_upper_corner = 0
                    previous_max_length = 0
                    max_length_in_row = 0
                    current_height += max_height_in_basis
                    max_height_in_basis = 0
                plot.append(max_height_in_basis)
            else:
                previous_max_length = max_length_in_row
                left_upper_corner = 0

    current_height += max_height_in_basis

    return current_height, plot


def systematic_search(bin_, boxes):
    bin_copy = bin_.copy()
    a_copy = boxes.copy()

    # kolejnosc boxów
    permutations_of_a = list(itertools.permutations(a_copy))

    best_result = sys.maxsize

    for permut_a in permutations_of_a:
        boxes_perm = []
        for current_box in permut_a:
            boxes_perm.append(list(dict.fromkeys(itertools.permutations(current_box))))

        combinations = list(itertools.product(*boxes_perm))

        for combination in combinations:
            result = search(combination, bin_copy)
            if result[0] < best_result:
                best_result = result[0]
                # plot_sys_search = result[1]

    return best_result


def layer_search(bin_, boxes):
    bin_copy = bin_.copy()
    a_copy = boxes.copy()

    # obrócenie boxów tak, żeby ich wysokość była jak najmniejsza
    for box in a_copy:
        box[::-1].sort()

    # sortowanie nierosnąco po objętości
    a_copy = sorted(a_copy, key=lambda box: box[0] * box[1] * box[2], reverse=True)

    result = search(a_copy, bin_copy)
    best_result = result[0]
    # plot_layers = result[1]

    return best_result


def tree_search(bin_, boxes):
    bin_copy = bin_.copy()
    a_copy = boxes.copy()

    # obrócenie boxów tak, żeby ich wysokość była jak najmniejsza
    for box in a_copy:
        box[::-1].sort()

    # sortowanie nierosnąco po objętości
    a_copy = sorted(a_copy, key=lambda box: box[0] * box[1] * box[2], reverse=True)

    overall_height = 0
    curr_height = 0
    plot_tree = [0]

    root = Node(0, 0, bin_copy[0], bin_copy[1])

    for box in a_copy:
        new_insert = root.insert(box)
        if new_insert is None:
            # new tree
            root = Node(0, 0, bin_copy[0], bin_copy[1])
            overall_height += curr_height
            curr_height = 0
        else:
            if new_insert > curr_height:
                curr_height = new_insert
        # plot_tree.append(overall_height + curr_height)

    overall_height += curr_height

    return overall_height