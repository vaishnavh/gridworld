png('plot_sarsa99_return.png',width=1200,height=700,pointsize=20)

returns <- read.table(file="sarsa_99/A_return.csv",sep=",")
nrow(returns)
returns <-apply(returns,MARGIN=2,FUN=mean)
plot(x=1:length(returns),y=returns,type="l",main="Sarsa(0.99)",
     xlab="Episode Index",ylab="Average Return",)




returns <- read.table(file="sarsa_99/B_return.csv",sep=",")
nrow(returns)
returns <-apply(returns,MARGIN=2,FUN=mean)

lines(x=1:length(returns),y=returns,col="red")

returns <- read.table(file="sarsa_99/C_return.csv",sep=",")
nrow(returns)
returns <-apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,col="blue")
legend(x=400,y=-2,col=c("black","red","blue"),legend=c("A","B","C"),lwd=2)
dev.off()

png('plot_sarsa90_steps.png',width=1200,height=700,pointsize=20)

steps <- read.table(file="sarsa_99/A_steps.csv.corr",sep=",")
nrow(steps)
steps <-apply(steps,MARGIN=2,FUN=mean)

plot(x=1:length(steps),y=steps,type="l",main="Sarsa(0.99)",
     xlab="Episode Index",ylab="Average Steps",ylim=c(0,3000))

steps <- read.table(file="sarsa_99/B_steps.csv.corr",sep=",")
nrow(steps)
steps <-apply(steps,MARGIN=2,FUN=mean)

lines(x=1:length(steps),y=steps,col="red")


steps <- read.table(file="sarsa_99/C_steps.csv.corr",sep=",")
nrow(steps)
steps <-apply(steps,MARGIN=2,FUN=mean)

lines(x=1:length(steps),y=steps,col="blue")

legend(x=50,y=2500,col=c("black","red","blue"),legend=c("A","B","C"),lwd=2)

dev.off()
