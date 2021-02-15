# 선택정렬
for i in range(len(arr)):  # 쭉~보면서 제일 작은값인 인덱스를 알아내고, 앞에서부터 정렬해나가는거야
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

    
    

# 삽입정렬
for i in range(1, len(arr)):  # 하나하나 보면서 삽입할 위치를 정해주는거지! 순서에 안맞는놈은 옆으로 밀어내는 느낌
    for j in range(i, 0, -1):
        if arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
        else:
            break
            
            
            
# 계수 정렬
count = [0] * (max(arr) + 1)  # 리스트의 최댓값보다 1 더 크게 리스트 생성

for i in range(len(arr)):
    count[arr[i]] += 1  # 리스트의 값에 해당하는 인덱스의 값 하나씩 증가

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
