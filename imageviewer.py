from matplotlib import pyplot as plt
import numpy
import sys


data = numpy.load(sys.argv[1])


plt.imshow(data, interpolation='nearest')
plt.show()