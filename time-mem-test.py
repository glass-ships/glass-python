%load_ext memory_profiler
%memit
import time
ti = time.time()

# Code goes here

tf = time.time()
print('Run time: ',tf-ti,' sec')