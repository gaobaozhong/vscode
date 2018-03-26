#coding:utf
# 很长时间了，准确的说应该是23号到现在，今天是25号了，两天的时间了，这两天我实在没想明白，毕业是怎么做这样的一个集体学习，我觉得你在忙这本书的内容，再读一遍，从现在开始一直到读完整张不停，预备开始，
# 第四章，基于该浏览的分类方法，朴素，贝叶斯本条内容使用概率分布进行分类学习，朴素贝叶斯分类器仅需2s原数据使用朴素贝叶斯来分析不同数据的态度，前两章我们要求分类器作出艰难决策，给出该数据实例属于哪一类，这样的问题的明确答案，我们学的是天天和那个，橘子树，分类的很简单，只需要判断一下距离，然后找出这些距离中那个最贱的那些，然后找出前十条，再看一下这前十条中有多少个类别，找出那个最大的那个，然后作为我们反馈结果，它又属于哪一类？而且该说的话呢，则是根据我们的熵值，先判断一下商局哪个商品最大，然后他就进行以哪个属性来进行分类，然后最后的话呢，看看我们之后几点大概属于哪一个分支，这个分支的话呢，然后由这个分支是哪一类，然后决定他属于哪一类？有时会产生错误，结果这个时候要求分类器给出一个最优的类别才算结果，同时给出这个猜测的概率估计值，也就是说我们之前的作品说的是确定结果，但是我们这里假定要给出一个结果，还要给他给出这个结果，是这个结果类别的可能性的概率值，这个时候就要用到概率论了，
# 概率论是谁的计算机学习算法的基础，我们深刻理解这一主题显得非常重要，根本就是所谓的一个数的频率嘛，第三张在计算特征，即取某个值的概率的时候，设计了一些概率知识，我们这里先统计特征，在数据集中取某个特征值的次数，然后除以数据集的实例总数就得到了特征，取该值的概率，我们将在此基础上进行深入讨论，
# 本章会给出一些使用概率论进行分类的方法，首先从一个最简单的概率分力气开始，然后给出一些假设来学习朴素贝叶斯分类器，我们称之为，是因为整个形式化过程只做最原始最简单的假设，不必担心，你会详细了解到这些假设，我们将充分利用排放的文本处理能力将文本签分为词向量，然后利用词向量对文档进行分类，我们还将构建另一个分类器，观察其在真实的垃圾邮件数据集中的过滤效果，必要时还会回顾一下条件概率，最后我们将介绍如何从个人发布的大量广告中学习分类器，并将学习结果转换成人类可理解的信息，
# 你，第四章，基于概率论的分类方法，朴素贝叶斯，使用概率分布进行分类，我是贝叶斯分类器，婕茜元数据使用朴素，贝叶斯来分析不同地区的态度，前两章我们要求菲立即作出艰难决策，给出该数据的实例属于哪一类之类问题的明确答案，不过分类器有时会产生错误结果，这是要求分离，请给出一个最优的类别猜测结果，同时给出这个猜测的概率估计值，概率论是许多及其学习算法的基础，所以深刻理解这一主题就显得非常重要，第三张在计算特征值，取某个值的概率是涉及了一些概率知识，在那里，我们现在统计特征，在数据集中去某个风景区的次数，然后除以数据集的是一种书，背得到了特征乞丐这个概率，我们在这个基础上深入探讨，会给出一些使用的方法，最简单的概率分类器开始，然后给出一些假设来学习，不是vs朴素，是因为整个形式化过程只做最原始最简单的假设，不会担心，我们将充分利用排放的，橙子销量分类，我们还将构建另一个分类器，观察其的真实的垃圾邮件，数据集中的管理结果表示我们回顾一下条件概率，最后人家介绍如何从个人发布的大量广告中学习分类器，结果转化为人类可理解的信息，4.1，基于贝叶斯决策理论的分类方法，朴素也是，它的优点是在数据较少的情况下依然有效，可以处理多了一个问题，缺点是对于输入数据的准备方式较为敏感，他是用的数据类型，是标称使用标称型数据，朴素贝叶，斯是卞思决策里面的一部分，快速了解一下被鞭尸的军事理论，我们现在有一个数据集团，有两类数据组成数据分布是这样子的，如图4-1所示，这个概率分布参数决定了分布的形状，为读者找到了描述图中两列数据的统计参数，暂且不用管，如果找到描述这类数据的统计参数，第十章会详细介绍，我们现在用ps vita数据几点sy属于类别一的概率，用ps vita是数据点y属于二的概率，那么对一个声音的数据点，可以用下面的规则来判断它的类别，若psy大于ps外，那么类别一，如果ps的ps的那么累点儿，也就是说我们会选择高概率对应的类别，这就是BS决策理论的核心思想，你选择具有最高概率的决策，回到图斯港一场，如果该图中的整个数据使用六个浮点数来表示，那么计算类别概率的开放代码只有两行，那么你会更倾向于哪一个方法？那就是你的灵魂累了，第兄弟大热天可以进行一千次的距离计算，第二行，第二的决算数，分别沿x轴和y轴划分数据，第三，计算数据点属于哪个类别的概率？这里有一个问题就是他有个假定就是，如果图中的每个数据使用六个分数来表示，这里的人的备注就是整个数据由两类不同分布的数据构成，有可能只需要六个统计参数来描述好，整个数据集是两类不同的数据，每个数据都放在有六个同学猜出，这六个才出第六课属性点数表示现在计算一个新点就给你新的一个六个浮点数来，让你判断它属于哪个类别，那么应该怎么做呢，他说第一个，如果使用第一张的天，这几天一千次的距离也算这里有个问题哈，这个1400怎么计算出来的k它是怎么计算的呢？他是要计算新来的一个点和已有的点的距离，然后取钱可不可以？你呢？因为有多少点中确定这里，他好像是说，一千个人就有做一千层的颜色，第二个是使用第二大的决策树，这群特殊的话能言数据决策书的话是按照属性，俺求它的熵值的这些属性的话呢，因为有六个浮点数的表示有六个参数，华南这里六个属性，因此他说要按照，和百度来划分数据，六个属性的空间是，再加上第三270，数据判断，属于每个类别的概率，这个方法就是说判断题的概率是多少？概率是多少？这个该怎么判断？这还是个问题，这可能就是本章的重点了，不会非常成功，而简单的概率计算相比堪的计算量又太大，对于上述问题，最佳选择是使用刚才提到的概率比较方法，接下来的话，我们要详细描述一下，如何计算一下这两个概率，计算题一和p2，讨论一下条件概率，如果你觉得自己已经相当了解条件概率，那就可以跳过下面的部分，这里穿插一下什么叫贝叶斯的概率地属于边，也是概率理论的范畴，该流行而效果非常的好，别失了律师，80级的一个婶婶家就他妈44，他的名字便是概率论，引入了先验知识和逻辑推理来处理，不确定命题，另一种概率解释称为频数概率，他只从数据本身，或许结论，并不考虑逻辑推理和先验知识，这是说的另一种概率啊，他指的是普通的概率，就指的是频率很快碎报告给你听，他要考虑逻辑和先验知识了，就像考虑这个条件，这个东西就是所谓的条件，因此这里称之为条件概率，第二届条件概率，来看一下，如果你对ps外，在c一的条件下，这个符号比较熟悉，那么我就可以学得比较轻松一些了，假装我们现在有七个石头，在罐子里，这个以前的这个石头有三块是灰的，有四块是黑色的，如果从袋子中随机取出一块石头，那么灰色石头的可能性有多大？如果取石头有几种可能那么三种为灰色，那么肯定取灰色石头的概率就是3/7，取黑色石头的概率呢是4/7，这个是非常简单的，我们用屁股的事情，灰色石头的概率就是灰色石头的数目，就是灰色这个属性的数目，除以总数，一个包含71000盒，深色的颜色为灰色或黑色，如果随机从中取一块石头，他们取得成功的概率是3/7的灰黑色石头的概率4‰，如果七块石头如图13所示，放在两个桶中，这里哪有问题了，我们现在要把这个七块石头灰的四款黑的发两个图中的概率应该如何计算？我们把那个四块石头放倒了一桶中，把三块石头放到了地图中，现在要计算一下这个灰色和黑色石头的概率，事先要知道的信息会不会改变结果呢？有可能影响到了计算，从鼻孔中取出灰色石头的概率的方法，就是条件概率，小弟呢，计算的是从b桶取出灰色石头的概率，这个频率的KTV pk在八桂大地等一下，我们称之为在已知石头出自逼吞下去住黑色石头的概率，，在park city学校，我们可以得到这个结果，一中的有两个炮灰的，两块黑的，总共四块石头，那么在一桶中取出灰色石头的概率，那肯定是2/4答应的币种中，那两块黑的一半灰的那么屁龟，在吧Q币的条件下，它的概率就是1/3，1/2的，分别的意思就是灰色石头在不同的桶中的概率，这就是一个条件概率，其他公式呢是这样子的，我们刚才是直接数出来的，它的公式是，p在b条件下，它的概率等于p这张的大kb就是g在b中又在，又是灰色的石头的概率，除以p8kb就是是取得石头是发Q币，这个图中的他的概率，这个公式是否合理，首先呢，我们刚才已经看出来了，这个屁股扒开的b呢，它的值是1/3，首先我们看一下，在桶中灰色石头的总数，除以两桶中总数是多少？灰色石头的总数在笔筒中呢，是两个黑的，一个黑的，因此它的总数就是一个，而那个总数的是，我不知道，说的是那个七个，因此这个px就是技术灰色的笔筒中的这样的石头的概率的就是1/7，然后再算一下这个id，他的气质，八个都比他的概率的性质，就是你取一个石头在不同的概率，鼻孔有三块石头，那个黑桶有四块石头，那么b桶中的石头出现在地图中，石头的概率就是3/7号呢，结果正好是1/3，这个和我们刚才所算的这个条件概率，这个是这个是吻合的，这个故事对于简单例子来说的有点复杂，但对存在动作特征的时候就非常有效，例如有必要我们如何交换条件概率中的条件和结果，即如果已知px的条件下，求PC x的方法，x等于ps，好，再来一张，他有这么优秀的方法叫PC x就是求求那个c，science的条件下的概率，等于ps概率乘以bc，在处理px，你的话能这个大家要理解一下，我们现在讨论的这个叫条件概率的方法，这个也是对的，他们这两个条件的话，那一个PC一个px，我们假定这个c的判断是这个独立就是灰色x的话就是8kb，那么我们现在我们刚才已经得到了，那个在笔筒中出现灰色石头的概率是1/3，它的取值应该是什么呢？首先我们算一下这个p8Q币，这个刚才已经说了，是其分支，这PC就是pk它的概率呢就是，也是3/7在，c就是灰色石头，概率的条件下出现在笔筒中的概率是多少？在灰色石头的条件下，灰色石头排下来，就是只考虑石头，他出现在b桶中，总共亏了13块呢，有一次等于1/3，这里的很明显啊这里我们觉得结果呢，这种非常巧妙，这个px和ps这个值是相同的，都是1/3，这样的话我们就可以得出结论，我们最后的结果是1/3，通过这个公式的话，也是这个公式，我们会发现我们把这个在系统中出现和那个灰色石头的概率转换成了灰色石头出现在地图中的概率，这两个条件的互相做了一个颠倒，这个公式呢，我们后面就会用到，这是我们的核心，非常的简单
# 4.3使用条件概率来分类，提到了BS决策理论，要求计算量概率p1和p2，如果ps y大于ps属于内源，一，如果p二大于p11002，这两个准则并不是abs的角色里面的所有内容，CPU只是为了简化描述的是p，sy和PC20万，这个符号所代表的具体意义就是，假如给定一个sy所表示的数据点，那么一点是c一的概率是多少？该注意点什么CEO的概率又是多少？psy在c条件下是不一样的，不准则来交换概率中条件和结果，具体的，因为我也是准则得到PCci，这样我们可以得到这个区间内取号怎么取的就是，就是我说的是某个点，它是某种类别的朋概率是多少，就是条件就是五个点，然后呢？结果是他是哪个类别的？然后呢？我们以前的时候只是决定它是不是我们现在的话就求它的概率了，按照刚才BS准则的话，正好可以转换成为p在某种类别中出现这个点的概率，乘以这个类别的概率还有除以这个点等概率，这里有个问题，就是这个点的概率该怎么求我们接下来的话那主任注意一下，用这个定义的话，我们可以定义便是分子转换成为了什么呢？就是如果pc一在还是卖点的c的类别上，它的概率大于天天低价c2的概率，那我们就说它属于谁？学校我们可以通过三个一致，这样我们就可以利用BS准则的计算概率，已经分类代码，现在我们介绍完了这个BS的理论了，我们了解了这些理论，构建合理的方法，接下来我们要付诸实践了哦，他总共的原理就是这个BS的选择了你的话呢，他认为这个只是某个点它的概率还有五个类别的概率，还有在某个类别下出现这个点的概率，他认为这个点这三个字呢，都是确定的，都是可以计算的，那就可以，就要选择就可以迅速得到，这个店是某种类别的概率，那怎么计算五个点的概率和在某个类别中出现某个点的概率了？接下来就是我们要讲的4s
# 4.4使用朴素贝叶斯分类，应用分类这个味道的话，他比较特殊文档，比如说一个文件包含很多的，这次说句子他是怎么分类的的一个重要应用就是文档的自动分类，在文档分类中，整个文档就是实例，然后我们要把那个文档来判断一下这个文档属于哪种类型，这就是我们之前所说的那个点点就能到了，就是多给他点啊点这个文档他属于哪种类别的概率，就等于选择了就等于在这个类别，率乘以这个类别的概率图例，这个文档的概率，现在问题就是怎么求这三个概率？最多的邮件就是我们要处理的这个实力代理邮件，他是个不断增加的文本，但是我同样可以用，可以对于新闻报道用户留言这个功能的任意类型的文本进行分类中出现的词，把每个词的出现或不出现，都有一个特征，这样就得到一个特征数目，且会跟词汇表中的字母一样多，意思是上节介绍的培树ps扩展，适用于等到分类的做法，我们现在要用它来进行文档分类什么？每个词作为特征来判断它是否出现这样的特征，数目有多少呢？真正的是哪一种人的语言？估计不止一种语言，在英文中的单词总共是50万，阅读的话呢，至少需要几千个单词，就意味着我们现在的属性是50万，或者是几千，这个属性的值是零和一这样的一个文档，有这么大的话就表示怎么着，怎么着就是它属于这个类别了，我们来看一下朴素的一般过程，第一步，这个还是传统的方法，总共六部，收集，准备，分析，训练，测试和使用，收集就是得到数据，准备数据就能开始，就开始把数据读出来，转换成数据集合训练集了，这个数据的话，那是属于展示我们最终的效果，或者展示我们的数据效果，然后的训练数据，现在算法根据不同的特独立特征，打开其他普通的第23，这里要去的话，我没有得到鹏哥率，然后测算了一下我们错误率，我们要拿出一份数据集来作为判断是否成功这么一个结果，常见的便是应用，是个大分类，可以在任意的轮子里找你，能使用s367，而且那不一定非要使用文本，一千个单词，样本数为一千个实例，手写识别示例中的哪个数字有200两本儿？觉得数十里中的有24个样本之类呢，24个小时，有点少的话还可以，1200就好多了，网站地址中的有三个特征特征与统计学指导，如果每个特征需要n个样子，那么对于十个才能加，需要分成10个样本，对于包含一千个特征的词汇表将需要分成一千个样本，美术会随着它的数量增大而增大这个样本，要就是我们收集的一条实例吧，说每个特征需要安个样子，哪个特征需要n个样本，如果对于十个特征，有一千的样子，那么十个特征的话呢，就有按照特征来分的话，那就是有，3×10个样子，这里是指的十个样本，可能班车是这样的可能包含一千个特征的词汇量才需要，将有11000个样本可能加如果，好，我现在不考虑这个关联的，我们现在把所有的整个文档全部打散，就给你打成字，然后把所有的思绪也全部乱掉，我们就可以把这个，的，然后变成了一个由他使用的词组成的一个属性文档，各属性条目，这里要重点说一下，这个队有个概念叫独立，他指的是统计意义上的独立，第一个特征，或单词出现的可能性，与他和他的词之间没有关系，这个我肯定清楚，这是不对的，对不对？因为你想写的文章和你写的文章，他说第一场完全不一样，但有的字可能都是一样的，
# 好现在是那个，这学期实战第四章，第二次录音，好我们继续，上次课我们说到44，要使用朴素贝叶斯进行文档分类，然后讲了一下不是毕业诗，他的分类的过程，总共六个步骤，这里还介绍了一下我们要处理的，这次这个例子就是文档这个例子，它的特色就是我们尝试着把文档把它分成单词，然后能对应的字典中哪个单词作为一个属性，然后他存在就是一部存在，就是灵魂画师的画呢，给他增加了一个很大的属性，这次的这个时间特别大，这是一个一个非常好的例子，他说的一个问题就是假如我们认定此后时间的关系，我们不考虑，在不考虑的情况下，那么考虑对一个文档，那我们现在就可以尝试着对着那些处理，因为不考虑这一个，除了之间的关系，那这个门道就会变的非常的，嗯，概率就会变得非常小，就变得非常小，比如说我们这里哟，一千个样本，一千个很大，假如说我们现在语文大多只用了一千个单词让我们，实际上我们需要考虑的就是这一千个人有一千种出现这一千个单词属性的这么一个问题，这个例子比如说，我们说一个单词，这个单词就被坑就备考，悲伤的出现在l后面，鱼出现在被对手是后面的概率是相同的，当时我们知道这个假设并不正确，该矿实际上本身更合适和dns，然后呢，出现？lc这个词一起是朴素贝叶斯分类器中朴素这个词的含义，另一个假设就是每个课程都重要，这个也有问题，不同类型的，热门大出现某种词，他可能会比较关键，他是比较热门的词，关系肯定不一样了，一，名词和动词的意义是不同的，但是我们这里要价低，他们是相同的，痛的重要的，如果要看到你的留言是否得到那么重，可能不需要看网速的一千个单词，只需要看10到20个特征，就足以作出判断了，尽管上述的假设存在一些小的瑕疵，但是他的事业，但是实际效果还是可以的，我们已经了解了足够的知识，我们准备开始写代码了，这个知识就是我们现在给你那个点了，然后我们就那个点是某种类别的概率，然后这里呢，这个点我们也说了，就是用可以铺地的，是两个假设，然后把它用自己的方式了，然后来描述，然后在这里的话，我们要求的就是我说类它的概率，我点的概率以及，在某种内向，出现某个点的概率，只要有这三个，我们就可以求出我们想要的某个点是哪种类别的概率这个问题了？好，接下来的话呢，我们准备开始写代码了，4.5节，4.5的使用分类将成为本周获取特征的话呢，需要先拆分文本，具体怎么做呢？这里的特征来自于文本的词条ok文本的词条，那我就要逃开一个四条，那是字符的任意组合，一个词条可以想象为单词world也可以使用费单子撕掉，比如说16000，ip地址或任意的其他词不错，然后将每一个文本片段表示为一个词条量，就是每一个文本的片段表示为一个掏空组成的向量，徐州值为一，表示该词条中的闹钟，如果是临时调整，并未出现，以在线社区的留言板为例，为了不影响社区的发展，不需要屏蔽侮辱性的言论，向构建一个快速分类器，而某条言论使用负面或负面的词汇的，将该留言标志为内容不当，不过你过滤掉玻璃渣的内容是很常见的一个问题，这个问题需要建立两个类别，就是你师傅侮辱了别人，或者是没有不如别人，这里是由一和零来表示，接下来首先得将文本转换为数字向量的过程，然后再介绍如何接下来计算条件概率，在这基础上能够建立起，最后还有一项利用python实现朴素贝叶斯过程中需要考虑的问题哦，我下来的话有几个关键问题哈，就是你们大家可能不太熟悉的就是如何计算五个点的概率就是某个文档的概率，第二个如何计算？第三个如何计算在这个类别中出现，这什么概率能开始四点五点一准备数据，所有的那个系学习的不足啊，都十分钟就够的知识，中级准备分析，训练测试和使用收集数据之间文件我们这里的一般也使用的都是比较好的例子，嗯，我们都听过好了，所以说这个收集数据直接跳入水中，就是要转换成我们标准的格式，我的数据集的话呢，前面讲过的紧张的例子都是这样子的，就是要求你输入数据属性，然后输入得到一个相应的类别，有这么一个标准化的一个数据集，这样的话是我比较喜欢你在准备数据的话，那世界上就要把我们无论从哪里得到的数据转换成为这样的一个数据的过程，接下来就是四点五点一了，准备数据，从为美中构建词向量，我们把对看成单词向量和向量，你就说加句子转化为向量，考虑出现的每一个文档中出现的单词壁纸店交哪些词语词汇表或者说所要的词汇集合，然后必须要将每一篇文档转换为村上的一个向量开始四点py的这样的一个文件，然后把下面的程序停机两天了，我也住14-1所示的清单的这个是辞掉，先下载了一个转换书，我们这里写了一个地理，还是叫note，装载数据集，然后他返回的他这里有的人又变靓，就要post，就是那个poss，我们刚才说的留言板，留言板的列表，别把列表中的他是一个，列表这个列表中能包含了资料表中包含了一些词，1114条，比如说第一个包含的是my dog help help is，我的狗丢了，请帮忙，第二个是me not to dog park，不要把他带到公园去好不好？陈丹这个行业的侮辱性的词汇了哈，第三个词条的是my dear miss si love you这个词什么意思我不记得了啊，我都是非常可爱的，我爱他，第四个是stop this is it不要在那个发帖了，蠢蛋，这是没有价值的垃圾帖子好，nexus卖CDK，how to stopo，什么东西吃了我的什么东西，快阻止他，我下一个itby佛停止卖无价值的狗食物愚蠢的达到内容也少了两个文档，大概有七八个单词组成单词的话呢，七八个单词组成的话，哪个单词哪个组合？这是哪个文档？嗯，大概就这样子了，大概要好几千字啊，都可能在这里的话也只是一个poss，我只是一个就是这个年代，先进的词比较少，他只有加个退的话144个，然后呢这个新浪的话，144个字用自豪他给他吃的话就更少了，144个字组成的词，大概也就是最多70，很少，那我们就定了一个，调了一个叫play to这样的一个列表联系以前使用的是中国号，中考号类型，然后接下来的话再定一下，我们的就是标准的类别了，类别属性的定义了一个词叫classicplus，可能就是我们的类别，向量的意思，这两个向量的话让它包含的是一个列表，这里包含的值正好是六个里好吧，一和零一的话表示有悟性的文字，刚才我们注意到，那个xx明显就是侮辱性词汇，然后我在这里呢，还有一个是哪个stop， to be what is it这里你不要再那个发这个发帖了，蠢蛋这几天九点，最后一个就快答应what is a good job这三个字，三个词的话，20好像它属于一个一个帖子的一部分，返回，哦，这是第一个函数，这是装载数据集了，准备好11级了，还说的是叫亏我cut，是根据数据集转换成为相应的事项列表，我现在用的帖子了呢？我们现在要把整个所有的帖子的文档，然后转换成一个数据集，我们遇到的事其实不是全部的，因为你在这里的你很明显，这里是一个类似找狗的帖子，对每一个论坛，因此这里面只喝煮沸，有找过相关的一些内容，很少很少，只需要把我们自己在样本中出现的所有词组合成一个集合就行了，如何做这个集团呢？这个使用的方法就是定就可以了，然后定义好一个叫我看比赛的，这个我给你打的十足的一个集合，确定他为一个空集合，又晒的空气后，然后接下来的话，能再把那个所有的词都往里放了，可以把任意的一个列表类型转换成集合类型，他就没有次序列表是有次序的，还没有这个赛事没次序，而且没有重复项个一个你然后再和之前的我看个赛，然后做一个病，近期还将就可以了，这样得到一个新的集合，这话说的处理一遍，然后返回一下，最后返回一下就得集合，再行了一个list的类型，然后把那个积分转换成个列表，号召一下这个大夫，再定一个新的函数外，这是一个词，转换成向量，所以集合它的参数是我开过类似的和店铺size，最好是我们大概初一听的，我这还不是这句话，是我们搞了这么高的地儿，还是找汗出的结果就是我们的促销量列表叫此项集合生成列表，还有第二个是输入即可输入几个数字，明显就是我们要判断的那个的，他那个到了，啊你就是返回的销量，它等于零乘以内我形成了一个，嗯，包含多少个数的？包含多少个零的叫一个你好，然后我开个list，这两天就复制了一下这个我看的历史长度，然后他所有的值都是零，这样的一个集合给你几个？玩，某一个单词出现还是不出现了，因此就趁这个机会就离了，就是权力应该是每一个心情好，就是他那个，然后开始发呆，然后对于输入级中的每一个单词，如果work， is好奇看了一下，就是对于我们输入的新闻当中的每一个单词，如果每个单词，如果这个单词是在x，真的很好，然后我们就问这个向量，然后程潇的什么什么东西呢？就是应该出现了，我们就让他这这个词所在的值等于一，这次是多少呢？然后给我开个list，然后用这个此销量词，生成的列表，方法根据新的相同项，对应的事都要等到3.6导致的这个词就是字符串，然后它对应的，所以值是多少，然后都只获得相应的生存的，这个女太认可他的颜值，他都有一坨屎的话，我就可以得到一个新的一个现象了，s是什么呢？而not in my class玩儿然后就是直接返回下就说这个不在我这我就不处理了哦，他不在我就不处理了，不考虑那个了你，处理方法，简单的处理方法好的，的，给来是一个数据集的名字，这些留言本系列的词条集合，标点符号去掉，共同探讨文本处理的气息，返回的是第二个变量，是用来一个礼拜三节课就有两例的非物质性，最新版本的那边有人工标注这些信息为训练程序，以便自动检测侮辱性的留言，下一个函数的cable则会创建一个包含在文档中出现的不重复词的列表，使用了python的site数据类型，该那个词条列表输给这个赛道，还输三个月不重复的列表，首先这个我学过的这个大学不知道，首先得创建一个空集合，然后呢，每天傍晚返回的新磁极和天涯导致的集合中去，用于求两个集合的并集，然后呢，对这个符号就出现这个就可以定级了，按照we或托福在数学符号中的安非或操作，或者集合求并操作，使用相同的这个符号指向注意一下，获得这个词汇表后呢，便可以使用函数图y未曾为表未曾为表，即某个文档输出文档向量，每一个元素就是一过年更表示数据集中的单词在书中是否出现，首先创建一个与苏联等长的项链，然后把元素设置为零，然后中的所有单词若出现，则将输出的文档，电脑用的电池是唯一，就不需要检查某个词时，我还在list中操作执行效果，保存这个ps软件，然后再拍上提示符下输入，然后你opos之前的那个就是的，快哈，就是刚才的BS函数就可以了，然后我就得到了这个xx之后呢？嗯，好像是这个，嗯，这还说的话就会把我们的数据集转换成一个嗯，顺吉，嗯，就把我们把我们当初一起转换成我们想要的那个销量，嗯单词列表集合，然后就可以给我看list，然后叫之前的那个文档里的poss，我看please，这就是我们想我们得到的结果，结果就是一个由所有的文档出现的词，组成的集合转换成的列表，这是我看过类似的，然后是个不重复的一个杰克，而且本质上它应该是按照相应的一个，嗯，条件进行了一个排序啊，发现不会出现重复的词，这个表的话并没有排序，需要的话可以进行排序，顺便再看一下函数cf，他肯定，它就可以把一个日本有很大转换成相应的一个列表，使用的是徽标，或者要检查的单词，中文输入，然后为每一个单词构建一个特征，给另一个文档，该文档就可以对照检查，检查一下这个函数的有效性，这个vocal list中所以为二的元素是个什么单词单词help，刚才睡觉的0120222号2号左右，二你明珠出现，我们的，你几天能到出去的啊0，123456六他第三啊，出现这个倒数第六个字的话，那就很可能是一个步入新的文档，我们看一下top3，对stop to talk正好是第四个检查的单词书，然后被某一个单词固定，一个特征，一段比另一篇文档那样，家里检查一个x等于20元，40个单词英语单词给他检查一下是否他在出现的第四个闹钟，好，这就是我呢，嗯，四点五点一，这三个函数啊，他的你属性我的是是否出现那个特征的都没到，不信了，然后呢？别的话我们也知道了.
# 四点五点二7.38，低谷男士得到数据，第二个就是准备数据，现在把数据都准备好了，然后呢，就是标准的我们的属性相类比这种方式了，那么接下来的话就开始训练了，现在数据，他的目的就是，我看了一下我们这个数据能不能进行分类，怎么好的进行分类？我们现在采用的算法呢，就是之前讲的不也是这个方法，我们刚刚介绍的是，将一组单词转换成每一组数字，接下来的发展将把这个数字的计算概率，现在我们知道了一个词出现在一天当中是是和否的这样的一个问题了，也知道这个文档所属的类别了，我们之前讲到毕业时选择我们把那个，轮到，这个号呢，我们尝试按照BS准则，然后来看一下怎么求，有很大，在这里别想出现这个人大，然后再乘于这个电源的概率，再除以这个文档的概率，这里呢，我们开始终于出现这个关键问题了，就是我们家的这三个是怎么计算的？按照上面的公式的话呢，每个内页计算开始，然后比较两个概率值的大小如何计算呢？首先我们可以通过类别，文档数，去除以总数来计算一下概率，PC这个简单就是爱那个某种类别的概率，这就是两种类别的一种是侮辱性的要求，非勿处的，除以总人大，这个很这个很容易做，我们现在总共六个文档，乌罗费乌鲁的话，隔两三个站都是3/6，张倩来我们在算的就是在某一个叫批，大部分在这个世上出现，我们的文档不干，这也是假设，如果将这个文档展开为一个独立课程，那么就可以将上述概率写作为，单词概率的独立性，如果我们就可以使用单词的成绩，那这个门道上个月派出在某种类别下出现这个文档，下这个文档中的单词的概率的成绩，多种方式的话，我们就可以大大的简化一下我们的计算过程，是这样子的，街上哪个女的都没大的数目，嗯这个简单玉米片七点能到，对于每一个类别，如果词条出现的那种，的技术支持，然后剩下所有的技术指标，那边，它的数目除以总词条数目，如何得到它的概率，然后返回每个类别的条件概率，干嘛呢？我们在这个ps文件中我们这里要使用的ip外，因此我们首先要装大pos信号一句添加到这个PSP外的最前面，然后接电话呢，我刚开始写这个程序清单，4:20力气的训练函数，这里要定一个教训，陈碧玲叫你还书，这个恩的是哪一朴素的，单纯的b是贝斯，是，一下，叫春，这个是训练的矩阵，那个是这个群鬼训练类别，分别表示，这是我们之间经常说的类别向量就是一个x，然后ok，刚才我下，然后呢？这个样子，第一行代码是那么拼到这个变量，num， lock看一下我们训练及有多少个文档，这就是认一下，然后出x就可以了一个链表吗？表示说这个类的话，这个大儿子的话呢，就是炼丹次数这样穿的，然后扔出去，能，这里有个问题还是个人吹么，意思就是说要求每个文档中出现的单词数是一致的啊，这个问题肯定是要把事情处理了，然后在这里会得到一下，我们的txt，就是第一个啊，第一个文档文档的，它的长度是第一个文档，它长度值呢，这样就可以算为这个number，这是每一个班多少个词条的数目，下面再订一个叫pps，然后我这个ps表示不行的吧，p的概率，然后的概率等什么呢？尚春伟就训练累点，呵呵，厨艺那都还那个类别，这样的话吹了个大屁，在我这里是3/6，然后在ip林娜这批里那么多的意思就是嗯，嗯，pig在这里我还不确定这个领导是这个是565，是男人侮辱性的，反正这个批评这种类别的，嗯送你干什么呢，number二，这是我们的一个组成，就是一个轮到龙包含的词的数目，然后直接用单数，这样的话，床上呆着，嗯，汉城零也是，您就好了呢，是什么呢，啊你的电脑电脑，然后下面有个屁电脑，然后全都是为零，还不知道什么意思，应该是零和一的概率设立是指，然后find love drops整个文档的数目开始了，这个应该是取文档，那就直接使用就可以了，太，如果春晚，如果先判断一下，这是一个典型的一个文档的话，就是个屁皮囊，听他们的欢乐之家，x，得吃你的，的屁哦你这批，结果tm他是一个在鲁南mall的话就是文档长度，因此他得到一个全一个文档长度，哪个全名或者用那常用的一个权利，然后的话加个菜文档在这里的话，我们都是经过处理的，一召唤的一家对应纸相架，然后去个屁滴闹，他也是家等你，然后散了吹伞的事，训练集和然后呆萌叮当500780现在取所有的，你就出现的在在word文档中所有单词出现的个数，让我们得到一个，新的睡个屁中我，然后，暑假要统计每个词出现的数目归事相应的这个霹雳，那也是做了同样的事情，乖乖的哈，都可以得到这个东西哦，这里有个区别，p第二个视频那，然后就开始叫我们全做完一遍就可以得到，虽无韵，一个屁那日批那拍一个p0，你那还有个屁分别代表一个销量对象的事，雪中词出现的毒素，然后呢？听到的是不同香料，不同的离别中，然后出现一的倒数这几个字是吧，好像差不多，电影个屁的文档的一个概率等于什么？拼的是现在这个销量，谢谢，是一个门道能到的项链，然后去除这个ppt那这号码就可以得到你个词，你的词出现的总次数的频率哦，这个频率的pk，这是哪个词的频率，尼克斯出现的频率，在某个类别中出现某个单词的频率，让我们下步之后就可以得到一个霹雳，那么推荐的评级弄哦，原来这样子，刚才讲到了我们算这个零五要求，这个要求每个人都是独立的，你可以把那个球一定能到的概率，就变成了求一个单词的概率，我们这里修出来了就是这个单词出现，然后在作文当中的次数，这不是总人，到了团队是所有的文档，有单词出现的频率，一w一样子，好吃个屁，这样就得到了，然后返回这个pizza和pizza，这就是分别的相应的我们的频率对象量，但此前一样，然后那个ps又px呢？这是那个训练类别这种，这是侮辱性的文档的数目，出一个我们的总数，这个是那个，这个本应该是那个皮恩，PC和PC，PC PC PC相应的p0c一点就可以了，差点走到哪里了，好笑的话分子解决了，解决了我的话，我是每个单词的，三次的频率，那就可以让这个单词注意这个，这就不用分类了，开出总数就行了，总数就是那个批点，加上瓶盖么？吃点速度速度的，中的输入参数就是文档的txt，以及由每天大力明天交钱所构成的向量群QQ，首先它是属于物理性的，nike SB的概率为p这是一个二类分类，分类问题，可以通过一件批多少批领队多个分类的营销代码修改ppi和除以c和pwrc需要初始化w快速连接程序中的分母变量是一个元素个数等于刺猬要大的那批外叔祖，在那个便利店及某个词语的对应词，对应的个数加一，然后在宿舍中的单词的总数也加一，我是总词数，对每个元素都除以该了一分钟的总次数，利用那匹马就很好的实现又一个露出一节课，若使用常规的排长列表这个任务哦，原来这里用到应用的南屏外，一个向量除以一个变量，出一个int类型，这个这个就以这方法，我就是一个烂屁娃儿这实现用一个数除以浮点数即可，若使用常规的拍散列表，在哪里完成这个任务，读者可以自己尝试一下，最后男孩只会返回两个变量的概率，加来实验一下，在陈奕迅8412中的代码添加到BS ps软件中，爱上胡夏输入让那批out你然后么sy，然后stop，ws，然后mike is talk english，你是hope那对，这次我们看见了一个注册列表，没看过cable，然后呢吹麦等一下flop，宾得k，please， oo，ok，这个list，oppo，这是我们的，嗯，现在列表，嗯睡了现在战绩x，然后的你的兔，我吃个饭头像亮着的，那只是个MAC office文档就可以把整个，嗯嗯大他的呢，零然后我的，先去挣，嗯，我，s，不信，然后，哦，这样子好看就可以了，来填充这个车卖掉属于哪个类别的销量70p，然后pk，分别是这个b to b，这样就直接可以得到相应的两个001类别的他们的销量现在绿了，一定要跟你商量，不知，然后这样的话呢一下多少？看到第六个屁，第二个失1234560.15，这只非常非常高的12345123我，喂，134561234520啊的条件下这单词这个瓶盖看是否正确，中的第一个字，那是cute，林中出现一次，而且力比一中难，从未出现南分别是这个，你在临沂零四哈林跟这款手机，肚皮疼，这是最能保证你的单词，问题，用这个得到的就该来进行分类测试算法可以根据实际现实情况来修改，分离器至四点五点三了测试成绩已获得文档，属于某个类别的概率个屁，www2等等，如果其中的概率为零的最好成绩是李飞的降低这种影响呢？这次的出现比较分明，八分二成绩的零呢，一次，是，然后能将分母除以二分母是？52，这个还不太清楚，打开PSP，外加bd30修改，然后拼命听完one of love to be number one smoks这个说得通的你天天在纳闷呢，她本来应该是所有词出现的呵，的，和而现在，速度，那是个问题，我们考虑一下，这是我们的第三次，谢谢大家，我，
# 你的话呢就意味着这个一是怎么解释呢，春天的树木至少适宜是这样子的，出现数目至少是一次，那出现一次的数目是多少呢？两次？然后他说还要二零中，他本来算的是所有所有出现的词的数目，二太少了，林志行担心闹钟可能不会出现，单词最多，那种可能全都是零，就这样子吧，失败有可能这样子提示下一出，由于太多很小的数相乘构成的，八，计算成绩的时候还太小，太小的时候他们成绩很想睡，床就会下溢出或得不到正确答案，我这还是个问题，我们可以用它长长是成很多小数，四舍五入得到的结果是零，这几个办法对于成绩取自然对数，就得重新取三个数呢？别成一b，等于一加乱bb，于是通过球队是哪几个避免下一出，或者是浮点数折路导致的错误，同时的存在，对处理不会有任何损失，了，对数太小了，结果取就可以解决，一，同时那层纱就是对处理都有两个损失，这里有个图484，他给出了x和x的曲线，在相同区域内同时增加或者减少，并且在相同点上取到极致，不同，但不影响结果哦，就可以把这个，系统就这个概率然后讲函数的简单就BS，这次搞伤了，是不是这样子的然后第一个kiss bye嗯，love， you电视可发一笔外币，他吃饭吃饭，这是向量，兔子理是道理是吧，销量转换成类，这什么意思，销量是这个意思吗？然后加一百，分别是那个什么就是那个我们的两个嗯词出现的概率的，闹完之后的商量，然后下来还有个p pass，这就是我们那个PC哦，PC w全都有了PC，wc全都有了没有，是的东西我，哦，这是要分类的项链，这里的销量明显，这是一个什么东西呢？这就是一个，轮到我们要判断他测试一下他是不是那种类型，哪种类型？然后我带你去啊，登上，然后mike，屁y这个，带图卡稀饭，要分类的销量是一个零一的，嗯，是个一，一组成的向量，一二组成的向量，然后乘以这个pp外壳，一外科，一外科，我们已经写好了，悟性文档中的词出现的频率成一个向量乘一个向量，什么意思？一个向量的销量位居相城，然后求和结果你皮卡司机了，漂亮，这什么意思？然后下来的话呢？如何如何啊，然后打pp是求和，然后也是相应的跟你商量个p0，然后沉吟道，一点去pk也没问题，如果p等于p0哇这个结果他们有三瓶酒的销量，然后得到了p货梯，大宇，难道他不考虑不考虑了？啊你？这两个故事中相同的可以样子好的我，函数，这是那个故事第二个，第二个的他的啊，然后有一个list，open， access，然后就开始叫那个卖wap，然后quit，这样话就可以把那个一个文档，然后转换成一个，嗯下面集合六点，然后就对你们这群卖车mx，然后呢？是现在把那个，嗯，nice，真的受的了这个文档，然后全部转换成集合，然后添加到，嗯，嫁到这个村里去，碧林，然后再把那个出卖，然后使用数字化转换，转换成数组哦的数字，然后，然后我带你去，这么快就得到几个和三个嗯字的那个，嗯，香的屁屁的屁屁，out了，在店里了，里面是love卖的吗？丹麦vs爱我的小狗狗，应该是这样子，上档次你等你，你兔然后卖，我看你，然后把这个case来看个例子v，我把你当成一个相应的，嗯像，嗯，这是一个数字，就是林一数字的，一二，然后你帮我看看是什么？下面是task，然后stop， it like thisitSB，你以为还有pp方便的话，我们可以看得出来啊，一，这两张是这个要分类的电量出case要清零零，这个吹牛你看一下哈，这不就是刚才那个骑单车的，我们使用的话呢，嗯，使用证好像那边，然后那个限定的事，我们回顾一下，他首先把这个矩阵转换成相应的，嗯，知道下一句跟这条数就能当个数，然后再得到，嗯，他的属性书，这单词数，然后下来的话能再直接用，然后用这个，我们要训练这个点，然后除以这个数，都喝出一点钟，的，嗯，我们的训练能到书，我，的你，像个律师的once，晚上的话就是我们说的那个，把数字把那个送给他了，死就是嗯嗯嗯呢，成，然后难不成嗯，把事情不处理，如果呢，等于放个屁，那就等于x，等一下哦，不带的你的我一下，但是不知道结果，俺会想你的的期待哦，我们通过这个程序都可以得到相应的概率，现在上概率了，然后叫人调一下带入到那个发生概率，还有我们要测试的那个大中，然后我们就可以得到我们想要的结果了，使用这个大批量的数字相乘的结果是什么意思？指的是元素相乘，就像两个月销量中的第一个元素相乘，然后将该值加到内存的对数据，最后比较类别的概率才会大概率，相应的类别标签不是很难哦，并刚才在忙，就是那个让我们测试的文档，文档就成为我们的pp外壳，几百块就已经是我们的新闻到了，单词出现的概率了，然后呢？我们再把这个数据乘那个，让我们的这个文档，这个数去一个什么结果啊，的商城，的，为何不给转换成头疼的，在将你的类别的，然后将该纸箱到类别的对手应该留下去，这条比较难懂啊，中午吃的对应值香香，然后把该局加大力度下去，然后比较累的概率返回，大概你的阴道内标签比较类别的概率，然后再返回打开对了，你多少钱干嘛对我来说是一个概率函数，叫congress潮州，以节省输入代码的时间哦，不知道哦，叔叔的一下结果对我是不？w的，然后成立PC的是，办公室，在身上出现多少了你出现的，哥和，一个向量乘向量，那就是得了，嗯的，呵呵！的什么？去不你，两个相加，商城，就是这个学校处理，一他的，的，出来，说，问题，是，嗯，是可以的，你不？你思考一下，如果结束了，你想来的话，准备数据轮到慈善国行，我们家每个词出现于否，做了一个特征，瓷器模型的3.55，二四楼，容易出现，不止一次得一位的盖茨出现在文档中所不能表达的愤怒信息，这个方法称为磁带模型，玩什么的在？每个单词可以出现多次在此句中的每个单词只能出现一次，考虑一下那个瓷砖的数目，就是光晒的话，就只考虑它是否出现，为了适应目前的话，需要对海树snow white进行修改图给出了模型的代码，to mike几乎完全相同的单词，而不是相对应的数值设为一，好办个what，m，他说他的参数类型，一个是我看的是列表此类的次的全，然后呢，我耳朵都疼，对于此事里面所有的词，然后看一下是否出现在这里面，就加一加一姑娘好了，邮件哦，这个是四点五点四的内容，我们修改一下这个pos贷模型，然后这样的话，我们现在一个词，它的值，32他有可能是1120号，现在可能是一和二呢，还是这个样子，在我们家附近来4.6提醒一个不呢，我的听歌，电视呢，1到4的话呢，主要是出于三个，还有一个是创建一个测试鸡吧，已经第二个可以让我看到类似的话，送你一个你的，我们是一级转换成了一个，他们是一级我们二货都能等，然后转换成一个集合列表，因为它是重复的这个site，再把那个我们得到了
# 4.6，这还是一个势力，要使用贝叶斯朴素贝叶斯来过滤垃圾邮件，是解决了一些现实生活中的问题，主要是从文本内容列表，然后再生成词向量，在这个例子中，我们将而作为一个电子邮件，垃圾过滤来看一下，是否能够解决这个问题，嫁了依然是通用的，我们绝不走第一步，收集数据，第二部准备数据，第三步分析数据，第四步训练法，第五步测试算法，第六步实用算法，底部的数据数据呢，这里要使用的是电子邮件的话，没有得到电子邮件的数据库，准备出去的话，同样的事，把它们转换成相应的词条向量，我们这边准备数据使用了三个函数在这里的话呢，可能要用一下，你现在不是这样的，日子中并没有分析，就没有展示数据。八上班来到我们的根基，嗯，然后我们使用我们的BS，然后来进行一个分类，最小的一个是否准确？修缮法，我们现在就准备要实用三房，什么算法呢？然后尝试者对文档进行分类，然后将其作为一个函数，该6.1准备数据的，在前一节介绍了如何创建词条，量着基于这些朴素贝叶斯分类的过程，在前一节中的材料是一些给定的，下面介绍的是从文本到文本文档中创建出自己的词列表，对一个文本字符串可以使用path类的，将它取名叫它划分，然后看看实际的运行效果，在干啥呢？我输入一下啊，就是不可以说他是不可能拍摄elleheart痛，然后直接使用sc的方法，然后就可以得到这个数字图词组成的一个一个list类型符号也被当成了词的一部分符号，这里可以使用正则表达式来区分，就是使用分隔符作为词数字之外的任意字符串，这里的阿姨就是那个好吧的，这什么意思呢，号词的列表是这个，然后我，然后，是这个有信号是什么呢？这个，这个是，是的是请好好的，最后一次是结尾吧，都是一次结尾的，他就把他给偷拍了，就应该把它识别出来，识别出来是这个样子，现在就可以得到一系列的词组成的，此表单里面的空字符串需要去掉，控制不住而需要去掉，二的长度大于0.2，哦这样子，脱口take， place，嗯，偷这个写法也是挺有趣的，它定义成一个变量的变量的话，能直接是那个这个list中的猿族，那就是元素，然后呢？后面加个QQ判断爱人top这个单词是大写的，如果目的是，就是查找有用，不还是出在中间还是结尾还是开头方法可以打游戏，比如说使用字符串的方法就可以达到目的，我们可以进行如下处理，拖个点漏，就这个了，还是说他因为top，然后就可以得到四个单，得到的人本就不要了，完整的电子邮件的实际处理结果，该数据集的存放在文件夹中，两个子文件夹m，等于pro6s然后呢s的，在露天市场的一种邮件，最需要注意的方案，由于这里有个l，ml然后问候一声，o等于0，嗯，然后安的office等于174623的一部分，因此会出现一个会ps的单词，当队员有一个划分的时候，你会得到很多的时候，我们想要去掉这些单词，因此在实际中会过滤掉长度小于三的字符串，ok，等你生了一个通俗的文本解析规则来实现这一点，在设计过程中的需要用更高级的管理起来，对诸如ak6号又要进行处理，目前一个月二岁中会缺席成为词汇表中的单词，比如点wap.com，解析，可能是一个相当复杂的过程，简单的函数也可以根据情况进行修改
# 四点六点二测试算法使用朴素，贝叶斯进行交叉验证，下面的江伦敦及其他，集成到一个完整的体系中去打开文件分析系统则将下面的程序，其他的代码证加到这个PSP的文件中去，这程序清单四高五的内容，我们现在要使用他的号，第一个test pass我们分析他然后倒入这个阿姨，然后呢，it对于it，谁用的这个杯子，然后这次他话费的时候呢，他第一个参数是对的，我们的20个w信号不好，这里的他注意到这里，他使用的是一个加了一个二，这一段是取消转一次的意思取消那个，嗯，都穿着短衣服的意思，嗯，因为这里有一个斜杠w我们这些高的话就是买衣服，他家老二之后，他就不需要再写这双鞋高这话一个是以我的结尾办公室，然后pick up late night，嗯，对于这个情况的话，我们就可以得到一个，嗯，所有的大于二的消息，这样的一个本本的自传，然后定下一个大pos，就是病毒，病毒和垃圾邮件test这个函数了，这就是一个叫什么的，就是测试函数，嗯，可方便还书吗？然后第一个第一行代码，第一个doctor，ws的意思是一个列表，然后cosplay的队形列表，然后feat，打枪的，这都是个例子，然后爱赛尔号开始循环和锐志126126226这什么意思？号126260345吗？来看一下吧，然后what，what是什么呢？test， test他QQ说，他要打一个，转换成为，词列表点来看一下第的哦这样子哦的，打开一个文件夹下的文件，文件的话两套这里使用了一个套子里的人，为什么是126呢？是因为他的8月份本名啊，本名就是126，脱口而出的话，那就给打开了打开之后的文件，然后点锐的，好了，就可以打开一个文件，然后再通过这台4s店把它转换成资料，就得到一个list好，然后得到之后呢，然后进行处理，然后呢把文本列表s，我说的是doctor一下，好像是的，的清楚，然后把这个加进来，估计他要娶一个集了，然后kiss，然后继续kiss一日志里的，他娶的是这个疼啊，然后继续what，然后这里要再去从汉墓里面走，还没有正常的邮件吧，然后我们看着，然后这里肯定是最后那副太子爷家了，最后的840499360，不知合适的话，我们就可以把所有的文件，然后病毒和那个相应的正常文件全部导入了，因为它们都放到家中，我们这里的就是正常的，就知道它们的分类，这样的话卡斯特做出来了都，帮我找下，读完之后的数据处理完了，继续玩下去，我开个list，我看breast，这里是我们的慈善的列表，这里我们直接使用那个可以透过case，我们之前定好的函数把这个我们的doctor，转换一下我们的词下载列表最好，这里这个慈善的列表就是取消重复的，此之后，然后这个春色的，然后在第一个case就是个训练基地，现在觉得有什么的古诗，50就是这种事可是一到五十零到49，还不知道什么用处，然后test是空的，我不爱跟你对质，一个是从领导是从0到9，然后开始循环，然后就认定一个随机的说一句随机的摄影师，哦，他随机取值，从区局，然后做增量部分，一会又来做训练，你不用来做测试，嗯tm的flame听铃声，春季赛的就是训练机，那就是长度，知道与否，随即指给玉凤这个随机的故事，规格规格，然后从零开始零是训练机，训练器去训练，其他给了一个是不是？月租50，就从这个0到50中，然后取一个随机数，然后做了一个x，随即直的，所以值这个对恩，然后继续kiss，然后得到一个测试及测试方法，然后把这个翠绿色的，x把这个训练机中的索引值，然后添加到这个测试机里面去，然后delete，然后吹牛，然后这个男的应该，然后再把这个训练集中的这个数，所以只按删掉账号就可以得到一个，这是50个数中，除了十个数那个两个鸡，一个是这个test下面的这个大队出色的是一个数字化，就是索引号是哪一个列表列表给我下了这个车，迈腾迈腾，这就是一个训练矩阵，这是我们的训练，我们现在已经得到了，这个才是，我们要把那个真正的这个文档和累以后的车开来，这样我就可以放心还了，如果这个，如果是在测试集中的所有的所有，那这个忒慢了一下，这个函数叫seven two week，这个函数的作用呢，就是把那个我们的命运，把我们的，嗯，对就是那个字，就把我们的一个新的措施的一个，嗯，ws这里就是我们的人，一个文件一个文档，然后呢转换成相应的向量啊，这里呢，可以看到第一个参数就是这个，我看please，我们之前得到的那个，这样的，我应该我都笑了啊，然后呢这个抖s然后他才说是doctor x，这是我们在训练集中的这个文件取出来，然后把它转换成相应的，嗯，相应的数字销量，然后听到这个吹mic，然后这个卡现在也同样是缘分的，然后把caster，把case里面的这个到北京34号寄出来一下就是丢了我们的青春，它的背上有两个，第一个是我们的训练机，我们的训练器数字取证，然后第二个是我们的类列表，这里都要使用二维数组，然后来把它组装起来，这样我们都得到之后呢，就开始用这个车nb了，蜕变之后就可以求出那个，然而不同类别的以及我们的，然后类别的那个销量概率及，我们的病毒邮件就像概率，ok，那定一个错误错误数，这时候就开始准备测试了s，对于，嗯，所以这是啊，然后开始其他的值，然后可以把这个black list他动的是我的那个收音机哦，x，这个数据下载速度能到一个一个一个what，嗯，之后呢，可以判断了，如果刚开始带bb，这个很容易玩的开，是个what，放屁，PS2个都带去推迟若不等于3xx，那我们就说这个l号的就加一了，不说话呢，然后最后的话打印一下错误率是多少？这个错误数除以像我们的总共的那个case的数，这样我们就可以得出第一个大写为的，谢谢您的自动化处理的文件销量一个是几个月训练机，都是随机选出的，本周共有506000多选择为测试集分类精选辑中的文档来完成吹牛，我们从随机数中选出十个文件，选择出的数字，对应的人大量的测试及录取，同时也从七点就被踢出，这种随机选择数据的一部分面积作为测试，这回老子cos你的表的这次在吹牛比零还是多用计算分类所需要的概率，然后的遍历测试，及对其中每封电子邮件进行分类，如果邮件分类错误的错误，加医疗的错误数的百分比，现在对上证经常是，我们怎么接下来的话呢？就需要使用这样的代码来做，第一个掉那个BS啊，直接叫他然后出了树林，是什么开始在掉一次，然后我们这里可以说可以得到一个分类错误吧，说这个home basic english我给你听w and kiss you keep anlove you as you lovetest name，就stop and life，l is点一，因此出现一个错误，0.1输出在石峰随机选择的里面的分类错误率，然后这些邮件是随机选择的，结果没有差别的话，还是会给出错误分到的资料，这个错误，如果想更好的估计错误率，那么就应该是上述过程重复多次，比做十次，然后求平均值，我这么做了一下后出现的错误就是将垃圾邮件误判为正常，相比之下邮件要比这边好，错误的有多种形式来进行修正，分类器讨论，目前我们已经使用了case进行分类，接下来的话就是他的另一个应用，下个月才会展示，如何解释，不是佩森一起训练得到的知识，好吧，我们使用的是这个葡萄ps来进行那个垃圾邮件的测试，这里我们写两个函数的函数是叫cass，这里只是把文本转换成一个大文本，转换成字符串出租车的那份表，这里他主要是处理了一下，还是用的那个轴的表达式，把那一些一些一些自己不想要的数据进行清洗啊，你说字符小于两个的，这个一般表示特殊符号，对于要做一个应用之类的话，这样的坚持，我饿着，还有一个就是这个test，这是主函数了，今晚的话题就是我们首先要创建我们的数据，就是收集收集数据的数据的话，这个过程的话呢，这里直接使用的是这个，嗯方法打开文件，然后使用就可以得到一个字符串，然后之后呢，然后使用这个之前我们定好的cast，就可以把这个整个文本，然后转换成我们清洗过之后的一个词列表，吃吃那个吃得了，然后再把这个策略倒呢方法，然后变成一个矩阵，变成一个一个一个矩阵，然后呢？接下来的话再把我们的那个方法得到全部的词，然后再把我们的case也得到了，然后得到之后呢，这是第一部，第一部，第二部的话就是我们要精英今天那个飞机了，这个是衣服洗完了啊，这样的话下一步就是使用这个，好what time， is it，要把我们的文本然后处理，把我刚才得到的这个，嗯，这个矩阵矩阵，然后能转化成为我们想要的这个，嗯，磁县列表，此项列表，因为这个里面有重复的代码，重复的去掉还能集合吗？然后再往下的话，那就开始做一个，把我的数据在进一步处理了，我们现在收集的话，你就说现在有50个文件，犹如50个门诊，如果是文本的话，那我们现在就需要，嗯，从0到50，然后随机取区分一下区分的时候是这么区分的，然后其中首先取林老师，然后呢？把他们叼紧随机的值来1%的值的话呢，然后作为添加到什么车上有个test，谁能娶到领导029然后，然后得到一个随机的值，都要，一直都是一个孙燕姿最大生命值的话，能再把我们这个值的话能贴到一个test的领取，然后再把我们的训练赛中的这个，所以只敢再删掉，这样我就知道两个一个是训练机，然后一个是十个测试机，这话应该是40个，七年级十个三十几，然后接下来就把这个我的收音机，嗯，再送一下所有的春运证，然后把每篇文档的话都是用那个我们想要的那个用了，现在接下来的话要使用我们的方法的话，必须要得到一个，嗯数据黑哥类的列表，我列表好好的，这样来做，使用这个，然后再到work的方法，这个函数的话呢，他把我们的每一个文档，根据我们的case，我看的list，然后进行了一段，处理，然后你得到几个我们的车卖了，累的话也是一样的，得到相应的列表，然后这样的话我们就使用我们的车，一方法就会得到我们的，嗯，三个概率等我上个月花了，我们家来在说我们的咖啡分地方吧，这边我是个函数，第一个参数就是我们要测试的那个测试等功能的这个词，原本的话也要使用那个什么，要是用舌头外吐奶的方法，我先把它转换成数字的，然后呢，带你去之后就可以得到一个判断一下是不是指定好的测试类，要出错率哦，这个方法就是我们今天讲的，这就是使用ps进行邮件的调查验证概念，这个要知道，
from numpy import *


def loadDataSet(
):  #load a data set. it conclude a variable named postinglist. posting is a needed something. list ia a type including some string.
    postinglist = [
        ['my', 'dog', 'has', 'flea', 'problem', 'help',
         'please'],  #my dog has flea, this iss a problem ,please help me.
        ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park',
         'stupid'],  #maybe do not take him to find dog in park ,this is stupid
        ['my', 'dalmation', 'is', 'so', 'cute', 'I', ';love',
         'him'],  # my dalmation is so cute, i love him
        [
            'stop', 'posting', 'stupid', 'worthless', 'garbage'
        ],  # Stop posting , this is stupid, it is worthless and you are garbage
        ['mr', 'lickes', 'ate', 'my', 'steak', 'how', 'to', 'stop',
         'him'],  #mr lickes, ate my steak, how to stop him
        ['quit', 'buying', 'worthless', 'do', 'food', 'stupid'
         ]  #quit buying , it is worthless to do the stupid thing. food.
    ]
    classVec = [0, 1, 0, 1, 0,
                1]  # According to the postinglist ,this is the class Vectory

    return postinglist, classVec


def createVocabList(
        dataSet
):  # create the vocability list. The data Set will be splited to teh vocability.
    vocabSet = set([])  # define the vocab set as a null list
    for document in dataSet:  #for any document in dataset
        vocabSet = vocabSet | set(
            document)  # let vocabset include document or others.
    return list(vocabSet)  #??


def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1  # this place is so smart. word is a string. index(word) is a int. returnVec(index) is the object
        else:
            print 'the wrod: %s is not in  my Vocabulary!' % word
    return returnVec


# 4.5.2 training algorithm: from word vector to compute the p.

def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = zeros(numWords)
    p1Num = zeros(numWords)
    p0Denom = 0.0
    p1Denom = 0.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = p1Num/p1Denom
    p0Vect = p0Num/p0Denom
    return p0Vect,p1Vect,pAbusive 
    


#4-3
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def testingNB():
    listOPosts, listClasses = loadDataSet()

    myVocabList = createVocabList(listOPosts)

    trainMat = []

    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V, p1V, pAb = trainNB0(array(trainMat), array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry, 'classified  as : ', classifyNB(thisDoc, p0V, p1V, pAb)
    testEntry = ['a','stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry, 'classified as:', classifyNB(thisDoc, p0V, p1V, pAb)



def textParse(bigString):
    import re
    listOfTokens = re.split(r'\w*',bigString)
    return [tok.lower() for tok in listOfTokens if len(tok)>2]
def spamTest():
    docList = []
    classList = []
    fullText = []

    for i in range(1,26):
        wordList = textParse(open('D:\\Users\\gao\\Documents\\Code\\python\\digits\\email\\spam\\%d.txt' % i).read())
        docList.append(wordList) 
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('D:\\Users\\gao\\Documents\\Code\\python\\digits\\email\\ham\\%d.txt' % i).read())
        docList.append(wordList) 
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)
    trainingSet = range(50)
    testSet = []
    for i in range(10):
        randIndex = int(random.uniform(0,len(trainingSet))) 
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainingMat = []
    trainingClasses = []
    for docIndex in trainingSet:
        trainingMat.append(setOfWords2Vec(vocabList,docList[docIndex]))
        trainingClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNB0(array(trainingMat),array(trainingClasses))
    errorCount = 0
    for docIndex in testSet:
        wordVector = setOfWords2Vec(vocabList,docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
    print 'the error rate is : ', float(errorCount)/len(testSet)

