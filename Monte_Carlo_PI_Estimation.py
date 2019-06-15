############################## Import libraries
import time
import numpy as np

############################## Implementation of tic toc MATLAB equivalents 
def tic():
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()
def toc():
    if 'startTime_for_tictoc' in globals():
        print "Elapsed time is " + str(time.time() - startTime_for_tictoc) + " seconds."
    else:
        print "Toc: start time not set"

############################## Define sample size and samples that pass criteria
n = 10000 # Number of samples
m = 0 # Number of samples that pass criteria

############################## Start measuring computation time               
tic()

############################## Run the Monte Carlo Simulation
for i in range(n):
    #x = np.random.rand()
    x = np.random.uniform(0,1)
   
    #y = np.random.rand()
    y = np.random.uniform(0,1)
    

    if (x**2.0 + y**2.0) <= 1.0:
        m += 1
        
############################## Print the estimated value of PI
print 4.0*float(m)/float(n)



############################## Finish measuring computation time
toc()