from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
if rank==0 :
    data = "hiiiidajg"
    comm.send(data,dest=1)
    comm.send(data,dest=2)
if rank==1:
    data = comm.recv(source=0)
    print(set([i for i in data if i in ['a','e','i','o','u']]))
if rank==2:
    data = comm.recv(source=0)
    print(set([i for i in data if i not in ['a','e','i','o','u']]))