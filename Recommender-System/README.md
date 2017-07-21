# 推荐系统

#### 推荐系统处理的对象

* 用户: 用户特征
* 物品: 物品特征
* 用户对物品的偏好

#### 推荐场景

* 城市(本地/旅游)
* 位置(距离远近)

#### 推荐方法

* 基于人口统计学的推荐(Demographic-Based Recommendation)
* 基于内容的推荐(Content-Based Recommendation)
* 协同过滤推荐(Collaborative Filtering Recommendation)
    * 基于用户的协同过滤推荐(User-Based Collaborative Filtering Recommendation): UserCF
    * 基于物品的协同过滤推荐(Item-Based Collaborative Filtering Recommendation): ItemCF
* 基于模型的推荐(Model-Based Recommendation)

#### 推荐方法对比

* 基于人口统计学的推荐(只考虑用户)

    1. 用户特征 - 用户相似度
    2. 用户 - 相似用户 -  历史偏好物品

* 基于内容的推荐(只考虑物品)

    1. 物品特征 - 物品相似度
    2. 用户 - 历史偏好物品 - 相似物品

* 基于用户的协同过滤推荐(用户对物品的偏好)

    1. 二维矩阵(用户-物品-偏好) - 用户相似度
    2. 用户 - 相似用户 -  历史偏好物品(个性化推荐)

* 基于物品的协同过滤推荐(用户对物品的偏好)

    1. 二维矩阵(用户-物品-偏好) - 物品相似度
    2. 用户 - 历史偏好物品 - 相似物品(个性化推荐)
    3. 物品 - 相似物品(物品推荐)

* 基于模型的推荐

    1. 用户 - 历史样本(物品-偏好) - 训练模型
    2. 物品 - 训练好的模型 - 偏好

#### 用户对物品的偏好特征

* 浏览: 布尔, 0/1
* 评分: 数值, 1~5
* 收藏: 布尔, 0/1
* 分享: 布尔, 0/1
* 顶: 布尔, 0/1
* 踩: 布尔, 0/1
* 点击(头图、导航、电话、点评、推荐菜): 布尔, 0/1

#### 偏好特征推荐处理

* 分组处理
* 加权处理

#### 相似度计算

* 同现相似度

* 欧几里得距离(Euclidean Distance)

<div align="center"><img src="http://latex.codecogs.com/svg.latex?d(x,y)=\sqrt{\sum_{i=1}^{n}(x_{i}-y_{i})^{2}}" /></a></div>

欧几里得距离越小，相似度越大

<div align="center"><img src="http://latex.codecogs.com/svg.latex?sim(x,y)=\frac{1}{1&plus;d(x,y)}" /></div>

* 杰卡德系数(Jaccard Index)

<div align="center"><img src="http://latex.codecogs.com/svg.latex?J(A,B)=\frac{\left&space;|&space;A\cap&space;B&space;\right&space;|}{\left&space;|&space;A\cup&space;B&space;\right&space;|}=\frac{\left&space;|&space;A\cap&space;B&space;\right&space;|}{\left&space;|&space;A&space;\right&space;|&plus;\left&space;|&space;B&space;\right&space;|-\left&space;|&space;A\cap&space;B&space;\right&space;|}" /></a></div>

* 皮尔逊相关系数(Pearson Correlation Coefficient)

<div align="center"><img src="http://latex.codecogs.com/svg.latex?P(x,y)=\frac{\sum&space;x_{i}y_{i}-n\bar{x}\bar{y}}{\sqrt{\sum&space;x_{i}^2-n\bar{x}^2}\sqrt{\sum&space;y_{i}^2-n\bar{y}^2}}" /></a></div>

* 余弦相似度(Cosine Similarity)

<div align="center"><img src="http://latex.codecogs.com/svg.latex?T(x,y)=\frac{\sum&space;x_{i}y{i}}{\sqrt{\sum&space;x_{i}^{2}}\sqrt{\sum&space;y_{i}^{2}}}" /></a></div>

#### 相似度计算复杂度

* UserCF: 用户越多, 复杂度越大
* ItemCF: 物品越多, 复杂度越大

#### 召回(候选集生成)

* UserCF: 用户 - 相似用户 -  历史偏好物品
* ItemCF: 用户 - 历史偏好物品 - 相似物品

#### 用户对物品的偏好预测

* UserCF: 用户相似度w * 用户对物品的偏好s
* ItemCF: 用户对物品的偏好s * 物品相似度w

<div align="center"><img src="http://latex.codecogs.com/svg.latex?P=\sum&space;w_{i}s_{j}" /></a></div>

#### Top-N推荐

#### 推荐系统评测指标

#### 参考

* [一个 RNN 调研引发的点评推荐血案](https://www.qcloud.com/community/article/826536)
* [个性推荐理论与实践](https://www.qcloud.com/community/article/383583)
* [Deep Neural Networks for YouTube Recommendation](http://www.jianshu.com/p/c5b8268d273b)
* [Youtube 短视频推荐系统变迁](https://www.qcloud.com/community/article/989677)
* [个性化推荐系统从0到1](https://www.qcloud.com/community/article/850053)
* [美团点评 - 旅游推荐系统的演进](https://tech.meituan.com/travel-recsys.html)
* [美团点评 - 外卖O2O的用户画像实践](https://tech.meituan.com/waimai-ups.html)
* [外卖排序系统特征生产框架](https://tech.meituan.com/feature_pipeline.html)
* [协同过滤和基于内容推荐有什么区别](https://www.zhihu.com/question/19971859)
* [推荐引擎初探](https://www.ibm.com/developerworks/cn/web/1103_zhaoct_recommstudy1/index.html)
* [深入推荐引擎相关算法 - 协同过滤](https://www.ibm.com/developerworks/cn/web/1103_zhaoct_recommstudy2/index.html)
* [深入推荐引擎相关算法 - 聚类](https://www.ibm.com/developerworks/cn/web/1103_zhaoct_recommstudy3/index.html)
* [推荐系统不相信眼泪](http://iyao.ren/2017/02/28/itemcf/)
* [协同过滤推荐算法的原理及实现](http://blog.csdn.net/yimingsilence/article/details/54934302)
* [基于Map Reduce的协同过滤推荐算法的并行实现](http://www.doc88.com/p-0774360741317.html)
