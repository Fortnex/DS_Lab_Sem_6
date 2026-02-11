from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()  
name = MPI.Get_processor_name()
if rank == 0:
    print("Inside parent process")
else:
    print("Inside child process",rank)