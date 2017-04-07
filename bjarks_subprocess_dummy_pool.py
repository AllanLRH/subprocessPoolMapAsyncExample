#!/usr/bin/env python
# -*- coding: utf8 -*-

import subprocess
from multiprocessing.dummy import Pool
from time import time


def call_external(sleep_time):
    p = subprocess.Popen('sh ./external_program.sh {}'.format(sleep_time).split())
    p.wait()
    stdout, stderr = p.communicate()
    if stderr:
        raise RuntimeError("An error occured:\n\n{}".format(stderr))
    return (stdout)


args = [i/20 for i in range(1, 30, 3)]


print('Time to sleep: {} s'.format(sum(args)), end='\n\n')
time_lst = list()
pool_size_lst = [2, 3, 4, 6, 8, 10]  # , 12, 16, 20, 25, 30]:  # Larger args needed, and I'm lazy
for pool_size in pool_size_lst:

    t0 = time()

    pool = Pool(pool_size)
    call = pool.map_async(call_external, args)
    result = call.get()
    pool.terminate()
    t1 = time()

    time_lst.append(t1 - t0)

    print('\nTime to compute with {} threads was {:.3f} seconds\n'.format(pool_size, t1 - t0))

print('Overview:\n-----------------------------\n\nPool size\tTime (s)')
for ps, t in zip(pool_size_lst, time_lst):
    print(ps, t, sep='\t\t')
