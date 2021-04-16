"""
print("hello world")
print("Mary`s cosmetics")
print('신씨가 소리 질렀다. "도둑이야"')#큰 따음표는 작은 따음표를 사용하면된다.
print('"C/Windows"')
print('"안녕하세여.\n만나서\t반갑습니다."')#\n 줄바꿈 \t tap기능
print("naver;kakao;sk;samsung") #sep=" "을 사용하면 공백 사이에 " "출력
print("naver","kakao","sk","samsung",sep="/")
print("first",end=" ") ; print("second")  #--> 모르겠다
a=5/3
print("%0.1f" % a)

sam = 50000
sum = sam * 10
print(sum)

sum = "298조"
money = "50000원"
per = 15.79
print(sum,money,per)

s = "hello"
t = "python"

print( "%s! %s" % (s,t) )
print(s+"!",t)

a=2+2*3
b=2
c=3
print(a)
print(b+b*c)

a = "1"
print(type(a))

num_str = "720"
print(int(num_str)+2)
num =100
print(str(num)+"a")

flo="15.711110"
print("%0.2f" %float(flo))
year = "2020"
print(int(year)-3)  # 2017
print(int(year)-2)  # 2018
print(int(year)-1) 

a = 48584
print("%d " % (a*36))
"""
"""
letters = 'python'
print(letters[0],letters[2])

license_plate="24가 2210"
print(license_plate[4:8])
print(license_plate[-4:])

st="홀짝홀짝홀짝"
print(st[0],st[2],st[4])
print(st[::2])

string="PYTHON"
print(string[::-1])

phone_number = "010-1111-2222"
number1= phone_number.replace("-"," ")
number2 = number1.replace(" ","")
print(number1)
print(number2)

url = "http://sharebook.kr"
url_split=url.split(".")
print(url_split[1])
print(url[-2:])

string="abcdefghijk"
st = string.upper()
rs = st.lower()
print(string.upper())
print(rs)
print("HI" * 3)


print("-" * 80)
a= "-"
print(a*80)

t1 = 'python'
t2 = 'java'
t3 = t1+" "+t2+" "
print(t3 * 4)

name1= "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: {0} 나이: {1} \n이름: {2} 나이 {3} " .format(name1,age1,name2,age2))
print("이름: %s 나이: %d \n이름: %s 나이 %d" %(name1,age1,name2,age2))
print(f"이름:{name1} 나이:{age1} \n이름:{name2} 나이:{age2}")
#--->문자열 출력하는 3가지 방법

상장 ="5,969,782,550"
상=상장.replace(",","")
print(상)

분기 = "2020/03(E) (IFRS연결)"
print(분기[0:7])

data="  삼성전자    "
print(data.rstrip())
print(data.lstrip())
print(data.strip())

ticker="btc_krw"
ticker1=ticker.upper()
print(ticker1)
ticker2=ticker1.lower()
print(ticker2)


a = "hello"
a = a.capitalize()
print(a)
"""
"""
file_name="보고서.xlsx"
file_name.endswith("xlsx")
print(file_name.endswith("xlsx"))
print(file_name.endswith(("xlsx", "xls")))
"""
"""
user_info={}
user_info["이름"]="이김박"
user_info["15"]="15"
user_info["성별"]="남자"
user_info["주소"]="인천"
user_info["핸드폰"]="예"
user_info["마스크"]="예"

#print(user_info)
FindOut=input( "찾으실 데이터를 입력하세요.")
print(user_info.get(FindOut))
print(type(user_info.get(FindOut)
#print(user_info.get(FindOut))
#values = list(user_info.values())
#print(user_info.get(FindOut))
if user_info.get(FindOut) in user_info.values():
    print( "ok" )
else:
    print( "none" )
"""

movie_rank=["닥터스트레인지", "스플릿", "럭키"]
print(movie_rank)

movie_rank.append("배트맨")
print(movie_rank)
movie_rank.append('스플릿')
print(movie_rank)
del movie_rank[-1]
del movie_rank[-2]
print(movie_rank)

lang1 =["c","c++","java"]
lang2 =["python","go","c#"]
lang3 = lang1+lang2
print(lang3)

nums = [1,2,3,4,5,6,7]
print("max: ", min(nums))
print("min: ", max(nums))

cook = ["피자",'김밥','만두','양념치킨','족발','피자','쫄면']
print(len(cook))

num=[1,2,3,4,5]
a=len(num)
b=sum(num)
ave = b/a
print(b/a)

price = ["20180728",100,130,140,150,160,170]
print(price[1:])

nu=[1,2,3,4,5,6,7,8,9,10]
print(nu[::2])
print(nu[1::2])
print(nu[::-1])

interest = ['삼성전자','lg전자','naver']
print(interest[0], interest[2])
del interest[1]
print(interest)