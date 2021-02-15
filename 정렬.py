# 선택정렬
for i in range(len(arr)):  # 쭉~보면서 제일 작은값인 인덱스를 알아내고, 앞에서부터 정렬해나가는거야
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
