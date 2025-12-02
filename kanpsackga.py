from random import randint


class KnapsackProblemAG():
    def __init__(self,num_of_individ: int, num_of_items: int, weight_items: list, value_items: list, load_capacity):
        self.num_of_individ = num_of_individ
        self.num_of_items = num_of_items
        self.weight_items = weight_items
        self.value_items = value_items
        self.load_capacity = load_capacity

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

    def calculate_individuals(self):
        population = self.gen_individuals()
        items_w = self.gen_items_weight()
        items_v = self.gen_items_value()
        weight_individ = []
        value_individ = []
        for individual in population:
            weight = 0
            value = 0
            for index, gene in enumerate(individual):
                if gene == 1:
                    weight += items_w[index]
                    value += items_v[index]
            weight_individ.append(weight)
            value_individ.append(value)

        return weight_individ, value_individ


test = KnapsackProblemAG(10, 5, [3,1,6,4,2], [4,1,8,5,2], 50)
test_ind = test.gen_individuals()
test_items = test.gen_items_weight()
test_calcu = test.calculate_individuals()
print(test_calcu)
