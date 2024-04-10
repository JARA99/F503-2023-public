# file: fit_csv.gnuplot
set terminal pdfcairo
set output 'plot.pdf'

set datafile separator ','

d=0

f(x) = A*exp(-((x-u)/r)**2/2)

A=400
u=200
r=100

fit f(x) 'data.csv' using 1:3 every :::0::d via A,u,r

set xrange [0:400]
# plot 'data.csv' using 1:3, f(x)
plot 'data.csv' using 1:3, 'data.csv' every :::0::d using 1:3, f(x)
# plot f(x)

# unset terminal

