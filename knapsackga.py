import random
from random import randint


class KnapsackProblemAG:
    def __init__(self, num_of_individ: int, num_of_items: int,
                 weight_items: list, value_items: list, load_capacity: int, pc: float, pm: float, max_stagnation: int,
                 stop_numb: bool, stop_stag: bool):
        self.num_of_individ = num_of_individ
        self.num_of_items = num_of_items
        self.weight_items = weight_items
        self.value_items = value_items
        self.load_capacity = load_capacity
        self.pc = pc
        self.pm = pm
        self.max_stagnation = max_stagnation
        self.stop_numb = stop_numb
        self.stop_stag = stop_stag
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

        r = random.uniform(0.0, F)
        suma = 0
        for i in range(len(fitness)):
            suma += fitness[i]
            if suma >= r:
                return self.population[i]

    def pick_parents(self):
        parent1 = self.roulette_wheel_selection()
        parent2 = self.roulette_wheel_selection()
        while parent2 == parent1 and len(self.population) > 1:
            parent2 = self.roulette_wheel_selection()
        return parent1, parent2

    def crossover(self):
        parent1, parent2 = self.pick_parents()
        u = random.random()  # float z [0,1)
        point = randint(1, self.num_of_items - 1)  # 1..n-1

        if u >= self.pc:
            child1 = parent1[:]
            child2 = parent2[:]
        else:
            child1 = parent1[:point] + parent2[point:]
            child2 = parent2[:point] + parent1[point:]

        return child1, child2

    def mutate_individual(self, individual):
        for i in range(len(individual)):
            u = random.uniform(0.0, 1.0)
            if u < self.pm:
                individual[i] = 1 - individual[i]
        return individual

    def next_generation(self):
        new_population = []

        while len(new_population) < self.num_of_individ:
            child1, child2 = self.crossover()

            child1 = self.mutate_individual(child1)
            child2 = self.mutate_individual(child2)

            new_population.append(child1)
            if len(new_population) < self.num_of_individ:
                new_population.append(child2)

        self.population = new_population
        return self.population

    def stop_by_numb(self):
        for _ in range(self.max_stagnation):
            self.population = self.next_generation()
        final_fitness = self.fitness()
        best_idx = final_fitness.index(max(final_fitness))
        return self.population[best_idx], max(final_fitness)

    def stop_by_stagnation(self):

        best_fitness_ever = 0
        stagnation = 0

        while stagnation < self.max_stagnation:

            fitness_list = self.fitness()
            current_best = max(fitness_list)

            if current_best > best_fitness_ever:
                best_fitness_ever = current_best
                stagnation = 0  # reset stagnacji
            else:
                stagnation += 1  # brak poprawy → +1

            self.next_generation()

        final_fitness = self.fitness()
        best_idx = final_fitness.index(max(final_fitness))
        return self.population[best_idx], max(final_fitness)

    def __str__(self):
        if self.stop_numb:
            best_ind, best_fit = self.stop_by_numb()
        elif self.stop_stag:
            best_ind, best_fit = self.stop_by_stagnation()
        else:
            return "Algorytm nie został uruchomiony (brak warunku stopu)."

        return (
            f"Najlepszy osobnik: {best_ind}\n"
            f"Jego fitness: {best_fit}"
        )


test = KnapsackProblemAG(
    num_of_items=6,
    num_of_individ=10,
    max_stagnation=50,
    weight_items=[3,5,1,8,9,4],
    value_items=[2,3,4,5,6,7],
    load_capacity=14,
    pc = 0.8,
    pm = 0.2,
    stop_numb=True,
    stop_stag=False
)
print(test)

