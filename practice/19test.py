# 19test.py

# 1번째 출력

# 초기화 a=7; b=2; hap=0; gob=0;
# 초기화 a,b,hap,gob = 0,0,0,0

a = 7
b = 2
hap = 0
gob = 0

hap = a + b
gob = a * b

print(a, '+', b, '=', hap)
print(a, '*', b, '=', gob)
print()
print('%d + %d = %d' % (a, b, hap))
print('%d * %d %d' % (a, b, gob))
print()
print('{} + {} = {}'.format(a, b, hap))
print('{} * {} = {}'.format(a, b, gob))
print()
print(f'{a} + {b} = {hap}')
print(f'{a} * {b} = {gob}')

print()

mok = 34.647895
print(mok)
print(round(mok, 2))
print('%d' % mok)
print('%f' % mok)


mok = 9856

print('{}'.format(mok))
print('|{}|'.format(mok))
print('|{:10}}|'.format(mok))
print('|{:^10}|'.format(mok))
print('|{:<10}|'.format(mok))
print('|{:>10}|'.format(mok))
print()
print('|{:0>10}|'.format(mok))
print('|{:*>10,}|'.format(mok))
print()

print(1200, '78')  # 앞꺼 숫자 , 뒷쪽 문자
# print (1200 +'78') # 에러발생
print(1200 + int('78'))  # 에러해결
print('abc' + str(78))  # 에러발생
