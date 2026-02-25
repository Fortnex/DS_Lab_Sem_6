from mpi4py import MPI
import random
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
n = comm.Get_size()-1
if rank%2==0:
    data = comm.recv(source=n-rank)
    sq = data*data
    comm.send(sq,dest=n-rank)
else:
    data = random.randint(1, 100)
    comm.send(data,dest=n-rank)
    op = comm.recv(source=n-rank)
    print("original is: "+str(data)+" squared is: "+str(op))

