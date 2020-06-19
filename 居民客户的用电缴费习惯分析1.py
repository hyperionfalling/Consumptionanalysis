import csv
with open('customer_pay_habbit.csv', 'r') as f:
    reader = csv.reader(f)
    result = list(reader)
    ####平均缴费金额
    sum_nums = len(result)-1        #第一行不是数据，列表从1开始
    sums = 0                        #统计
    for i in range(1,len(result)):
        sums += int(result[i][2])   #第三项为金额

    ####平均缴费次数
    users_nums = 1
    for i in range(1, len(result)-1):
        if result[i][0] != result[i+1][0] :
            users_nums += 1

    headers = ['平均缴费金额', '平均缴费次数']
    rows = [(sums/sum_nums, sum_nums/users_nums)]

    with open('居民客户的用电缴费习惯分析1.csv','w',newline='') as f1:
        f_csv = csv.writer(f1)
        f_csv.writerow(headers)
        f_csv.writerows(rows)

