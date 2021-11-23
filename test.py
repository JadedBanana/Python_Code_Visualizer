import test2

import sys

print(sys.modules.keys())

del sys.modules['test2']

print(sys.modules.keys())

print(test2.test3)

print(sys.modules.keys())

import test2

print(sys.modules.keys())