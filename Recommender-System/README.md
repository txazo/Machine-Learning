# 推荐系统

#### 推荐过程

* 用户推荐位的曝光和点击行为上报离线系统
* 训练样本集(Item的曝光和点击 + Item特征 + 用户特征) - 训练算法

* 餐厅库 -> 候选集生成 -> 排序 -> 推荐展示给用户

#### 特征提取

用户特征: 

餐厅特征: 名称、位置、菜系、推荐菜、星级、标签、均价、评分

点评特征: 评分、评论、口味、环境、服务

#### 协同过滤

KNN查找相似用户

#### 文本处理

文本 -> 词向量

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
