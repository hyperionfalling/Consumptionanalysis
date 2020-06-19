import csv
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
            hesuan += 1
            if c >= float(times):
                if per_sum >= float(money):
                    high_many.append(result[i][0])
                else:
                    low_many.append(result[i][0])
            else:
                if per_sum >= float(money):
                    high_less.append(result[i][0])
                else:
                    low_less.append(result[i][0])
        else:
            if result[i][0] != result[i+1][0] :
                c += 1
                sum1 += int(result[i][2])
                per_sum = sum1/c
                hesuan += 1
                if c >= float(times):
                    if per_sum >= float(money):
                        high_many.append(result[i][0])
                    else:
                        low_many.append(result[i][0])
                else:
                    if per_sum >= float(money):
                        high_less.append(result[i][0])
                    else:
                        low_less.append(result[i][0])
                c = 0
                sum1 = 0
            else:
                c += 1
                sum1  += int(result[i][2])

    max_len = max(len(high_many), len(high_less), len(low_many), len(low_less))
    add_hm = max_len - len(high_many)
    add_hl = max_len - len(high_less)
    add_lm = max_len - len(low_many)
    add_ll = max_len - len(low_less)

    high_many.extend(add_hm * [''])
    high_less.extend(add_hl * [''])
    low_many.extend(add_lm * [''])
    low_less.extend(add_ll * [''])

    headers = ['高价值型', '大众型', '潜力型', '低价值型']

    with open('居民客户的用电缴费习惯分析2.csv', 'w', newline='') as f2:
        writer = csv.writer(f2, delimiter=',')
        writer.writerow(headers)
        writer.writerows(zip(high_many, low_many, high_less, low_less))




