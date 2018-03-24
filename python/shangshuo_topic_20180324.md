# Searching trajectories by regions of interest

## 阿拉伯土豪大学

# problem

* TsR 感兴趣区域
* Given
* Finds 从空间和密度中寻找轨迹
* 已有的轨迹搜索，一般用在旅程规划中，

# 背景

* 给一组查询点，查询相似的轨迹
* 我们是给查询区域
* 因为用户给新区的地方不是一个点，而是要给区域。我们认为用户 对POI密集的区域会更感兴趣

# 例子

# challeges

* network-based query
* massive trajectory data millons of trajectories
* sheduling multiple query sources

# problemm definition

* spatial influence factor between two vertieces
* 要增加考虑密度

# Baseline method

* uniform-speed search
* netowrk epasion form ceners 
* bounds : a Lb

# weakness

* scheduling 
    * the seraches of query regions are ateh same speed
    * uss lacks of an effective scheduling strategy 
* search space overlap 
    * if centero of twoquery 被反复读写，影像效率

# best-expansion serach 

* 估算整体范围，可以是整体范围最小，可以范围小的可以得到最高的效率
* 交互查询，需要时间，最优结果可能时间较长，我们假定均匀分布。

# scheduling

* 只搜索优先级最高的

# extension

* 已有的查询，是没有排序的。

# 实验

* 北京出租车80万的数据集

# summary



