import sys
word = list(sys.stdin.readline().lower().rstrip()) #lower로 대소문자 무시, strip으로 공백 제거
dupWord ={}
for i in word:
    try: dupWord[i] +=1 #중복 등장
    except: dupWord[i] =1 #처음 등장한경우
sortedKeyList =sorted(dupWord, key= lambda x : dupWord[x],reverse = True) # value를 기준으로 정렬한 key 리스트를 반환
if len(sortedKeyList)>1 and dupWord[sortedKeyList[0]] == dupWord[sortedKeyList[1]] :
    print("?")
else:
    print(sortedKeyList[0].upper())  # 소문자를 대문자로
