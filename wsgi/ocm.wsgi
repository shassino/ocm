from sys import path
from os import chdir
path.insert(0, '/home/shm/ocm/managerserver')
chdir('/home/shm/ocm/managerserver')
from server import app as application
