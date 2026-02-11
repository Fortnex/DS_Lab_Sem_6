from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("My rank is :",rank)
if rank==0:
    data = "HI 1"
    destt = 1
    
    comm.send(data,dest=destt)
    print("sending data %s" %data + "to %d" %destt)
    datar = comm.recv(source=1)
    print("receivef from other %s"%datar)
if rank==1:
    desttt = 0
    data = "HI 0"
    
    comm.send(data,dest=desttt)
    print("sending data %s" %data + " to %d" %desttt)
    datar = comm.recv(source=0)
    print("receivef from other %s"%datar)
    