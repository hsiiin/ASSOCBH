import pandas as pd
    
df=pd.read_csv("./test.csv")
    # print(df)
df_content=df.loc[:,"judge_content"]
    # print(df_content)
    
num={"壹":1, "一":1, "貳":2 , "贰":2, "二":2, "參":3, "参":3, "叁":3, "叄":3, "三":3, "肆":4, "四":4,  "伍":5, "五":5, "陸":6, "六":6, "柒":7, "七":7, "捌":8, "八":8, "玖":9, "九":9, "拾":10,"十":10, "佰":100, "百":100}
unit={"年":365, "月":30, "日":1}
    
transfer=[]
transfer2=[]
transfer3=[]
number=0
judge=[]
    
    # 將判刑欄位中每一筆取出
for i in df_content:
    transfer=[]
    transfer2=[]
    transfer3=[]
    number=0
    # 將每一筆判刑內容中文字逐一取出
    for j in i:
    # 將國字數字和單位轉換成數字list
        if j in num:
            transfer.append(num.get(j))
        elif j in unit:
            transfer.append(j)
    # print(transfer)
    # 將transfer list中數字做運算
    for n in transfer:
        if n in unit:
            transfer2.append(number)
            transfer2.append(n)
            number=0
        elif n !=10:
            number+=n
        elif n ==10:
            if number==0:
                number+=10
            else:
                number*=10
        elif n ==100:
            if number==0:
                number+=100
            else:
                number*=100
    # print(transfer2)
    # 將數字和單位做運算
    for m in transfer2:
        if m in unit:
            number*=unit[m]
            transfer3.append(number)
            number=0
        else:
            number+=m
    # print(transfer3)
    # 將刑期加總並加到csv中
    number=sum(transfer3)
    judge.append(number)
        # print(judge)
    
df['number']=judge
    # print(df)
pd.DataFrame(df).to_csv("./test.csv", index=None, encoding="utf-8-sig")