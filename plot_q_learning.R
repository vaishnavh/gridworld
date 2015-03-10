png('plot_q_return.png',width=1200,height=700,pointsize=20)
returns <- read.table(file="q_learning/A/qA_return.csv",sep=",")
nrow(returns)
returns <-apply(returns,MARGIN=2,FUN=mean)
plot(x=1:length(returns),y=returns,type="l",main="Q-Learning",
     xlab="Episode Index",ylab="Average Return",)

returns <- read.table(file="q_learning/B/qB_return.csv",sep=",")
nrow(returns)
returns <-apply(returns,MARGIN=2,FUN=mean)

lines(x=1:length(returns),y=returns,col="red")

returns <- read.table(file="q_learning/C/qC_return.csv",sep=",")
nrow(returns)
returns <-apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,col="blue")
legend(x=400,y=-2,col=c("black","red","blue"),legend=c("A","B","C"),lwd=2)

dev.off()

png('plot_q_steps.png',width=1200,height=700,pointsize=20)
steps <- read.table(file="q_learning/A/qA_steps.csv.corr",sep=",",stringsAsFactors=FALSE)
nrow(steps)
steps <-apply(steps,MARGIN=2,FUN=mean)

plot(x=1:length(steps),y=steps,type="l",main="Q-Learning",
     xlab="Episode Index",ylab="Average Steps",ylim=c(0,600))

steps <- read.table(file="q_learning/B/qB_steps.csv.corr",sep=",",stringsAsFactors=FALSE)
nrow(steps)
steps <-apply(steps,MARGIN=2,FUN=mean)

lines(x=1:length(steps),y=steps,col="red")


steps <- read.table(file="q_learning/C/qC_steps.csv.corr",sep=",",stringsAsFactors=FALSE)
nrow(steps)
steps <-apply(steps,MARGIN=2,FUN=mean)

lines(x=1:length(steps),y=steps,col="blue")

legend(x=400,y=500,col=c("black","red","blue"),legend=c("A","B","C"),lwd=2)
dev.off()
