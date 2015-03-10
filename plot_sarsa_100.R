returns <- read.table(file="sarsa_100/A_return.csv",sep=",")
nrow(returns)
returns <-apply(returns,MARGIN=2,FUN=mean)
plot(x=1:length(returns),y=returns,type="l",main="Sarsa(1)",
     xlab="Episode Index",ylab="Average Return",)




returns <- read.table(file="sarsa_100/B_return.csv",sep=",")
nrow(returns)
returns <-apply(returns,MARGIN=2,FUN=mean)

lines(x=1:length(returns),y=returns,col="red")

returns <- read.table(file="sarsa_100/C_return.csv",sep=",")
nrow(returns)
returns <-apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,col="blue")
legend(x=400,y=-2,col=c("black","red","blue"),legend=c("A","B","C"),lwd=2)



steps <- read.table(file="sarsa_100/A_steps.csv.corr",sep=",")
nrow(steps)
steps <-apply(steps,MARGIN=2,FUN=mean)

plot(x=1:length(steps),y=steps,type="l",main="Sarsa(1)",
     xlab="Episode Index",ylab="Average Steps",ylim=c(0,3000))

steps <- read.table(file="sarsa_100/B_steps.csv.corr",sep=",")
nrow(steps)
steps <-apply(steps,MARGIN=2,FUN=mean)

lines(x=1:length(steps),y=steps,col="red")


steps <- read.table(file="sarsa_100/C_steps.csv.corr",sep=",")
nrow(steps)
steps <-apply(steps,MARGIN=2,FUN=mean)

lines(x=1:length(steps),y=steps,col="blue")

legend(x=400,y=2500,col=c("black","red","blue"),legend=c("A","B","C"),lwd=2)
