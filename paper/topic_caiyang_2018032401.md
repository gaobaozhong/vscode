# foveacam a proactical solution to face recognition in surveillance

# garbage in , garbage out

* recognitionaccuracy drops sharply as faces get oto small
    * task : face verification
    * dataset:lfw
    * method:vgg-face & relesed model
* 把官方数据图片缩小之后，发现数据质量太差的时候，任何应用效果都很差。

# why not just increase resolution?

* problems: 4k的图片看远处图片也不清楚
* motivation:
    * capture distant * Objects Clearly
* inspiration
* 
: human eyes
    * perception
    * 人眼的余光可以看的很多。
    * 人眼有特殊构造
    * 人眼不是均匀
    * 有个黄斑，fovea，是视力最好的地方

* image sensing:
* simulate image understaning 
    * accurate ,robust and efficetn cnn-based object detection
