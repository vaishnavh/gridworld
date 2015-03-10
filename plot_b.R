png('plot_b_return.png',width=1200,height=700,pointsize=20)

returns <- read.table(file="q_learning/B/qB_return.csv",sep=",")
returns <-apply(returns,MARGIN=2,FUN=mean)
plot(x=1:length(returns),y=returns,type="l",main="Learning for B",
     xlab="Episode Index",ylab="Average Return",col="darkblue")



returns <- read.table(file="sarsa_00/B_return.csv",sep=",")
returns <-apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col="black")

returns <- read.table(file="sarsa_30/B_return.csv",sep=",")
returns <-apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col="gray8")

returns <- read.table(file="sarsa_50/B_return.csv",sep=",")
returns <-apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col="gray29")

returns <- read.table(file="sarsa_90/B_return.csv",sep=",")
returns <-apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col="gray40")

returns <- read.table(file="sarsa_99/B_return.csv",sep=",")
returns <-apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col="gray60")

returns <- read.table(file="sarsa_100/B_return.csv",sep=",")
returns <-apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col="gray73")

legend(x=400,y=-2,col=c("darkblue","black","gray8","gray29","gray40","gray60","gray73"),cex=1,
       legend=c("Q","S(0)","S(0.3)","S(0.5)","S(0.9)","S(0.99)","S(1)"),lwd=2)
dev.off()

png('plot_b_steps.png',width=1200,height=700,pointsize=20)
steps <- read.table(file="q_learning/B/qB_steps.csv.corr",sep=",")
steps <-apply(steps,MARGIN=2,FUN=mean)
plot(x=1:length(steps),y=steps,type="l",main="Learning for B",
     xlab="Episode Index",ylab="Average Steps",col="darkblue",ylim=c(0,1500))



steps <- read.table(file="sarsa_00/B_steps.csv.corr",sep=",")
steps <-apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col="black")

steps <- read.table(file="sarsa_30/B_steps.csv.corr",sep=",")
steps <-apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col="gray8")

steps <- read.table(file="sarsa_50/B_steps.csv.corr",sep=",")
steps <-apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col="gray29")

steps <- read.table(file="sarsa_99/B_steps.csv.corr",sep=",")
steps <-apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col="gray40")

steps <- read.table(file="sarsa_99/B_steps.csv.corr",sep=",")
steps <-apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col="gray60")

steps <- read.table(file="sarsa_100/B_steps.csv.corr",sep=",")
steps <-apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col="gray73")

legend(x=400,y=1000,col=c("darkblue","black","gray8","gray29","gray40","gray60","gray73"),
       legend=c("Q","S(0)","S(0.3)","S(0.5)","S(0.9)","S(0.99)","S(1)"),lwd=2)
dev.off()
