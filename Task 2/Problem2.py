text=input()
k=int(input())
freq={}
for i in range(len(text)  - k+1):
    p = (text[i:i+k])
    freq[p]=freq.get(p ,0)+1


max_c = max(freq.values())

result=[]


for j in freq:

        if freq[j]==max_c:
            result.append(j)

print(" ".join(sorted(result)))
