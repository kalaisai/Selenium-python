a = 4
if a > 3:
    print("a is greater")
else:
    print("b is greater")

# sum of natural no........

summation = 0
for i in range(1,6):
    summation = summation + i
print(summation)

### range( i[start] , j[end] , [iterative index]+1,+2,+3.............)

print("*******************")

for k in range (2,15,3):
    print(k)

print("*********WHILE******************")

ab = 12
while ab > 8:
    if ab == 10:
        break
    print(ab)
    ab = ab-1

#break-break the whole loop a
#continue-continue and goes to previous i

print("**************************")

ab = 12
while ab > 3:
    if ab == 8:
        ab = ab -1
        continue
    if ab == 10:
        break
    print(ab)
    ab = ab-1





