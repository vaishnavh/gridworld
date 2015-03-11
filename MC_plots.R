returns <- read.table(file="mc/B20_1_return.csv",sep=",")
returns <-apply(returns,MARGIN=2,FUN=mean)
plot(returns, type="l")

returns <- read.table(file="mc/B20_1_steps.csv",sep=",")
returns <-apply(returns,MARGIN=2,FUN=mean)
plot(returns, type="l")

returns <- read.table(file="mc/B20_1_rewards.csv",sep=",")
returns <-apply(returns,MARGIN=2,FUN=mean)
plot(returns, type="l")

returns <- read.table(file="mc/A100_return.csv",sep=",")
returns <-apply(returns,MARGIN=2,FUN=mean)
plot(returns, type="l")

returns <- read.table(file="mc/A100_steps.csv",sep=",")
returns <-apply(returns,MARGIN=2,FUN=mean)
plot(returns, type="l")

returns <- read.table(file="mc/A100_rewards.csv",sep=",")
returns <-apply(returns,MARGIN=2,FUN=mean)
plot(returns, type="l")
