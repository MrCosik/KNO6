import math
import random
import pygad
import pyswarms as ps
from matplotlib import pyplot as plt
from pyswarms.backend.topology import Star, Random, VonNeumann, Ring
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.functions.single_obj import sphere
from pyswarms.utils.plotters import plot_cost_history

import pyswarms.backend as P
from pyswarms.backend.swarms import Swarm

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

#
# gene_space = [0, 1]
# num_parents_mating = 5
# num_generations = 30
# keep_parents = 2
# sol_per_pop = 10
# num_genes = len(items)
# parent_selection_type = "sss"
# crossover_type = "single_point"
# mutation_type = "random"
# mutation_percent_genes = 8
#
# ga_instance = pygad.GA(
#     num_generations=num_generations,
#     gene_space=gene_space,
#     num_parents_mating=num_parents_mating,
#     fitness_func=knapsack_fitness,
#     sol_per_pop=sol_per_pop,
#     num_genes=num_genes,
#     parent_selection_type=parent_selection_type,
#     keep_parents=keep_parents,
#     crossover_type=crossover_type,
#     mutation_type=mutation_type,
#     mutation_percent_genes=mutation_percent_genes)
# ga_instance.run()
#
# solution, solution_fitness, solution_idx = ga_instance.best_solution()
# print("Parameters of the best solution : {solution}".format(solution=solution))
# print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
#
# result = []
# result_value = 0
#
# for idx, item in enumerate(items):
#     if solution[idx] == 1:
#         result.append(item['item'])
#         result_value += item['value']
#
# print("Predicted output based on the best solution : {result}".format(result=result))
#
# ga_instance.plot_fitness()
#
#
# # 2)
# # tutaj max to około 3.14
# def endurance(x, y, z, u, v, w):
#     return math.exp(-2 * (y - math.sin(x)) ** 2) + math.sin(z * u) + math.cos(v * w)
#
#
# def metal_fitness(solution, solution_idx):
#     return endurance(solution[0], solution[1], solution[2], solution[3], solution[4], solution[5])
#
#
# metal_names = ['x', 'y', 'z', 'u', 'v', 'w']
# metals = {}
#
# for i in metal_names:
#     metals[i] = round(random.uniform(0, 1), 2)
#
# gene_space2 = [{'low': 0, 'high': 1}, {'low': 0, 'high': 1}, {'low': 0, 'high': 1}, {'low': 0, 'high': 1},
#                {'low': 0, 'high': 1}, {'low': 0, 'high': 1}]
#
# ga_metals = pygad.GA(
#     fitness_func=metal_fitness,
#     num_generations=50,
#     num_parents_mating=5,
#     crossover_type="single_point",
#     mutation_type="random",
#     sol_per_pop=sol_per_pop,
#     num_genes=6,
#     gene_space=gene_space2,
# )
# ga_metals.run()
#
# solution, solution_fitness, solution_idx = ga_metals.best_solution()
# print("Parameters of the best solution : {solution}".format(solution=solution))
# print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
#
# ga_metals.plot_fitness()

# 4)




star_topology = Star() # The Topology Class
ring_topology = Ring(static=False) # The Topology Class
random_topology = Random(static=False) # The Topology Class

# Set-up hyperparameters
options = {'c1': 0.5, 'c2': 0.3, 'w':0.9, 'k': 2, 'p': 1}

# Call instance of GlobalBestPSO
def create_optimizer(topology):
    optimizer = ps.single.GeneralOptimizerPSO(n_particles=10, dimensions=2,
                                          options=options,
                                          topology=topology)
# Perform optimization
    stats = optimizer.optimize(fx.sphere, iters=100)
    return optimizer

# Obtain cost history from optimizer instance

star_optimizer = create_optimizer(star_topology)
ring_optimizer = create_optimizer(ring_topology)
random_optimizer = create_optimizer(random_topology)

star_history = star_optimizer.cost_history
ring_history = ring_optimizer.cost_history
random_history = random_optimizer.cost_history

# Plot!
plot_cost_history(star_history, title='Star plot')
plt.show()

plot_cost_history(ring_history, title='Ring plot')
plt.show()

plot_cost_history(random_history, title='Random plot')
plt.show()

print(f"Cost history of star topology is {star_history}")
print(f"Cost history of ring topology is {ring_history}")
print(f"Cost history of random topology is {random_history}")
