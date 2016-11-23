"""
Modulo para Algoritmo Genetico
"""
# -*- coding: utf-8 -*-

from random import randint, random
from operator import add

def individuo(tamanho, min, max):
    'Cria um membro da populacao.'
    return [randint(min,max) for x in xrange(tamanho)]

def population(n_individuos, tamanho, min, max):
    """
    Cria um numero de individuos

    count: numero de individuos na populacao
    length: numero de valores por individuos
    min: minimo possivel de individuos
    max: maximo possivel de individuos

    """
    return [individuo(tamanho, min, max) for x in xrange(n_individuos) ]

def fitness(individuo, objetivo):
    """
    Determina o fitness de um individuo. Quanto maior melhor.

    individuo: ---
    target: numero de individuos que se deseja obter
    """
    sum = reduce(add, individuo, 0)
    return abs(objetivo-sum)

def grade(populacao, objetivo):
    'Encontra o fitness medio da populacao'

    summed = reduce(add, (fitness(x, objetivo) for x in populacao))
    return summed / (len(populacao) * 1.0)

def evolve(pop, target, retain=0.2, random_select=0.05, mutate=0.01):
    graded = [(fitness(x, target), x) for x in pop]
    graded = [x[1] for x in sorted(graded)]
    retain_length = int(len(graded)*retain)
    parents = graded[:retain_length]

    # adiciona individuos aleatoriamente para promover diversidade genetica

    for individual in graded[retain_length:]:
        if random_select > random():
            parents.append(individual)
    # faz mutacao de alguns individuos
    for individual in parents:
        if mutate > random():
            pos_to_mutate = randint(0, len(individual)-1)
            individual[pos_to_mutate] = randint(
                min(individual), max(individual))

    # crossover dos pais
    parents_length = len(parents)
    desired_length = len(pop) - parents_length
    children = []
    while len(children) < desired_length:
        male = randint(0, parents_length-1)
        female = randint(0, parents_length-1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = len(male) / 2
            child = male[:half] + female[half:]
            children.append(child)
    parents.extend(children)
    return parents