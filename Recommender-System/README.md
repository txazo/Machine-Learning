# 推荐系统

#### 推荐方法

* 协同过滤推荐(Collaborative Filtering Recommendation)
    * User-Based(UserCF): 基于用户的协同过滤推荐
    * Item-Based(ItemCF): 基于物品的协同过滤推荐
* 基于内容的推荐(Content-Based Recommendation)

#### 推荐方法对比

* 基于用户的协同过滤推荐
    * User相似度 -> 相似User -> 相似User的Item
* 基于物品的协同过滤推荐
    * User的Item -> Item统计相似度 -> 其它相似Item
* 基于内容的推荐
    * 不考虑User
    * User的Item -> Item内容相似度 -> 其它相似Item

#### 推荐过程

* 用户推荐位的曝光和点击行为上报离线系统
* 训练样本集(Item的曝光和点击 + Item特征 + 用户特征) - 训练算法

* 餐厅库 -> 候选集生成 -> 排序 -> 推荐展示给用户

* 召回: 候选集生成
* 排序

#### 特征提取

用户特征: 历史行为

餐厅特征: 名称、位置、菜系、推荐菜、星级、标签、均价、评分

点评特征: 评分、评论、口味、环境、服务

#### 协同过滤

* KNN算法
* 相似度算法
* User-Based算法: 用户相似度 -> 相似用户集
* Item-Based算法: Item相似度 -> 每个Item的相似集
* 用户历史行为(用户 + 相似用户集) -> Item集 -> Item候选集
* Top-N推荐: Item候选集 -> 排序 -> Item推荐集
* 相似命中率: Item集切分为训练集和测试集 -> Item推荐集和测试集计算相似命中率

* 用户行为 -> 用户偏好

* 数据处理: 减噪、归一化

#### 文本处理

文本 -> 词向量

#### 语料库

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
* [深入推荐引擎相关算法 - 协同过滤](https://www.ibm.com/developerworks/cn/web/1103_zhaoct_recommstudy2/)
* [协同过滤和基于内容推荐有什么区别](https://www.zhihu.com/question/19971859)
* [推荐引擎初探](https://www.ibm.com/developerworks/cn/web/1103_zhaoct_recommstudy1/index.html)
* [深入推荐引擎相关算法 - 协同过滤](https://www.ibm.com/developerworks/cn/web/1103_zhaoct_recommstudy2/index.html?ca=drs-)
* [深入推荐引擎相关算法 - 聚类](https://www.ibm.com/developerworks/cn/web/1103_zhaoct_recommstudy3/index.html?ca=drs-)
* [推荐系统不相信眼泪](http://iyao.ren/2017/02/28/itemcf/)
