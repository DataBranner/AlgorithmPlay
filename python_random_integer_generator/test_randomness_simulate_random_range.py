import simulate_random_range
import numpy
import random

def main(trials=100, given=5, desired=7):
    test_array = [0 for i in range(desired)]
    for i in range(trials):
        test_array[simulate_random_range.main(given, desired)-1] += 1
    test_ratio = numpy.std(test_array)/numpy.mean(test_array)
    print('Ratio of s.d. to mean in simulated randint():', test_ratio)
    control_array = [0 for i in range(desired)]
    for i in range(trials):
        control_array[random.randint(1, desired)-1] += 1
    control_ratio = numpy.std(control_array)/numpy.mean(control_array)
    print('Ratio of s.d. to mean in actual randint():   ', control_ratio)
    if test_ratio > control_ratio:
        relative_ratio = control_ratio/test_ratio
    else:
        relative_ratio = test_ratio/control_ratio
    print('Proportion of these ratios, smaller over larger:', relative_ratio)
