# Multiple linear regression

#install.packages('caTools')
library(caTools)

# Importing the dataset
dataset = read.csv('50_Startups.csv')

# Encoding categorial data
dataset$State = factor(dataset$State,
                       levels = c('New York', 'California', 'Florida'),
                       labels = c(1, 2, 3))

# Splitting the dataset into training and test set
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Fitting multiple linear regression to the training set
# regressor = lm(formula = Profit ~ ., data = training_set) shortcut
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State, data = training_set)
#summary(regressor)
# Looking at the summary it is possible to say that the only relevant independent variable is R&D.Spend
# So, the model could be rewritten as a single linear regression with this only variable or feature

# Predicting test set
y_pred = predict(regressor, newdata = test_set)
y_pred

# Backward elimination based on P value:
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State, data = training_set)
summary(regressor)

regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend, data = training_set)
summary(regressor)

regressor = lm(formula = Profit ~ R.D.Spend + Marketing.Spend, data = training_set)
summary(regressor)

regressor = lm(formula = Profit ~ R.D.Spend, data = training_set)
summary(regressor)
