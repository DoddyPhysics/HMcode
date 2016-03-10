reset

#This gnuplot script plots the output file 'power.dat' that is spat out of HMcode.
#Simply load up gnuplot (type gnuplot in the terminal) and then type "gnuplot>load 'plot.p'"
#The plot should then be the non-linear spectrum at 16 redshifts

set log x
set xrange [0.001:100.]
set xlabel 'k/(h Mpc^{-1})'

set log y
set yrange [1e-8:1e4]
set ylabel '{/Symbol D}^2(k)'
set format y '10^{%T}'

file='power.dat'

set key top left

col(i)=sprintf("#%1x%1x0000",i-1,i-1)

plot \
for[i=1:16] file u 1:(column(i+1)) w l lw 2 lc rgb col(i) noti


