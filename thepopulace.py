import random
import sys

import numpy as np
import matplotlib.pyplot as plt


def get_amount(from_n, to_n, step):
    """ Get amount. """

    return random.random()


def get_initial_value(n):
    """ Return initial value. """

    return random.random()


def initialize_population(population_size):
    """ Initialize the population. """

    population = []
    for n in xrange(population_size):
        population.append(get_initial_value(n))

    return population


def iterate_population(population, step, allow_negative=False):
    """ Iterate over the population. """

    population_size = len(population) - 1

    from_n = random.randint(0, population_size)
    to_n = random.randint(0, population_size)

    amount = get_amount(from_n, to_n, step)

    # Transfer amount from from_n to to_n
    if allow_negative or amount < population[from_n]:
        population[from_n] -= amount
        population[to_n] += amount


def calculate_histogram(population, bins=6):
    maximum = max(population)
    minimum = min(population)

    binsize = (maximum - minimum) / bins

    bin_counts = []
    bin_ranges = []
    for step in xrange(bins):
        bin_start = step * binsize
        bin_end = (step + 1) * binsize

        bin_count = 0

        for item in population:
            if item >= bin_start and item < bin_end:
                bin_count += 1

        bin_counts.append(bin_count)
        bin_ranges.append((bin_start, bin_end))

    return (bin_counts, bin_ranges)


def print_histogram(population):
    plt.figure()
    plt.hist(population, bins=100)
    plt.show()

    bin_counts, bin_ranges = np.histogram(population, bins=6)

    for n in xrange(len(bin_counts)):
        print 'bin: {} count: {} range: {}'.format(n, bin_counts[n], bin_ranges[n])


def run_model(population_size=600, steps=10000):
    population = initialize_population(population_size)

    for step in xrange(steps):
        iterate_population(population, step)

    print_histogram(population)


def main(argv=None):
    run_model()


if __name__ == "__main__":
    sys.exit(main())
