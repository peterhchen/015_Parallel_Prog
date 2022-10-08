import numpy as np
from timeit import default_timer as timer 

def VectorAdd (a, b, c):
    for i in range(a.size):
        c[i] = a[i] + b[i]

def main():
    N = 32000000

    A = np.ones(N, dtype=np.float32)
    B = np.ones(N, dtype=np.float32)
    C = np.ones(N, dtype=np.float32)

    start = timer()
    VectorAdd (A, B, C)
    vector_add_time = timer() - start

    print("C[:5] = " + str(C[:5]))
    print("C[-5:] = " + str(C[-5:]))
    print("VecrtorAdd took for % seconds" % vector_add_time)


if __name__ == "__main__":
    main()