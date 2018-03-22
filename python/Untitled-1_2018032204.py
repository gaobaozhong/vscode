#coding:utf
import trees_2018031303 as trees
import treePlotter_2018031701 as treePlotter
#3.4 
#1.手机数据，2， 准备数据，3.分析数据，快速检查数据，却博爱正确的而解析数据内容，使用create Plot函数惠州i最终广东省内图。 
#4. xunliansufan ,shiyonmg crate tree
#5测试算法，辨析测试傻逼你塑胶遗憾和中等裁决测书可以正确分类给定个数据实力。
#6.使用算法，存储输的数据接口狗一边下次使用时无需重新构造书。
  
fr = open('D:\Users\gao\Documents\Code\python\digits\lenses.txt')

lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ['age','prescript','astigmatic','tearRate']
lensesTree = trees.createTree(lenses,lensesLabels)
print lensesTree
treePlotter.createPlot1(lensesTree)

