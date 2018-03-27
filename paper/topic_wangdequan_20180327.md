# three elementsin automnomous driving

## dequan wang

## Elemnets of autonomous driving ：three papers

* perception
    * high accuracy 
    * efficent
    * unified framework
* data
    * large scale
    * realistic
    * diverse
* environment
    * reefect real driving
    * control simulation
    * rich annotation data 

## Overview: image recognition

* too much networks
* common classification networks
* learn to Aggregate Blocks
    * Aggregate Blocks: 把线性block改为树形block，这样，深度变深。有效深度变深的时候，会出现deep inside 现象。改进之后，让深度不是很深，防止不收敛。最后提出了非线性

## Dense prediction

## Shallow Aggregation

## Iterative Deep Aggregation

* 兼顾了语义和分辨率

## boundary prediction

* 在另一个数据集上效果测试更好 
* 我们发现，除了线性组合，可以结合树形结构

## BDD current Release

* 如果你训练iphone的照片是不好的，所以，采集数据要求 不要有设备要求
* 720P的数据，36000多，有gps数据，
* 输入是viedo，
* 有两个人，可以inside sumtaton

## BDD Next

* 我们有100k 的视频要做
* 隧道场景很难做，camera在隧道进入和离开的时候，会曝光，这样就是机器失明状态
* 地理位置纽约
* Scene :场景很多样
* Object Numbers：自行车等各种车
* Diversity：
* 这是第一方面

## Scalable annotation tool

## Bounding Box Annotation

* 标注需要很多人做，而且很难做,手工画图，很难做，一个人，一张图，一小时，这就是ai的现状

## Bounding Box Annotation

* Prepareimages
* 自动检测，提高了标注效率

## Region Annotation

## Simulation

* Grand Theft Auto
* GTA很真实，可否用游戏来测试自动驾驶。
* GTA Game API:没有花一分 钱，用游戏来跑测试，得到了很好的结果。
    * interactive conntrol signal
* 3D Vehicle Tracking: 可以把轨迹画出来，预测出轨迹。
