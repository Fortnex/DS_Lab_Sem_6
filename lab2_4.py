from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("My rank is :",rank)
if rank==0:
    data = "HI 1"
    destt = 1
    
    datar = comm.sendrecv(data,dest=destt,source=destt)
    print("sending data %s" %data + "to %d" %destt)
    print("receivef from other %s"%datar)
if rank==1:
    desttt = 0
    data = "HI 0"
    
    datar=comm.sendrecv(data,dest=desttt,source=desttt)
    print("sending data %s" %data + " to %d" %desttt)
    print("receivef from other %s"%datar)
    