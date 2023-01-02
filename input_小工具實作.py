# python中輸入與輸出的函式：input()、print()
# input() => 輸入
# print() => 輸出

# 1.print()函式
# print()是python中負責將結果「輸出」的函式，將輸出的結果顯示在程式執行的命令列中

import time # 引入套件。網路上會有一些Python本體沒有但很好用的套件，利用import可以把他們引入
print("Hello world!") # 輸出引號中的字: Hello world!
print("1","2","3") # 也可以同時輸出多個東西
a=1
b=2
print(a,b)
print(1,2,sep=", ") # sep => 表示每個分隔的對象，在印出時中間的間隔符號，預設為空白
print(1,2,3,sep=",",end=" // ") # end => 預設換行符「\n」，表示印出的結尾符號
print(1,2,3)

# 如果在print的內容前加上「\r」的指令，就能讓每次印出時的游標位置，移動到該行的開頭
# 搭配end不換行的方式，就能做出類似「畫面更新」的效果

# 倒數計時
s=10
for i in range(s+1):
    print(f'\r倒數{s-i}秒',end='')
    time.sleep(1) # 停頓1秒
print('\r時間到',end='')

# 2.input()函式
# input()函式會讓程式暫停，等待使用者輸入文字，python在取得輸入文字後，會把輸入的文字存到一個變數內
# 執行input(x)後，命令列會顯示x內容，並等待使用者輸入內容，按下enter鍵後再進行下方的動作，按下enter之後，可將輸入的內容存進變數內

# 攝氏溫度與華氏溫度之換算：攝氏-->華氏
C=input("請輸入攝氏溫度：")
C=float(C) # 要確保變數是整數或浮點數才能做運算
F=C*9/5+32
print("華氏溫度："+str(F)) # 字串只能和字串相加

# 小工具實作

# 攝氏溫度與華氏溫度之換算：華氏-->攝氏
F=input("請輸入華氏溫度：")
F=float(F)
C=(F-32)*5/9
print("攝氏溫度："+str(C))

# 判斷是奇數或是偶數
number=float(input("請輸入您要判斷的數字："))
if number%2==0:
    print(str(number)+"是偶數")
elif number%2==1:
    print(str(number)+"是奇數")
else:
    print("資料有誤")
    
# 計算機
n1=0
n2=0
n3=0
n4=0
n5=0
n6=0
n7=0
n8=0
confirm=int(input("請選擇要加減乘除的哪一個？「+」請輸入1，「-」請輸入2，「*」請輸入3，「/」請按4："))
if confirm==1:
    n1=float(input("請輸入被加數："))
    n2=float(input("請輸入加數："))
    equals1=n1+n2
    print(str(n1)+" + "+str(n2)+" = "+str(equals1))
    print("答案是："+str(equals1))
elif confirm==2:
    n3=float(input("請輸入被減數："))
    n4=float(input("請輸入減數："))
    equals2=n3-n4
    print(str(n3)+" - "+str(n4)+" = "+str(equals2))
    print("答案是："+str(equals2))
elif confirm==3:
    n5=float(input("請輸入被乘數："))
    n6=float(input("請輸入乘數："))
    equals3=n5*n6
    print(str(n5)+" * "+str(n6)+" = "+str(equals3))
    print("答案是："+str(equals3))
elif confirm==4:
    n7=float(input("請輸入被除數："))
    n8=float(input("請輸入除數："))
    equals4=n7/n8
    print(str(n7)+" / "+str(n8)+" = "+str(equals4))
    print("答案是："+str(equals4))
else:
    print("資料有誤")
    
# BMI計算
height1=float(input("請輸入您的身高(公分)："))
height=height1/100
weight=float(input("請輸入您的體重(公斤)："))
bmi=weight/(height**2)
if bmi<18.5:  
    print("您的BMI值是："+str(bmi)+"，過輕")
elif bmi>24:
    print("您的BMI值是："+str(bmi)+"，過胖")
else:
    print("您的BMI值是："+str(bmi)+"，正常")


