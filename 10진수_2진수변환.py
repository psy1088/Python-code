def Dec_to_Bin(n):
    if n == 1:
        return '1'
    answer = ''
    while True:
        if n % 2 == 0:
            answer += '0'
        else:
            answer += '1'
        n //= 2

        if n == 1:
            answer += '1'
            return answer[::-1]
