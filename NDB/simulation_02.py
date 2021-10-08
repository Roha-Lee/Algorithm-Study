N = int(input())

# 시 0~23 
# 분 0~59 
# 초 0~59

# 초부터 체크 
secs = 0
for sec in range(60):
    if '3' in str(sec):
        secs += 1 
        
# 분 체크
mins = 0
for min in range(60):
    if '3' in str(min):
        mins += 60
    else:
        mins += secs

result = 0
# 시 체크 
for hour in range(N+1):
    if '3' in str(hour):
        result += 3600 # 60 * 60 
    else:
        result += mins

print(result)