import numpy as np
##################################################################################
def gauss(Matt,bb):
  n = len(Matt)
  m = len(Matt[0])
  mi =[0 for i in range(n)]
  perm_mat = [[int(i==j) for i in range(n)] for j in range(n)]
  Mat = [[val for val in liste] for liste in Matt]
  b = [bb[i] for i in range(n)]
  x = [0 for y in range(n)]
  index = 0
  maxx = int(Mat[0][0])
  for k in range (1,n):
###################################################################################
   #Looking for the max pivot, i could do it without that block of instruction 
    maxx = int(Mat[k-1][k-1])
    for r in range(k - 1,n):  
      if( Mat[r][k-1] > maxx): 
        maxx = int(Mat[r][k-1])
        index = r
    if (maxx != Mat[k-1][k-1]):
      perm_mat = [[int(i==j) for i in range(n)] for j in range(n)]
      perm_mat[k-1],perm_mat[index] = perm_mat[index],perm_mat[k-1]
      Mat = np.dot(perm_mat,Mat)
      b[k-1],b[index] = b[index],b[k-1]
###################################################################################
    if(maxx == 0) : continue #if you havent find any pivot != 0
      #move to the next colone
    for i in range(k,n):
      mi[i] =  (Mat[i][k-1]  / Mat[k - 1][k -1]) 
      for j in range(n):
        p = Mat[i][j]
        Mat[i][j] = p -  Mat[k - 1][j] * mi[i] 
      b[i] = b[i] - b[k-1] * mi[i] 
    mi =[0 for i in range(m)]

  for i in reversed(range(n)):
    s = sum([Mat[i][j] * x[j] for j in range(i,n)])
    if(Mat[i][i] != 0):
      x[i] =  (b[i] - s)/Mat[i][i]
    else:
      x[i] = 0
  return x
###################################################################################
