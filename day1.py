#q1
np.count_nonzero(np.diff(np.loadtxt('day1.txt')) > 0)
#q2
np.count_nonzero(np.diff(np.convolve(np.loadtxt('day1.txt'),np.ones(3,dtype=int),'valid')) > 0)