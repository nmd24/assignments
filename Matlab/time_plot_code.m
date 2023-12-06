multiplier = (2:2:30);
time_stamp = [0.0579,0.1393,0.3467,0.5695,0.9056,1.3123,1.7906,2.6171,3.1562,4.1569,5.1498,6.5890,7.7855,9.9279,11.4732];

plot(multiplier,time_stamp)
xlabel("Rows, Columns: Multiplier value (in multiples of 50)")
ylabel("Time required to solve the equations (in sec)")

sgtitle(sprintf('Time required Vs Size of given matrix'))