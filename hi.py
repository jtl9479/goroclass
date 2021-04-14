"""
a=[1, 3, 5, 7, 9]
b= a[:2]
level =1 
new_level = level +1
print(new_level)
"""
#--------------------------------
#문자열 테스트하기
"""
new_weapon = "axe"
new_weapon2 = "shotgun"
new_weapon3= "bow"
new_weapon4 = "rocket-launcher"
print(new_weapon4[:])
new_weapon5 = "sword"
"""
#퀴즈:print 명령어를 1개만 사용해서 5개의 문자열을 모두 출력해보세요
#print(x,x2,x3,x4,x5)

#print( new_weapon,new_weapon2,new_weapon3,new_weapon4,new_weapon5)
#제목 같은걸 찍은다음에, 데이터를 출력하기
#print("my weapon is "+  new_weapon)
"""
print(new_weapon*2)
print(len(new_weapon))

c = "life is too short, you need python"
print(c)


d="i eat {0} apples."
print(d .format("두"))

e=" i am %s "
print(e % "배고파")
print(len(e))

a1=10
a2="tree"
a3="i am {0} apples, so i was sick {1} days."
print(a3 .format(a1,a2))
print("{0:배^10}".format("hi"))
#a4="{0:!<10}"
#print(a4.format("hi"))

string = "abcde"
print(string[0:2])
print(string[2:2])
print(string[3:2])




b1 = "pithon"
#b1[2]="a"
print(b1[:1] + 'y' + b1[1:])
print(" i eat {0} apples." .format(20))
print ("i eat %d %d apples." % (3, 3))

number = 1.23456
num = 1.7
print("i eat %0.2f %d " %(number, num))

data_backpack = ["abc","def","ggg","xxx","www","naver" ,"com"]
print(data_backpack[0]+data_backpack[1])

#리스트에 어떤데이터들을 저장해둔후에, 그것들을 수정해본다 (UPDATE, FIX)
#리스트는 어떤 데이터든 저장할수 있다.(정수,실수,글자)
number = [1,2,3,4,5]
char_box = ['A','B','C']
f_number = [1.0,2.0,3.2,5.432]
mix = [1,2,3,'A',7.123,-100.2]

#numbers 라는 것의 [2]번방에는 현재 3이 들어가 있다. 그것을 3.0으로 바꾼다
number[2] = 3.0
char_box[0] = '2'
f_number[2] = "what" #여긴 원래 소수점이 들어간다.
mix[1] = "unknown"
print(number)
print(char_box)
print(f_number)
print(mix)

#----> 수정이된다
#게임케릭터의 정보를 리스트에 저장해보자
#저장할 정보는 아래와 같음.
#리스트의 이름은 game.player
#그곳에 저장할 게임캐릭터의 이름은"player1"
#체력은 1000.123
#마력은 200.2
#무기는 "sword"
#레벨은 7
#전부다 잘 저장되었다면, 모든 정보를 한꺼번에 출력해보세요

i = "game.player"
n = "player1"
h = 1000.123
d = 200.2
s = "sword"
l = 7

print("%s %s %0.3f %0.1f %s %d" %(i,n,h,d,s,l) )
print("game.player " + n  )

#게임케릭터의 정보를 리스트에 저장해보자
#저장할 정보는 아래와 같음.
#리스트(데이터들을 여러가지 저장할수 있는곳)의 이름은 game.player
#그곳에 저장할 게임캐릭터의 이름은"player1"
#체력은 1000.123
#마력은 200.2
#무기는 "sword"
#레벨은 7
#전부다 잘 저장되었다면, 모든 정보를 한꺼번에 출력해보세요

game_player=["player",1000.123,200.2,"sword",7]
print(game_player)

n = "player1"
h = 1000.123
d = 200.2
s = "sword"
l = 7

game_player=[n,h,d,s,l]
print(game_player)
"""
"""

a="fsdkjhsfdpodqwpovklnbcvlkjnewpokdwqpomkvxcklmnasdlnk"
print(a.count('k'))
print(a.find('f'))

print("a".join('1111111111111'))

#리스트에 숫자 2개를 저장한다
#result에다가 저장을 한다.
#그리고 더한다
number=[100,123,101,105,107]

result = number[0] + number[1] + number[2] + number[3] + number[4]
print(number[0],number[1])
print(number[0]+number[1])
print(result)

#소숫점숫자를 1개 저장한다 (변수에 저장한다 이름은 n1)
#소숫점숫자를 1개 저장한다 (변수에 저장한다 이름은 n2)
#두개의 숫자를 더한결과를 변수에 저장한다 변수 이름은 n3
#더한 결과를 출력해본다
#출력결과를 소숫점이하 2자리까지 출력하도록 조정해준다
#소숫점을 조정할수있는 어떤 명령어나 방법이 존재한다.(round)
n1= 1.234483
n2= 3.3431434
n3=n1+n2
print(n3)
print("%0.2f" %n3)
print(round(n3, 2))
"""

#성적처리를 할수있는 파이썬 코드를 짜보자
#국어점수를 저장할수 있는 변수를 만들고 거기에 국어점수를 저장
#영어점수를 저장할수 있는 변수를 만들고 거기에 영어점수를 저장
#수학점수를 저장할수 있는 변수를 만들고 거기에 수학점수를 저장
#3과목의 점수를 더해서 총점을 구한후에 그걸 총점 변수에 저장함
#총점을 출력한다.

#korea = [100]
#english=[70]
#math = [80]
#--->리스트 배열형식
#korea = 100
#english=70
#math=80    -->단순한 인트형
korea = int(input("국어점수는 ?"))  #input은 기본적으로 string으로 받는다 int로 형변환을 해줘야한다.  
english = int(input("영어점수는 ?"))
math = int(input("수학점수는 ?"))
total = korea + english + math
ave = total/3
print("총점의 합은: ", total)
print("평균: %0.1f" %ave)
print("평균의 합은 : " , round(ave,1))
