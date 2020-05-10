# Simple linear regression

#install.packages('caTools')
library(caTools)
#install.packages('ggplot2')
library(ggplot2)

# Importing the dataset
dataset = read.csv('Salary_Data.csv')

# Visualising the dataset
ggplot() +
  geom_point(aes(x = dataset$YearsExperience, y = dataset$Salary),
             colour = 'red') +
  ggtitle('Salary vs Experience (dataset set)') +
  xlab('Years of experience') +
  ylab('Salary')

set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Fitting simple linear regression to the training set
regressor = lm(formula = Salary ~ YearsExperience, data = training_set)
#summary(regressor)

# Predicting the test set results
y_pred = predict(regressor, newdata = test_set)
#y_pred

# Visualising the training set results
ggplot() +
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             colour = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('Salary vs Experience (training set)') +
  xlab('Years of experience') +
  ylab('Salary')

# Visualising the test set results
ggplot() +
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
             colour = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('Salary vs Experience (test set)') +
  xlab('Years of experience') +
  ylab('Salary')





