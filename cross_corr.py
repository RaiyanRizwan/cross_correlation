signal_1 = [1, 1, -1, 1, 1]
signal_2 = [1, 1, 1, -1, -1]
received = [.2, .2, 1, 1, -1.2, 1, 1, .2, -.2]
signal_list = [signal_1, signal_2]

def zero_pad(l1, k):
	return l1 + [0]*(k-len(l1))

def shift(l1, k):
	return l1[-k:] + l1[:-k]

def compute_corr(signal, recieved):
	k = len(received)
	signal = zero_pad(signal, k)
	corrs = []
	for s in range(k):
		corrs.append(round(sum(map(lambda pair: pair[0]*pair[1], zip(shift(signal, s), received))), 2))
	return max(corrs)

def correlations(signal_list, recieved):
	return {f'signal_{i}': compute_corr(signal_list[i], recieved) for i in range(len(signal_list))}