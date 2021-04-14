"""
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[-1][0])
print(a[:])

a=[1,2,3,1,3,4,5,1,8,7,5,8,0]
c=a*3
b=[4,5,6]
d=['a','b','c']
print(a[0]+b[0])
print(c)
print(len(c))
print(len(a))
print(str(a[1])+"hi")
print(int(a[0])+4)

a[2] = 4 #[?] 번째 숫자 변경
print(a)
del a[1] #[?] 번째 리스트 삭제
print(a)
a.append(5) #맨뒷열 추가
print(a)
a.remove(3) #선착순 숫자 3 삭제
print(a)
a.sort() #정렬
print(a)
a.reverse() #역순정렬
print(a)
a.index(1)
print(a)

a.insert(0,4) # (a,b) a번쨰 열에 b추
print(a)
a.pop(1) #(a)번째 요소를 remove와 다르게 화면에 출력을 할수가 있다 그리고 삭제.
print(a.pop(1))
print(a)
print(a.count(4)) #(a) a가 몇개있는지를 알려준다.
a.extend([4,5])
print(a)
a.append([4,5])
print(a)
print(a[-1][0] + a[1])

t1=(1,2,'a','b')
print(t1)
del t1[0]
print(t1)  튜플은 그 값은 바꿀수가 없다 생성,삭제,수정 불가능

"""
"""
t1=(1,2,'a','b')
t2=(3,4)
print(t1[0:2])  #인덱싱하기
print(t1+t2) #더하기
print(t1*3) #곱하기
print(len(t1)) #길이구하기
"""
#딕셔너리 {Key1:Value1, Key2:Value2, Key3:Value3, ...}
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(dic)
a = {1: 'hi'}
b = { 'a': [1,2,3]}
print(a)
print(b)
dic['name'] ='key'  #[a:b] a의 키값을 b의 밸류값으로 변경이 가능하다.
print(dic)

c={1:'a'}
print(c)
c[3] = 'b'  #추가
print(c)

del c[1]  #삭제하고 싶을때는 key값을 입력하면 value 값까지 같이 삭제된다.
print(c)

print(c[3])  #key값을 입력하면 value값이 출력 된다.
#key값은 고유값을 가진다 

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())
#key값만을 보여준다 결과값은 dict_keys객체형식으로 나온다.

print(list(a.keys()))
#리스트 형식으로 변환되어서 화면에 출력된다,

print(a.values())
#values값만을 보여준다 결과값은 dict_keys객체형식으로 나온다.

print(list(a.values()))
#리스트 형식으로 변환되어서 화면에 출력된다      

print(a.items())
#키값과 벨류 값을 다보여준다 dict형식으로 보여준다.
print(list(a.items()))
#리스트형식으로 변환되어서 화면에 출력된다.

