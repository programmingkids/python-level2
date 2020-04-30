# 「1」から「20」の3の倍数の合計を表示する
total = 0

for i in range(1, 21) :
    if i % 3 == 0 :
        total += i

print( total )
