K = int(input())
inp = list(input())
new = []
var = True
cnt = 0

for n in range(len(inp)):
    var = True
    cnt = 0
    while var == True:
        if inp[n] == '\t':
            cnt = K - (len(new)%K)
            for k in range(cnt):
                new.append(' ')
            var = False
        else:
            new.append(inp[n])
            var = False

for j in range(len(new)):
    print(new[j], end = '')

print()
print(len(new))
