# 推荐系统

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
    2. 用户 - 相似用户 -  相似用户的物品

* 基于内容的推荐(只考虑物品)

    1. 物品特征 - 物品相似度
    2. 用户 - 历史物品 - 相似物品

* 基于用户的协同过滤推荐(用户对物品的偏好)

    1. 矩阵(用户-物品-偏好) - 用户相似度
    2. 用户 - 相似用户 -  历史偏好物品

* 基于物品的协同过滤推荐(用户对物品的偏好)

    1. 矩阵(用户-物品-偏好) - 物品相似度
    2. 用户 - 历史偏好物品 - 相似物品

* 基于模型的推荐

    1. 用户 - 样本(物品-偏好) - 训练模型
    2. 物品 - 训练好的模型 - 偏好

#### 用户对物品的偏好

* 浏览: 布尔, 0/1
* 评分: 数值, 1-5
* 收藏: 布尔, 0/1
* 分享: 布尔, 0/1
* 顶: 布尔, 0/1
* 踩: 布尔, 0/1
* 点击(头图、点评): 布尔, 0/1

#### 推荐处理

* 分组处理
* 加权处理

#### 相似度计算

* 欧几里德距离

<div align="center"><img src="http://latex.codecogs.com/svg.latex?d(x,y)=\sqrt{\sum_{i=1}^{n}(x_{i}-y_{i})^{2}}" /></a></div>

* 皮尔逊相关系数

<div align="center"></div>

#### 召回(候选集生成)

* UserCF: 用户 - 相似用户 -  历史偏好物品
* ItemCF: 用户 - 历史偏好物品 - 相似物品

#### 用户对物品的偏好预测

* UserCF: 用户相似度w * 用户对物品的偏好s
* ItemCF: 用户对物品的偏好s * 物品相似度w

<div align="center"><img src="http://latex.codecogs.com/svg.latex?P=\sum&space;w_{i}s_{j}" /></a></div>

#### 计算复杂度

* UserCF: 用户越多, 复杂度越大
* ItemCF: 物品越多, 复杂度越大

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
