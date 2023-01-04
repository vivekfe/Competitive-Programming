import math
import time
from joblib import Parallel,delayed
t1= time.time()
#results = [math.factorial(i) for i in range(8000)]
results= Parallel(n_jobs=-1)(delayed(math.factorial)(x) for x in range(1000))
t2=time.time()
print(t2-t1)
