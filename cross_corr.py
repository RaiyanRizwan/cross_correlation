import math

def zero_pad(l1, k):
	return l1 + [0]*(k-len(l1))

def shift(l1, k):
	return l1[-k:] + l1[:-k]

def normalized(signal):
	n = norm(signal)
	return list(map(lambda e: e/n, signal))

def norm(signal):
	return math.sqrt(inner_product(signal, signal))

def compute_corr(signal, received):
	k = len(received)
	signal = zero_pad(signal, k)
	corrs = []
	for s in range(k):
		signal_shifted = shift(signal, s)
		corrs.append(round(inner_product(signal_shifted, received), 2))
	highest_corr = max(corrs)
	return (highest_corr, corrs.index(highest_corr))	

def window_cross_corr(signal, received):
	k = len(received)
	corrs = []
	for s in range(k):
		corrs.append(inner_product(normalized(signal), normalized(shift(received, -k)[0:len(signal)])))
	return (max(corrs), corrs.index(max(corrs)))

def inner_product(s1, s2):
	return sum(map(lambda p: p[0]*p[1], zip(s1,s2)))

def correlations(signal_list, received):
	return {f'signal_{i}': window_cross_corr(signal_list[i], received) for i in range(len(signal_list))}
