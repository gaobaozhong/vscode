import csv
import codecs
import sys
import os
csv_reader = csv.reader(open('201.csv',encoding='utf8',errors='ignore'))
for row in csv_reader:
        print(row[2])
b = []
d=[]

# a=201511020201
# for row in csv_reader:
#
#     if(int(row[0])>=201511020201 and int(row[0])<201511020248):
#
#         if int(row[0]) == a:
#             e.append(row[2])
#         else:
#             a = a + 1
#             #print(e)
#             d.append(e)
#             e = []

# def func(i,a,c):
#     e = []
#     import csv
#     import codecs
#     import sys
#     import os
#     csv_reader = csv.reader(open('6.csv', encoding='utf8', errors='ignore'))
#     # for row in csv_reader:
#     #         print(row[0])
#     b = []
#     d = []
#
#     # a=201511020201
#     # for row in csv_reader:
#     #
#     #     if(int(row[0])>=201511020201 and int(row[0])<201511020248):
#     #
#     #         if int(row[0]) == a:
#     #             e.append(row[2])
#     #         else:
#     #             a = a + 1
#     #             #print(e)
#     #             d.append(e)
#     #             e = []
#
#     def func(i, a, c):
#         e = []
#         for row in csv_reader:
#
#             if (int(row[4]) >= a and int(row[4]) < c):
#
#                 # print(row[0])
#                 if int(row[4]) == a:
#
#                     e.append(row[3])
#                 else:
#                     a = a + 1
#                     print(e)
#                     d.append(e)
#
#                     # csvfile = codecs.open('csvFile2.csv', 'r+', encoding='utf-8')
#                     #
#                     # csvfile.seek(0, os.SEEK_END)
#                     #
#                     # writer = csv.writer(csvfile)
#                     #
#                     #
#                     # writer.writerow(e)
#                     #
#                     # csvfile.close()
#
#                     ###############################
#                     csvfile1 = codecs.open('2015xgbx00.csv', 'r+', encoding='utf-8')
#
#                     csvfile1.seek(0, os.SEEK_END)
#
#                     writer = csv.writer(csvfile1)
#
#                     writer.writerow(e)
#
#                     csvfile1.close()
#
#                     e = []
#                     e.append(row[3])
#                     # e.append(row[0])
#
#     func(1101, 1101, 1444)
#     # func(201511020201,201511020201,201511020240)
#
#     print(d)