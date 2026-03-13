#Task 3
import random

class GAEnvironment:
    def fitness(self, x):
        return x*x + 2*x

class GeneticAgent:
    def __init__(self, env, pop_size=6, generations=15, mutation_rate=0.1):
        self.env = env
        self.pop_size = pop_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.chromosome_length = 5

    def random_chromosome(self):
        return ''.join(random.choice('01') for _ in range(self.chromosome_length))

    def decode(self, chromosome):
        return int(chromosome, 2)

    def selection(self, population):
        population.sort(key=lambda c: self.env.fitness(self.decode(c)), reverse=True)
        return population[:2]

    def crossover(self, p1, p2):
        point = random.randint(1, self.chromosome_length-1)
        c1 = p1[:point] + p2[point:]
        c2 = p2[:point] + p1[point:]
        return c1, c2

    def mutate(self, chromosome):
        new = list(chromosome)
        for i in range(len(new)):
            if random.random() < self.mutation_rate:
                new[i] = '1' if new[i] == '0' else '0'
        return ''.join(new)

    def run(self):
        population = [self.random_chromosome() for _ in range(self.pop_size)]
        for gen in range(self.generations):
            best = max(population, key=lambda c: self.env.fitness(self.decode(c)))
            x = self.decode(best)
            fit = self.env.fitness(x)
            print(f"Generation {gen+1} Best: {best}  x={x}  fitness={fit}")
            parents = self.selection(population)
            new_population = parents.copy()
            while len(new_population) < self.pop_size:
                c1, c2 = self.crossover(parents[0], parents[1])
                c1 = self.mutate(c1)
                c2 = self.mutate(c2)
                new_population.extend([c1, c2])
            population = new_population[:self.pop_size]
        best = max(population, key=lambda c: self.env.fitness(self.decode(c)))
        x = self.decode(best)
        fit = self.env.fitness(x)
        print("\nFinal Result")
        print("Best Chromosome:", best)
        print("Best x:", x)
        print("Best Fitness:", fit)

env = GAEnvironment()
agent = GeneticAgent(env)
agent.run()
