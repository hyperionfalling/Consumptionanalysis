import csv
import heapq
import datetime

with open('customer_pay_habbit.csv', 'r') as f:
    reader = csv.reader(f)
    result = list(reader)
    with open('居民客户的用电缴费习惯分析1.csv', 'r') as f1:
        detail = csv.reader(f1)
        result1 = list(detail)
        money = result1[1][0]
        times = result1[1][1]
        #print(times)
        #print(money)
    #### 开四个表，计算用户消费次数和平均金额，放到相应表中
    high_many = []          #高价值型    钱多，次数多
    high_less = []          #潜力型     钱多，次数少
    high_less_perm = []
    low_many = []           #大众型     钱少，次数多
    low_less = []           #低价值型   钱少，次数少
    c = 0
    sum1 = 0
    hesuan = 0
    for i in range(1,len(result)):
        if i+1 == len(result):
            c += 1
            sum1 += int(result[i][2])
            per_sum = sum1 / c
            s1 = result[i+1-c][1].split("/")[0]
            s2 = result[i+1-c][1].split("/")[1]
            s3 = result[i+1-c][1].split("/")[2]
            e1 = result[i][1].split("/")[0]
            e2 = result[i][1].split("/")[1]
            e3 = result[i][1].split("/")[2]
            datadiff = datetime.datetime(int(e1),int(e2),int(e3)) - datetime.datetime(int(s1),int(s2),int(s3))
            per_day = sum1 / float(datadiff.days)
            if c >= float(times):
                if per_sum >= float(money):
                    high_many.append(result[i][0])
                else:
                    low_many.append(result[i][0])
            else:
                if per_sum >= float(money):
                    high_less.append(result[i][0])
                    high_less_perm.append(per_day)
        else:
            if result[i][0] != result[i+1][0] :
                c += 1
                sum1 += int(result[i][2])
                per_sum = sum1/c
                s1 = result[i + 1 - c][1].split("/")[0]
                s2 = result[i + 1 - c][1].split("/")[1]
                s3 = result[i + 1 - c][1].split("/")[2]
                e1 = result[i][1].split("/")[0]
                e2 = result[i][1].split("/")[1]
                e3 = result[i][1].split("/")[2]
                datadiff = datetime.datetime(int(e1), int(e2), int(e3)) - datetime.datetime(int(s1), int(s2), int(s3))
                per_day = sum1 / float(datadiff.days)
                if c >= float(times):
                    if per_sum >= float(money):
                        high_many.append(result[i][0])
                    else:
                        low_many.append(result[i][0])
                else:
                    if per_sum >= float(money):
                        high_less.append(result[i][0])
                        high_less_perm.append(per_day)
                c = 0
                sum1 = 0
            else:
                c += 1
                sum1  += int(result[i][2])


    high_less_perm_index = map(high_less_perm.index, heapq.nlargest(5, high_less_perm))
    high_less_perm_index = list(high_less_perm_index)
    high_less_top5_final = []
    #print(len(high_less))
    for i in range(5):
        high_less_top5_final.append(high_less[high_less_perm_index[i]])



    headers = ['最有可能成为高价值客户的TOP5']

    with open('居民客户的用电缴费习惯分析4.csv', 'w', newline='') as f2:
        writer = csv.writer(f2, delimiter=',')
        writer.writerow(headers)
        writer.writerows(zip(high_less_top5_final))