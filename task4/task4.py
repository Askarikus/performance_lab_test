import math
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as input_file:
            input_list = [int(i) for i in input_file.readlines()]

            avg_val_of_list = sum(input_list) / len(input_list)
            list_of_func = (round, math.ceil, math.floor)
            avg_calc_different_func_list = [func(avg_val_of_list) for func in list_of_func]

            result = min(sum(abs(a - e) for e in input_list) for a in avg_calc_different_func_list)
            print(result)
