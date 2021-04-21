# 1번 방법 (string 라이브러리 사용)
import string
temp = string.digits + string.ascii_lowercase
def convert_1(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return temp[r]
    else:
        return convert_1(q, base) + temp[r]  # 이 덧셈 순서를 바꿔주면 뒤집어서 출

    
# 2번 방법
def convert_2(num, base):
    temp = ''
    while num:
        temp += str(num % base)
        num //= base
    return temp # 뒤집어서 출력됨


# 출력 값
a = convert_1(11, 3)
print(a)

a = convert_2(11, 3)
print(a[::-1])
