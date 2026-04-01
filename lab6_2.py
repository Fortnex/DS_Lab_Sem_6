from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
if rank==0:
    n = int(input("Enter A NUMBER: "))
    comm.send(n,dest=1)
    for i in range(1,n):
        comm.send(i,dest=1)
    
    data = comm.recv(source=1)
    print("The factorial of ",n," is ",data)
if rank==1:
    op = 1
    n = comm.recv(source=0)
    for i in range(1,n):
        data = comm.recv(source=0)
        op *= data
    comm.send(op,dest=0)