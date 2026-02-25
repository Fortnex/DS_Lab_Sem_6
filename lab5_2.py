from mpi4py import MPI
import random
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
n = comm.Get_size()-1
if rank == 0:
    data = [random.randint(1, 10) for _ in range(1000)]
    even = [x for x in data if x%2==0]
    odd = [x for x in data if x%2!=0]
    data = []
    count = 0
    splitE = len(even)
    splitO = len(odd)
    startE = 0
    startO = 0
    for i in range(1,n+1):
        if i%2 ==0:
            comm.send(even[startE:startE+splitE],dest=i)
            startE+=splitE

        else:
            comm.send(even[startO:startO+splitO],dest=i)
            startO+=splitO
    sum  = 0
    for i in range(1,n):
        sum+=comm.recv(source=i)
    print(sum)
else:
    data = comm.recv(source=0)
    comm.send(sum(data),dest=0)