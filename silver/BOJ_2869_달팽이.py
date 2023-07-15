import sys
import math
a,b,v = map(int,sys.stdin.readline().split())
print(math.ceil((v-b)/(a-b)))

'''
int로 소수점 버리는거랑 math.ceil 로 올림 치는거랑 차이 파악해야해
'''