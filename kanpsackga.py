from random import randint


class KnapsackProblemAG():
    def __init__(self,num_of_individ: int, num_of_items: int, weight_items: list, load_capacity):
        self.num_of_individ = num_of_individ
        self.num_of_items = num_of_items
        self.weight_items = weight_items
        self.load_capacity = load_capacity

    def gen_individuals(self):
        population = []
        for _ in range(self.num_of_individ):
            individual = [randint(0, 1) for _ in range(self.num_of_items)]
            population.append(individual)
        return population

    def gen_items(self):
        items = {i: w for i, w in enumerate(self.weight_items)}
        return items

    def calculate_individuals(self):
        population = self.gen_individuals()
        return population, [sum(individual) for individual in population]



test = KnapsackProblemAG(10, 5, [3,1,6,4,2], 50)
test_ind = test.gen_individuals()
test_items = test.gen_items()
test_calcu = test.calculate_individuals()
print(test_calcu)
