from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("My rank is :",rank)
if rank==0:
    data = 1000
    destt = 4
    comm.send(data,dest=destt)
    print("sending data %s" %data + "to %d" %destt)
if rank==1:
    desttt = 8
    data = "hello"
    comm.send(data,dest=desttt)
    print("sending data %s" %data + " to %d" %desttt)
if rank==4:
    data = comm.recv(source=0)
    print("receviced :%s"%data)
if rank==8:
    data1 = comm.recv(source =1)
    print("receviced :%s" %data1)