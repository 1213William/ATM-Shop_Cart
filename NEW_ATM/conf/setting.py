import os


path = os.path.dirname(os.path.dirname(__file__))
# print(path)

BASE_DB = os.path.join(path, 'db')

BASE_LOG = os.path.join(path, 'log')



