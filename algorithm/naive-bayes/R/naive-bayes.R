library(e1071)

dataSet <- read.csv("pima-indians-diabetes.csv", header = FALSE)
names(dataSet) <- c('V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'Class')

length <- nrow(dataSet)
trainDataSet <- dataSet[1:500,]
testDataSet <- dataSet[501:length,]

dataSet <- read.csv("pima-indians-diabetes.csv", header = FALSE)
model <- naiveBayes(Class ~ ., data = dataSet)
pred <- predict(model, dataSet)
table(pred, dataSet$Class)

dataSet <- data.frame(
v1 = c(1,1,2),
v2 = c(1,2,1),
v3 = c(2,1,1)
)
model <- naiveBayes(dataSet[,-3], dataSet[,3])
table(predict(model, dataSet), dataSet[,3])

data(HouseVotes84, package = "mlbench")
model <- naiveBayes(Class ~ ., data = HouseVotes84)
pred <- predict(model, HouseVotes84)
table(pred, HouseVotes84$Class)

data(iris)
m <- naiveBayes(iris[,-5], iris[,5])
table(predict(m, iris), iris[,5])
