from math import ceil,sqrt


def find_max_dist(N,C, i):
    n = N
    c = C

    if n > c:
        asn = ceil(n / i)
    else:
        asn = ceil(c / i)
        if i < n:
         return asn

if __name__ == '__main__':
    print("Max_distance:",find_max_dist(67, 100, 24))

#def number(i,C):

 #for number in i:
#     number = 1
#     if C > number:
 #        number = i+1
 #    else:
  #       number = C
#if __name__ == '__main__':
 #   print(number(3,9))

