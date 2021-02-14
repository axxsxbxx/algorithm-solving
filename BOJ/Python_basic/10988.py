word = list(input())
word_reverse = list(reversed(word))
if word == word_reverse:
    print(1)
else:
    print(0)

# reverse 사용하지 않는 방법
n = list(input())
m = []
r = 0
for i in range(len(n)-1,-1,-1):
  m.append(n[i])
for j in range(len(m)):
  if n[j] == m[j]:
    r = 1
  else:
    r = 0
    break
print(r)