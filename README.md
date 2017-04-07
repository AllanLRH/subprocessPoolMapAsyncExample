Demonstrating using asynchronous thread pool to spawn multiple subprocesses.

Note that the program isn't wating for the last map_async to return?? I'll have to think about this.


Sample output (Anaconda Python 3.6.1):

```plain
$ python bjarks_subprocess_dummy_pool.py
Time to sleep: 7.25 s

slept for 0.05 second(s)
slept for 0.2 second(s)
slept for 0.35 second(s)
slept for 0.5 second(s)
slept for 0.65 second(s)
slept for 0.8 second(s)
slept for 0.95 second(s)
slept for 1.1 second(s)
slept for 1.25 second(s)
slept for 1.4 second(s)

Time to compute with 2 threads was 4.493 seconds

slept for 0.05 second(s)
slept for 0.2 second(s)
slept for 0.35 second(s)
slept for 0.5 second(s)
slept for 0.65 second(s)
slept for 0.8 second(s)
slept for 0.95 second(s)
slept for 1.1 second(s)
slept for 1.25 second(s)
slept for 1.4 second(s)

Time to compute with 3 threads was 3.029 seconds

slept for 0.05 second(s)
slept for 0.2 second(s)
slept for 0.35 second(s)
slept for 0.5 second(s)
slept for 0.65 second(s)
slept for 0.8 second(s)
slept for 0.95 second(s)
slept for 1.1 second(s)
slept for 1.25 second(s)
slept for 1.4 second(s)

Time to compute with 4 threads was 2.509 seconds

slept for 0.05 second(s)
slept for 0.2 second(s)
slept for 0.35 second(s)
slept for 0.5 second(s)
slept for 0.65 second(s)
slept for 0.8 second(s)
slept for 0.95 second(s)
slept for 1.1 second(s)
slept for 1.25 second(s)
slept for 1.4 second(s)

Time to compute with 6 threads was 1.983 seconds

slept for 0.05 second(s)
slept for 0.2 second(s)
slept for 0.35 second(s)
slept for 0.5 second(s)
slept for 0.65 second(s)
slept for 0.8 second(s)
slept for 0.95 second(s)
slept for 1.1 second(s)
slept for 1.25 second(s)
slept for 1.4 second(s)

Time to compute with 8 threads was 1.662 seconds

slept for 0.05 second(s)
slept for 0.2 second(s)
slept for 0.35 second(s)
slept for 0.5 second(s)
slept for 0.65 second(s)
slept for 0.8 second(s)
slept for 0.95 second(s)
slept for 1.1 second(s)
slept for 1.25 second(s)
slept for 1.4 second(s)

Time to compute with 10 threads was 1.463 seconds

Overview:
-----------------------------

Pool size   Time (s)
2       4.492825031280518
3       3.0288851261138916
4       2.509101629257202
6       1.982959270477295
8       1.6617870330810547
10      1.463209867477417
```
