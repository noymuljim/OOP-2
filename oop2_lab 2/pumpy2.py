import numpy as np
score = np.array([85,90,78,92,88])
new_datatype = score.astype('f')
print(new_datatype)
print(new_datatype.dtype)

a_score=score.copy()
a_score= a_score+5
print(a_score)

print(score.ndim)
print(score.shape)
print(score.size)
print(score.itemsize)
print(score.dtype)

print(np.sort(score))

x= np.where(score>80)
print(x)

print(score.mean())
print(score.max())
print(score.min())
print(score.sum())
print(score.std())
print(score.mean(axis=0))
print(score[::2],score[-3:2],score[1:4])
#print(score[-3:2])
#print(score[1:4])

