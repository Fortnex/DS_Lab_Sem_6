from mpi4py import MPI
import random
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
if rank==0 :
    data = [random.randint(1, 100) for _ in range(5)]
    comm.send(data,dest=1)
    datar = comm.recv(source=1)
    print("the sum from slave is "+str(datar))
    print("sum from master only above 50 is "+ str(sum([i for i in data if i<=50])))
if rank==1:
    data = comm.recv(source=0)
    comm.send(sum(data),dest=0)

