from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
if rank==0:
    n = int(input("Enter A NUMBER: "))
    comm.send((1,n//2),dest=1)
    comm.send((n//2,n),dest=2)
    firstinp = comm.recv(source=1)
    secondinp = comm.recv(source=2)
    print("The factorial of ",n," is ",firstinp*secondinp)
if rank==1:
    data = comm.recv(source=0)
    op = 1
    for i in range(data[0],data[1]):
        op *= i
    comm.send(op,dest=0)
if rank==2:
    data = comm.recv(source=0)
    op = 1
    for i in range(data[0],data[1]):
        op *= i
    comm.send(op,dest=0)

