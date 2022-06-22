from neuron import Neuron

n = Neuron(-1)

x = [1, 2, 0.5]
w = [0.5, -0.1, 1]

r = n.process(x, w)
print(r)

r = n.err()
print(r)

n.apply_err()
r = n.process(x, w)
print(r)
