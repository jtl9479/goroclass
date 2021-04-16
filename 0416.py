# for문
"""
기본 구조
for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2

"""

"""
test_list = ['one','two','three','four']
#객체의 값들을 i에다가 넣는다.
test = (1,2,3,4)
for i in test:
#들여쓰기를 통해서 본다.
    print(i+(1))
"""
"""
test_list1 =[(1,2,3),(4,5,3),(7,8,3)]
for (first, ond, las ) in test_list1:
    print(first , ond, las)

학생정보를 저장하는 리스트를 만든다(student_list)
저장되는 데이터의 종류는 학번,이름,핸폰,국어,영어,수학,총점,평균점수이다.
즉, 한개의 리스트는 1명의 학생의 정보를 모두 가지고있다.
"""
"""
d=[]
d.append( input("학번"))
d.append( input("이름"))
d.append( input("핸폰"))
d.append( input("국어"))
d.append( input("영어"))
d.append( input("수학"))
d.append( input("총점"))
d.append( input("평균점수"))

#----> 입력한것을 저장하는곳 

for i in d:

#여기서는 국어점수를 물어봐서 100점이 안되면,"탈락!"이라고 출력한다.
    d[2] = int(d[2])  -->인트형으로 변형하고나서 다시 객체에 저장해야 한다.
    if d[2]<100:  -->[2]위치를 알려준다.
    print("탈락") ->국어점수를 보고 탈락 여부를 알려준다.

su




num = str(input("학번은?"))
name = str(input("이름은?"))
phone = str(input("번호는?"))
ko = int(input("국어 점수는?"))
en = int(input("영어 점수는?"))
math = int(input("수학 점수는?"))
sum = (ko+en+math)
ave = (sum/3)

data=[" %s, %s, %d, %d, %d, %0.1f, %0.1f" %(num,name,ko,en,math,sum,ave)]

for i in data:

 if ko == 100 :
        print("합격")
 else:
        print("탈락")


d=[]
d.append("1001")
d.append("강")
d.append("010-7641")
d.append("10")
d.append("100")
d.append("90")
d.append("290")
d.append("95")
for i in d:  # i는 임시 저장소, 여기서 break까지 for의 영역
    d[3] = int(d[3])
    if d[3] < 100:      #-->[0]부터 시작해서 [3]까지 간다. if의 영역.
        print("탈락")
        break 



thing=["aaa","bbb","ccc"]
for data in thing:
    
    print(data)
    print(data)
    break

#--> break없을때에는 계속해서 반복문이 작동이되지만 break를 사용하면 첫번째만 출력이된다.


@for를 사용해서 1부터 5까지 반복할수있는 방법을 찾으세요




for i in range(1, 4):
   
    print(i)

print(list(range(1,4)))
"""
"""
def add(a,b):  #위에서 아래로 코딩시
    return a+b

a=int(input())
b=int(input())
c=add(a,b)
print(c)
"""
"""
def display(data):
    print(data)
data="asdadasd"  #데이터를 해줘야한다.
display(data)
#===================
def display2(data):
    print("함수가 실행됩니다")
    print(data)
    print("함수가 끝납니다")
display2("abcde")
"""

# 국어,영어,수학점수를 저장해서 함수에게 던진다.
# 던진것을 함수가 받는다
# 함수는 그것을 모두 더해서 총점을 출력한다.
"""
def dis(korean, english, math):
    total = korean + english + math
    print("총점은 %d 입니다" % total)

ko = 100
en = 20
ma = 10
dis(ko, en, ma)


def dis(korean, english, math):
    total = korean + english + math
    return total

ko = 100
en = 20
ma = 10
data = dis(ko, en, ma)
print(data)
"""

"""
class Cookie:
    # 설계도 설계도의 이름은 Cookie이다. 설계도안에 명령어나 데이터를 가지고 있다.
    pass  # 무언가를 하야하는데 할것이 없을때. 아무것도 아니다.
"""

# 게임제작을 하는데 필요한 기능
# 게임서버(로그인,로그아웃)
# 클래스는 기능들과 데이터들을 묶어주는 것이다.
# 문법으로는 아래와 같이 생겼다.
"""
class 설계도 이름 g_sv:
로그인  -->def login():
로그아웃 -->def logout():
플레이 -->def play():
저장 -->def save():
불러오기 -->def load():

a=Cookie()

b=Cookie()
"""
"""
user_info={}
user_info["이름"]="이김박"
user_info["나이"]=15
user_info["성별"]="남자"
user_info["주소"]="인천"
user_info["핸드폰"]="예"
user_info["마스크"]="예"

#print(user_info)
FindOut=input( "찾으실 데이터를 입력하세요.")
print(user_info.get(FindOut))

#print(user_info.get(FindOut))
#values = list(user_info.values())
#print(user_info.get(FindOut))
if user_info.get(FindOut) in user_info.values() :
   print( "ok" )
else:
    print( "none" )


class Cookie:
    # 설계도 설계도의 이름은 Cookie이다. 설계도안에 명령어나 데이터를 가지고 있다.
    pass  # 무언가를 하야하는데 할것이 없을때. 아무것도 아니다.
    # 게임제작을 하는데 필요한 기능
    # 게임서버(로그인,로그아웃)
    # 클래스는 기능들과 데이터들을 묶어주는 것이다.
    # 문법으로는 아래와 같이 생겼다.



class 설계도 이름 g_sv:
로그인  -->def login():
로그아웃 -->def logout():
플레이 -->def play():
저장 -->def save():
불러오기 -->def load():

a=Cookie()

b=Cookie()
"""
"""

##설계도
class cookie:
    # 기능
    def display(self):  # self를 써야한다. 클래스안에다가 집어 넣는다. 클래스 내부에 존재.
        print("나는 디스플레이다")

    def display2(self):
        print("나는 디스플레이2이다.ver2")
    # 데이터
    data = 100


# -------------------
# 액티브하게 돌아가는곳
# 설계도(cookie)로 실제물건(a)을 만들어낸다. 설계도가 먼저다 cookie가 먼저 아니다.
a = cookie()
b = cookie()
# 실제물건에 들어있는 기능중에 display() 라는것을 작동시키겠다
a.display()
b.display2()

"""
class cooki:
    def display2(self):
        print(self.korean)
        print(self.english)
        print(self.math)

    korean=100  #-->출력하고 싶으면 self를 붙여야한다.
    english = 10
    math =90
b = cooki()
b.display2()


