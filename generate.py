import numpy as np
import argparse
import sys


def generate(no_boxes, avg_number_boxes_width, avg_number_boxes_length, average_height=1, std_weight=8, std_length=4, std_height=3, width=1000, length=1000):
    mean_width = width / avg_number_boxes_width
    mean_length = length / avg_number_boxes_length

    widths = np.random.normal(mean_width, std_weight, size=no_boxes)
    lengths = np.random.normal(mean_length, std_length, size=no_boxes)
    heights = np.random.normal(average_height, std_height, size=no_boxes)

    widths = np.clip(widths, 0.0001, width)
    lengths = np.clip(lengths, 0.0001, length)
    heights = np.clip(heights, 0.01, max(heights))

    # sns.distplot(widths, hist=True, bins=avg_number_boxes_width)
    # plt.title("Distribution of widths")
    # plt.xlabel("width")
    # plt.show()
    #
    # sns.distplot(lengths, hist=True, bins=avg_number_boxes_length)
    # plt.title("Distribution of lengths")
    # plt.xlabel("length")
    # plt.show()
    #
    # sns.distplot(heights, hist=True, bins=(avg_number_boxes_width+avg_number_boxes_length)//2)
    # plt.title("Distribution of heights")
    # plt.xlabel("height")
    # plt.show()

    bin_ = [width, length, 0]
    boxes = np.stack((widths, lengths, heights), axis=1)

    return bin_, boxes


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generation parameters')
    parser.add_argument('--number_of_boxes', '-n', type=int, default=50, help='Number of boxes to be inserted')
    parser.add_argument('--avg_number_boxes_width', '-w', type=int, default=5, help='Average number of boxes that fit in width')
    parser.add_argument('--avg_number_boxes_length', '-l', type=int, default=5, help='Average number of boxes that fit by length')
    args = parser.parse_args()

    _, boxes = generate(args.number_of_boxes, args.avg_number_boxes_width, args.avg_number_boxes_length)
    for box in boxes:
        for i, edge in enumerate(box):
            if i < 2:
                sys.stdout.write(str(edge) + ",")
            else:
                sys.stdout.write(str(edge) + "\n")
