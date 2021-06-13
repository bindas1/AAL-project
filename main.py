import argparse
import methods


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Execution parameters')
    parser.add_argument('--mode', '-m', type=int, default=3, help='Execution mode')
    parser.add_argument('--number_of_boxes', '-n', type=int, default=50, help='Number of boxes to be inserted')
    parser.add_argument('--number_of_problems', '-k', type=int, default=1, help='Number of problems that should be executed')
    parser.add_argument('--step', '-step', type=int, default=50, help='How many boxes are added for the next problem')
    parser.add_argument('--samples', '-r', type=int, default=5, help='How many times do we simulate a problem')
    parser.add_argument('--avg_number_boxes_width', '-bw', type=int, default=5, help='Average number of boxes that fit in width')
    parser.add_argument('--avg_number_boxes_length', '-bl', type=int, default=5, help='Average number of boxes that fit by width')
    args = parser.parse_args()

    if args.mode == 1:
        methods.method_1()
    elif args.mode == 2:
        methods.method_2(args)
    else:
        methods.method_3(args)
