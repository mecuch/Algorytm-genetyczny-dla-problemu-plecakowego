import random
from random import randint


class KnapsackProblemAG:
    def __init__(self,num_of_individ: int, num_of_items: int, weight_items: list, value_items: list, load_capacity):
        self.num_of_individ = num_of_individ
        self.num_of_items = num_of_items
        self.weight_items = weight_items
        self.value_items = value_items
        self.load_capacity = load_capacity
        self.population = self.gen_individuals()

    def gen_individuals(self):
        population = []
        for _ in range(self.num_of_individ):
            individual = [randint(0, 1) for _ in range(self.num_of_items)]
            population.append(individual)
        return population

    def gen_items_weight(self):
        items_w = {i: w for i, w in enumerate(self.weight_items)}
        return items_w

    def gen_items_value(self):
        items_v = {i: w for i, w in enumerate(self.value_items)}
        return items_v

    def fitness(self):
        items_w = self.gen_items_weight()
        items_v = self.gen_items_value()
        fitness_individ = []
        for individual in self.population:
            weight = 0
            value = 0
            for index, gene in enumerate(individual):
                if gene == 1:
                    weight += items_w[index]
                    value += items_v[index]

            if weight > self.load_capacity:
                fitness_individ.append(0)
            else:
                fitness_individ.append(value)

        return fitness_individ

    def roulette_wheel_selection(self):
        fitness = self.fitness()
        F = sum(fitness)
        r = random.randint(0, F-1)
        suma = 0
        for i in range(len(fitness)):
            suma += fitness[i]
            if suma >= r:
                return i, self.population[i]



test = KnapsackProblemAG(10, 5, [3,8,6,4,2], [4,1,8,5,2], 10)
test_calcu = test.fitness()
test_roulette = test.roulette_wheel_selection()
print(test_roulette)
