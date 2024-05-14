s = 2; N = 200; primeSum = [0]*(N+1)
primeSum[2] = s
for i in range(3, N, 2):
    if primeSum[i]==0:
        s+= i
        primeSum[i::i] = [-1]*(N//i)
    primeSum[i] = s
    primeSum[i+1] = s

print(primeSum[20])
