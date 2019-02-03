# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def get_factors(number):
    r = range(2,number)
    seq = []
    index = 0
    dividend = number

    while index < len(r) and int(dividend/r[index]) > 0:
        if dividend % r[index] == 0:
            seq.append(r[index])
            dividend = int(dividend/r[index])
        else:
            index+=1

    return seq

print(max(get_factors(600851475143)))


