from mpi4py import MPI
import random
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
x = 9
n = 3
if rank == 0:
    data = []
    for i in range(1,n+1):
        data.extend(comm.recv(source=i))
    sum = 0
    for x in data:
        if x%5==0:
            sum+=x
            print(x)
    print(sum)

for i in range(1,n+1):
    if rank == i :
        data = [random.randint(1, 1000) for _ in range(int(x/n))]
        print(data)
        comm.send(data,dest = 0)
