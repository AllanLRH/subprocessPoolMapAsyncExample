#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
This script measures the time it takes to execute an external program using a thread-pool's
asynchronous map function vs. the pool size.

Note the the multiprocessing.dummy is just like the multiprocessing library, but with
threads instead of processes.

Since the external shell program is not a part of this Python interpreter, it's not
hampered by the "global interpreter lock", aka GIL, so no speed boost should be gained by
using multiple processes. This can be checked by changing:
from multiprocessing.dummy import Pool
to
from multiprocessing import Pool
"""


import subprocess
from multiprocessing.dummy import Pool
from time import time


def call_external(sleep_time):
    """Call shell scripts which sleeps for ⁄ sleep_time⁄  seconds, and prints the time it slept.
    """
    p = subprocess.Popen('sh ./external_program.sh {}'.format(sleep_time).split())
    p.wait()
    stdout, stderr = p.communicate()
    if stderr:
        raise RuntimeError("An error occured:\n\n{}".format(stderr))
    return (stdout)


args = [i/20 for i in range(1, 30, 3)]  # time to sleep


# Print how long the computer would sleep with a single process
print('Time to sleep: {} s'.format(sum(args)), end='\n\n')

time_lst = list()

# Larger args needed for larger pool sizes to be tested, but I'm lazy
pool_size_lst = [2, 3, 4, 6, 8, 10]  # , 12, 16, 20, 25, 30]:

# Measure for how long time the "computation" takes with different pool sizes
for pool_size in pool_size_lst:

    t0 = time()

    pool = Pool(pool_size)  # Chreate threads pool
    # Add the call to the workers pool
    # Use pool.starmap_async for mulitple call-function arguments
    call = pool.map_async(call_external, args)
    result = call.get()  # Do the "computation"
    pool.terminate()  # Kill the pool
    t1 = time()

    time_lst.append(t1 - t0)

    print('\nTime to compute with {} threads was {:.3f} seconds\n'.format(pool_size, t1 - t0))

print('Overview:\n-----------------------------\n\nPool size\tTime (s)')
for ps, t in zip(pool_size_lst, time_lst):
    print(ps, t, sep='\t\t')
