"""
head = "python"
tail = " is fun"
print(head+tail)
print(len("is"))
print(tail[1])      #-->객체 인덱싱
print("tail"[1])    #-->string

gun = tail[0] + tail[1] + tail[2] #-->슬라이싱 단어를 합친다 a[시작 번호:끝 번호]
shut = tail[0:2]
print(gun)
print(shut)
"""
"""
#포매팅  문자열을 대입하는 프로그램

#input을 사용해서 회원의 이름을 입력받고 저장한다
name = input("이름은? ")
#마찬가지로 회원의 정보 4가지를 입력받아서 저장한다
phone = input("번호는?")
id = input("아이디는?")
num = input("암호?")
add = input("주소는?")

#5개의 데이터가 잘 저장되었는지를 확인해본다.(출력.print)
print(name + phone + id + num + add)
#print(name.replace(name,"1"))
#리스트에다가 데이터값5개 저장
info=[name,phone,id,num,add]
#info=[name.replace(name,"1"),phone ,id ,num ,add] #name값을  input이 아니라 원하는 값으로 변경한다.
print(info[:])
info.append(['a','b'])
print(info[:])
"""
"""
#===========================  딕셔러니
코드 형식 key,values
이름 : kim
전화번호 : 010
저장공간의 이름을 먼저 결정해야됨.(useonfo)
userinfo={}
userinfo={이름:kim, 전화번호:010}
userinfo={"이름":"kim", "전화번호":"010"}  --->딕셔너리 완성본
"""
"""
userinfo={"이름":"kim", "전화번호":"010"}
print(userinfo)

name = input("이름은? ")
phone = input("번호는?")
id = input("아이디는?")
num = input("암호?")
add = input("주소는?")

a={"이름":name, "번호":phone,"아이디":id,"암호":num,"주소":add}
print(a)

a[2] ='b'  #--->딕셔너리 추가
print(a)

del a["번호"] #---->삭

print(a)
print(a["이름"])  #---->values값 출력
"""

"""
s1 = set(['a','b','c','d','e','f'])
print(s1)

s2=set([1,2,3,4,5,6,7])
l1=list(s2)
t1=tuple(s2)
print(s2)    #-->리스트 형식으로 안나옴
print(l1[:]) #--->리스트 형식으로 나옴
print(t1)    #-->튜플형식으로 나옴

s3="a"

print(ord(s3))

print(ord(l1))
"""
#print(ord(s1)&s2)
"""
조건문 
condition = True #조건이 참이다.
if condition:   --->이 조건이 뭐였든 "참" 이라면 밑에있는 PRINT를 실행한다
    print("참!")--->탭키로 밀던, 스페이스바로 밀던 상관없다. 같은 칸을 밀면된다
    #만약 조건이 뭐였든 거짓이라면 이곳으로 이동하게 된다.
print("거짓!")

비교연산자	설명
x < y	x가 y보다 작다
x > y	x가 y보다 크다
x == y	x와 y가 같다
x != y	x와 y가 같지 않다
x >= y	x가 y보다 크거나 같다
x <= y	x가 y보다 작거나 같다


condition = False     #조건이 참이다.
if condition:        #--->이 조건이 뭐였든 "참" 이라면 밑에있는 PRINT를 실행한다
            print("참!")     #--->탭키로 밀던, 스페이스바로 밀던 상관없다. 같은 칸을 밀면된다
            print("참!")                 #만약 조건이 뭐였든 거짓이라면 이곳으로 이동하게 된다.

            print("참!")
            print("거짓!")
            print("거짓!") #else 사용하지 않을 경우 false값은 붙어있어야한다.


money=True
if money:
    print("택시를 타라")
    print("버스를 타라" )
    print("차를 타라")
else:
        print("걸어가라")

x=3
y=2
print(x<y)


money = 2000
if money <= 3000:
    print("택시타라") #--->True값

    print("걸어가라") #--->False값
else:
    print("몰라")



#if를 이용한 프로그램 만들기
@점수에 따라서 합격/불합격 여부를 판단하기
(1) 국어,영어,수학점수를 입력받아서 모두 리스트에 저장한다.
리스트의 이름은 user_score
(2)저장된 점수들은 모두 글자일것이다, 이것들을 전부 숫자로 바꿔서 저장해둔다.
(3)3개의 점수들을 모두 더해서 총점을 계산한후에 출력한다,


korea=input("국어 점수는?")
english=input("영어 점수는?")
math=input("수학점수는?")

score =[korea,english,math]

score = (int(korea)+int(english)+int(math))
ave = score/3
print("3과목 총합은? %0.1f"  % score)
print("3과목 평균은? %0.1f" % ave)

#(4) 총점이 250점이상이면, 합격 이라고 출력해주고 250점 미만이면 불합격 출력
max_score = 250
if score >= max_score:
    print("합격")
else:
    print("불합격")

"""
"""
pocket = ['paper', 'handphone']  #여기있는 것을 가지고 활용한다
card = True                     #여기있는 것을 가지고 활용한다
if 'money' not in pocket:
     print("택시를 타고가라")
else:
      if card:
          print("버스를 타고가라")
      else:
            print("걸어가라")          
"""
"""
@소지품중에 어떤것이 있는지 확인-해본다
1.리스트를 준비한다
2.입력을 받아서 3개의 물건을 리스트에 저장해준다(문자열)
3.찾고싶은 물건을 변수에 저장해둔다.(Find_This)
4.if문을 사용해서 3개의 물건중에 찾고 싶은 물건과 일치하는것이 있는지를 물어본다
있으면, "찾았다" 없으면 "없다"
"""
"""
d=[]
d.append( input("첫번째물건"))
d.append( input("두번째물건"))
d.append( input("세번째물건"))
e="돈"
print(d)
if "돈" in d:
    print("찾았다")
else:
       print("없다")

goods =["돈","펜","노트","지우개","자"]
a=input("찾고싶은 물건")

if a == "돈":
    print("있다")
else:
    print("없다" + str(goods) + "이런게 있다")
"""

"""
@회원정보저장
1.딕셔너리를 만든다
userinfo=()
2.거기에 새로운 데이터를 저장한다.(회원정보 정보는 마음대로 갯수도)
userinfo["이름"]="김"
userinfo["주소"]="부천"
userinfo["핸드폰"]="010"
userinfo["나이"]="28"
print(userinfo)
3.검색하고 싶은 데이터를 입력받는다
4.입력받은 데이터를 덱셔너리에서 검색한다
이 부분은 새로운명렁어를 찾아야 할수있기 때문에 구굴링이나 책에서 찾아볼것
FoundOut
5.찾았으면 "ok" 아니면"none"
"""

name =input("이름은? ")
age =input("나이는? ")
add =input("주소는? ")
phone = input ("번호는? ")

a = { "name":name,"age":age,"add":add,"phone":phone }
print(a)

b= { "name":"강","age":"28","add":"부천","phone":"010" }

if a == b :
    print("ok")
else:
    print("none")







