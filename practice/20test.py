# 20test.py

city = 'seoul'
pay = 789
rate = 12.34
grade = 'B'

# %형식
print(city, ' ', pay, ' ', rate)


print('도시 %s 급여 %d 환율 %f' % (city, pay, rate))  # %소숫점6자릿기본
# print('% s %s %s ' % (city, pay, rate))
print('도시:%s 급여:%d 환율:%.2f' % (city, pay, rate))  # json 형식으로 착각
print('도시:%s 급여:%d 환율:%.2f' % (city, pay, rate))
print('도시:%s 급여:%d 환율:%.2f 등급%c' % (city, pay, rate, grade))
