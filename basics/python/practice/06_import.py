import numpy
print(numpy.__version__)

import pandas as pd
print(pd.__version__)

import package
print(dir(package))

tom = package.animal.Cat(name='tom')
print(tom)


