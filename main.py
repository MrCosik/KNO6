import pygad
import numpy

# S = [1, 2, 3, 6, 10, 17, 25, 29, 30, 41, 51, 60, 70, 79, 80]
items = [
    {'item': 'zegar',
     'value': 100,
     'weight': 7},
    {'item': 'obraz-pejzaz',
     'value': 300,
     'weight': 7},
    {'item': 'obraz-protret',
     'value': 200,
     'weight': 6},
    {'item': 'radio',
     'value': 40,
     'weight': 2},
    {'item': 'laptop',
     'value': 500,
     'weight': 5},
    {'item': 'lampka nocna',
     'value': 70,
     'weight': 6},
    {'item': 'srebrne sztucce',
     'value': 100,
     'weight': 1},
    {'item': 'porcelana',
     'value': 250,
     'weight': 3},
    {'item': 'figura z brazu',
     'value': 300,
     'weight': 10},
    {'item': 'skorzana torebka',
     'value': 280,
     'weight': 3},
    {'item': 'odkurzacz',
     'value': 300,
     'weight': 15},
]

num_items = 20
max_weight = 25

def knapsack_fitness(solution, solution_idx):
    total_value = 0
    total_weight = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            total_value += items[i]['value']
            total_weight += items[i]['weight']
    if total_weight > max_weight:
        return 0
    else:
        return total_value

gene_space = [0, 1]
num_parents_mating = 5
num_generations = 30
keep_parents = 2
sol_per_pop = 10
num_genes = len(items)
parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = 8


ga_instance = pygad.GA(
    num_generations=num_generations,
    gene_space=gene_space,
    num_parents_mating=num_parents_mating,
    fitness_func=knapsack_fitness,
    sol_per_pop=sol_per_pop,
    num_genes=num_genes,
    parent_selection_type=parent_selection_type,
    keep_parents=keep_parents,
    crossover_type=crossover_type,
    mutation_type=mutation_type,
    mutation_percent_genes=mutation_percent_genes)
ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

result = []
result_value = 0

for idx, item in enumerate(items):
    if solution[idx] == 1:
        result.append(item['item'])
        result_value += item['value']


print("Predicted output based on the best solution : {result}".format(result=result))

ga_instance.plot_fitness()
