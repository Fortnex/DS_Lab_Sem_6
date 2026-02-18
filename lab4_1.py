from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
if rank==0 :
    data = [1,2,3,4,5,6,7,8,9,10]
    comm.send(data,dest=1)
    comm.send(data,dest=2)
if rank==1:
    data = comm.recv(source=0)
    print(sum([i for i in data if i%2==0]))
if rank==2:
    data = comm.recv(source=0)
    print(sum([i for i in data if i%2!=0]))