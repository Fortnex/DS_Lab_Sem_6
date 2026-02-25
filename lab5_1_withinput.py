from mpi4py import MPI
import random
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
if rank == 0:
    data = []
    x = int(input("Enter x"))
    n = int(input("ENter n"))
    for i in range(1,n+1):
        comm.send(x,dest = i)
        comm.send(n,dest = i)
    for i in range(1,n+1):
        data.extend(comm.recv(source=i))
    sum = 0
    for x in data:
        if x%5==0:
            sum+=x
            print(x)
    print(sum)

else:
    x = comm.recv(source=0)
    n = comm.recv(source=0)
    data = [random.randint(1, 1000) for _ in range(int(x/n))]
    print(data)
    comm.send(data,dest = 0)
