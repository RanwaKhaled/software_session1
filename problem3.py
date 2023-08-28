#Problem 3: money
money = int(input('enter the sum of money: '))
rest = money
if rest>=200:
    p200 = int(rest/200)
    rest = rest%200
    print(f'{p200}x200LE',end=" + ")
if rest >=100:
    p100 = int(rest/100)
    rest =rest%100
    print(f'{p100}x100LE',end=" + ")
if rest>=50:
    p50 =int(rest/50)
    rest=rest%50
    print(f'{p50}x50LE', end=" + ")
if rest >= 20:
    p20=int(rest/20)
    rest=rest%20
    print(f'{p20}x20LE', end=" + ")
if rest>=10:
    p10=int(rest/10)
    rest=rest%10
    print(f'{p10}x10LE', end=" + ")
if rest>=5:
    p5=int(rest/5)
    rest=rest%5
    print(f'{p5}x5LE', end=" + ")
#p1 = rest
if rest>0:
    print(f'{rest}x1LE')