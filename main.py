from alggen import gen
# -*- coding: utf-8 -*-

target = 371
p_count = 100
i_length = 5
i_min = 0
i_max = 100
p = gen.population(p_count, i_length, i_min, i_max)
fitness_history = [gen.grade(p, target)]
for i in xrange(i_max):
     p = gen.evolve(p, target)
     fitness_history.append(gen.grade(p, target))
for datum in fitness_history:
        print datum
