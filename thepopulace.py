import random
import sys


def get_amount(from_n, to_n, step):
    """ Get amount. """

    return 0.5


def get_initial_value(n):
    """ Return initial value. """

    return 1.0


def initialize_population(population_size):
    """ Initialize the population. """

    population = []
    for n in xrange(population_size):
        population[n] = get_initial_value(n)

    return population


def iterate_population(population, step):
    """ Iterate over the population. """

    population_size = len(population) - 1

    from_n = random.randint(0, population_size)
    to_n = random.randint(0, population_size)

    amount = get_amount(from_n, to_n, step)

    # Transfer amount from from_n to to_n
    population[from_n] -= amount
    population[to_n] += amount


def run_model(population_size=100, steps=100):
    population = initialize_population(population_size)

    for step in xrange(steps):
        iterate_population(population, step)


def main(argv=None):
    run_model()


if __name__ == "__main__":
    sys.exit(main())
