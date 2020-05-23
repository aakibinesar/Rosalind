k = 15
m = 29
n = 29

p = k+m+n

prob = float(((4*k*(k-1))+(3*m*(m-1))+(4*(2*k*m+2*k*n+m*n)))/(4*p*(p-1)))
print(prob)