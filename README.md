# cross_correlation
A quick program I wrote to calculate cross correlations. Helpful for comparing a GPS antenna signal with various satellite signals (zero padded instead of periodic) and noise superimposed on the antenna, in order to classify which sats are transmitting.

Note: this code could be further developed to note signal time delay (storing max_corr shifts for each signal) and use linear algebra for computing position, even without time-sync (of sats & reciever) using relative time, >= 4 satellites, & least squares in 3 dimensions. 
