seoul_monthly_avg_temp_c = [-2.4, -0.4, 5.7, 12.5, 18.0, 22.2, 24.6, 25.7, 20.8, 14.8, 7.2, 0.4]
seoul_monthly_avg_temp_f = []

months = len(seoul_monthly_avg_temp_c)

for i in range(months):
    seoul_monthly_avg_temp_f.append((seoul_monthly_avg_temp_c[i]*1.8)+32)

print('서울의 월별 평균 기온')
for i in range(months):
    print(f'{i+1:>2}월: {seoul_monthly_avg_temp_c[i]:>7.2f}℃  = {seoul_monthly_avg_temp_f[i]:>7.2f}℉')

print()
for c in seoul_monthly_avg_temp_c:
    print(f'{c}',end=' ')
print()
