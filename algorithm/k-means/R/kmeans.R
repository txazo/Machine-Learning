# iris数据集
newiris <- iris
# iris数据集去除Species列
newiris$Species <- NULL
# kmeans聚类分析
kc <- kmeans(newiris, 3)
# 画散点图
plot(newiris[c("Sepal.Length", "Sepal.Width")], col = kc$cluster)
# 标出聚类中心
points(kc$centers[,c("Sepal.Length", "Sepal.Width")], col = 1:3, pch = 8, cex = 2)
