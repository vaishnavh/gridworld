returns <- read.table(file="q_learning/A/qA_return.csv",sep=",")
nrow(returns)
returns <-apply(returns,MARGIN=2,FUN=mean)
plot(x=1:length(returns),y=returns,type="l",main="Q-Learning (A)",
     xlab="Episode Index",ylab="Average Return",)

steps <- read.table(file="q_learning/A/qA_steps.csv.corr",sep=",",stringsAsFactors=FALSE)
nrow(steps)
steps <-apply(steps,MARGIN=2,FUN=mean)

plot(x=1:length(steps),y=steps,type="l",main="Q-Learning (A)",
     xlab="Episode Index",ylab="Average Steps")

#=================================#


returns <- read.table(file="q_learning/B/qB_return.csv",sep=",")
nrow(returns)
returns <-apply(returns,MARGIN=2,FUN=mean)
plot(x=1:length(returns),y=returns,type="l",main="Q-Learning (B)",
     xlab="Episode Index",ylab="Average Return",)

steps <- read.table(file="q_learning/B/qB_steps.csv.corr",sep=",",stringsAsFactors=FALSE)
nrow(steps)
steps <-apply(steps,MARGIN=2,FUN=mean)

plot(x=1:length(steps),y=steps,type="l",main="Q-Learning (B)",
     xlab="Episode Index",ylab="Average Steps")
#===================================#

returns <- read.table(file="q_learning/C/qC_return.csv",sep=",")
nrow(returns)
returns <-apply(returns,MARGIN=2,FUN=mean)
plot(x=1:length(returns),y=returns,type="l",main="Q-Learning (C)",
     xlab="Episode Index",ylab="Average Return",)

steps <- read.table(file="q_learning/C/qC_steps.csv.corr",sep=",",stringsAsFactors=FALSE)
nrow(steps)
steps <-apply(steps,MARGIN=2,FUN=mean)

plot(x=1:length(steps),y=steps,type="l",main="Q-Learning (C)",
     xlab="Episode Index",ylab="Average Steps")

