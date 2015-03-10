palette <- c("darkblue","black","darkred","hotpink","mediumorchid","seagreen3","seagreen")
png('plot_b_return_smooth.png',width=1200,height=700,pointsize=20)
returns <- read.table(file="q_learning/B/qB_return.csv",sep=",")
returns <-my_apply(returns,MARGIN=2,FUN=mean)
plot(x=1:length(returns),y=returns,type="l",main="Learning for B",
     xlab="Episode Index",ylab="Average Return",col=palette[1])



returns <- read.table(file="sarsa_00/B_return.csv",sep=",")
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col=palette[2])

returns <- read.table(file="sarsa_30/B_return.csv",sep=",")
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col=palette[3])

returns <- read.table(file="sarsa_50/B_return.csv",sep=",")
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col=palette[4])

returns <- read.table(file="sarsa_90/B_return.csv",sep=",")
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col=palette[5])

returns <- read.table(file="sarsa_99/B_return.csv",sep=",")
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col=palette[6])

returns <- read.table(file="sarsa_100/B_return.csv",sep=",")
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col=palette[7])

legend(x=400,y=-2,col=c(palette[1],palette[2],palette[3],palette[4],palette[5],palette[6],palette[7]),cex=1,
       legend=c("Q","S(0)","S(0.3)","S(0.5)","S(0.9)","S(0.99)","S(1)"),lwd=2)
dev.off()

png('plot_b_steps_smooth.png',width=1200,height=700,pointsize=20)
steps <- read.table(file="q_learning/B/qB_steps.csv.corr",sep=",")
steps <-my_apply(steps,MARGIN=2,FUN=mean)
plot(x=1:length(steps),y=steps,type="l",main="Learning for B",
     xlab="Episode Index",ylab="Average Steps",col=palette[1],ylim=c(0,1500))



steps <- read.table(file="sarsa_00/B_steps.csv.corr",sep=",")
steps <-my_apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col=palette[2])

steps <- read.table(file="sarsa_30/B_steps.csv.corr",sep=",")
steps <-my_apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col=palette[3])

steps <- read.table(file="sarsa_50/B_steps.csv.corr",sep=",")
steps <-my_apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col=palette[4])

steps <- read.table(file="sarsa_99/B_steps.csv.corr",sep=",")
steps <-my_apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col=palette[5])

steps <- read.table(file="sarsa_99/B_steps.csv.corr",sep=",")
steps <-my_apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col=palette[6])

steps <- read.table(file="sarsa_100/B_steps.csv.corr",sep=",")
steps <-my_apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col=palette[7])

legend(x=400,y=1000,col=c(palette[1],palette[2],palette[3],palette[4],palette[5],palette[6],palette[7]),
       legend=c("Q","S(0)","S(0.3)","S(0.5)","S(0.9)","S(0.99)","S(1)"),lwd=2)
dev.off()

png('plot_A_return_smooth.png',width=1200,height=700,pointsize=20)

returns <- read.table(file="q_learning/A/qA_return.csv",sep=",")
returns <-my_apply(returns,MARGIN=2,FUN=mean)
plot(x=1:length(returns),y=returns,type="l",main="Learning for A",
     xlab="Episode Index",ylab="Average Return",col=palette[1])



returns <- read.table(file="sarsa_00/A_return.csv",sep=",")
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col=palette[2])

returns <- read.table(file="sarsa_30/A_return.csv",sep=",")
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col=palette[3])

returns <- read.table(file="sarsa_50/A_return.csv",sep=",")
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col=palette[4])

returns <- read.table(file="sarsa_90/A_return.csv",sep=",")
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col=palette[5])

returns <- read.table(file="sarsa_99/A_return.csv",sep=",")
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col=palette[6])

returns <- read.table(file="sarsa_100/A_return.csv",sep=",")
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col=palette[7])

legend(x=400,y=-2,col=c(palette[1],palette[2],palette[3],palette[4],palette[5],palette[6],palette[7]),cex=1,
       legend=c("Q","S(0)","S(0.3)","S(0.5)","S(0.9)","S(0.99)","S(1)"),lwd=2)
dev.off()

png('plot_A_steps_smooth.png',width=1200,height=700,pointsize=20)
steps <- read.table(file="q_learning/A/qA_steps.csv.corr",sep=",")
steps <-my_apply(steps,MARGIN=2,FUN=mean)
plot(x=1:length(steps),y=steps,type="l",main="Learning for A",
     xlab="Episode Index",ylab="Average Steps",col=palette[1],ylim=c(0,500))



steps <- read.table(file="sarsa_00/A_steps.csv.corr",sep=",")
steps <-my_apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col=palette[2])

steps <- read.table(file="sarsa_30/A_steps.csv.corr",sep=",")
steps <-my_apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col=palette[3])

steps <- read.table(file="sarsa_50/A_steps.csv.corr",sep=",")
steps <-my_apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col=palette[4])

steps <- read.table(file="sarsa_99/A_steps.csv.corr",sep=",")
steps <-my_apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col=palette[5])

steps <- read.table(file="sarsa_99/A_steps.csv.corr",sep=",")
steps <-my_apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col=palette[6])

steps <- read.table(file="sarsa_100/A_steps.csv.corr",sep=",")
steps <-my_apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col=palette[7])

legend(x=400,y=400,col=c(palette[1],palette[2],palette[3],palette[4],palette[5],palette[6],palette[7]),
       legend=c("Q","S(0)","S(0.3)","S(0.5)","S(0.9)","S(0.99)","S(1)"),lwd=2)
dev.off()


png('plot_C_return_smooth.png',width=1200,height=700,pointsize=20)

returns <- read.table(file="q_learning/C/qC_return.csv",sep=",")
returns <-my_apply(returns,MARGIN=2,FUN=mean)
plot(x=1:length(returns),y=returns,type="l",main="Learning for C",
     xlab="Episode Index",ylab="Average Return",col=palette[1])



returns <- read.table(file="sarsa_00/C_return.csv",sep=",")
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col=palette[2])

returns <- read.table(file="sarsa_30/C_return.csv",sep=",")
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col=palette[3])

returns <- read.table(file="sarsa_50/C_return.csv",sep=",")
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col=palette[4])

returns <- read.table(file="sarsa_90/C_return.csv",sep=",")
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col=palette[5])

returns <- read.table(file="sarsa_99/C_return.csv",sep=",")
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col=palette[6])

returns <- read.table(file="sarsa_100/C_return.csv",sep=",")
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,type="l",col=palette[7])

legend(x=400,y=0.0,col=c(palette[1],palette[2],palette[3],palette[4],palette[5],palette[6],palette[7]),cex=1,
       legend=c("Q","S(0)","S(0.3)","S(0.5)","S(0.9)","S(0.99)","S(1)"),lwd=2)
dev.off()

png('plot_C_steps_smooth.png',width=1200,height=700,pointsize=20)
steps <- read.table(file="q_learning/C/qC_steps.csv.corr",sep=",")
steps <-my_apply(steps,MARGIN=2,FUN=mean)
plot(x=1:length(steps),y=steps,type="l",main="Learning for C",
     xlab="Episode Index",ylab="Average Steps",col=palette[1],ylim=c(0,1500))



steps <- read.table(file="sarsa_00/C_steps.csv.corr",sep=",")
steps <-my_apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col=palette[2])

steps <- read.table(file="sarsa_30/C_steps.csv.corr",sep=",")
steps <-my_apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col=palette[3])

steps <- read.table(file="sarsa_50/C_steps.csv.corr",sep=",")
steps <-my_apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col=palette[4])

steps <- read.table(file="sarsa_99/C_steps.csv.corr",sep=",")
steps <-my_apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col=palette[5])

steps <- read.table(file="sarsa_99/C_steps.csv.corr",sep=",")
steps <-my_apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col=palette[6])

steps <- read.table(file="sarsa_100/C_steps.csv.corr",sep=",")
steps <-my_apply(steps,MARGIN=2,FUN=mean)
lines(x=1:length(steps),y=steps,type="l",col=palette[7])

legend(x=400,y=1500,col=c(palette[1],palette[2],palette[3],palette[4],palette[5],palette[6],palette[7]),
       legend=c("Q","S(0)","S(0.3)","S(0.5)","S(0.9)","S(0.99)","S(1)"),lwd=2)
dev.off()


returns <- read.table(file="sarsa_100/A_return.csv",sep=",")
nrow(returns)
returns <-my_apply(returns,MARGIN=2,FUN=mean)
plot(x=1:length(returns),y=returns,type="l",main="Sarsa(1)",
     xlab="Episode Index",ylab="Average Return",)




returns <- read.table(file="sarsa_100/B_return.csv",sep=",")
nrow(returns)
returns <-my_apply(returns,MARGIN=2,FUN=mean)

lines(x=1:length(returns),y=returns,col="red")

returns <- read.table(file="sarsa_100/C_return.csv",sep=",")
nrow(returns)
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,col="blue")
legend(x=400,y=-2,col=c(palette[2],"red","blue"),legend=c("A","B","C"),lwd=2)



steps <- read.table(file="sarsa_100/A_steps.csv.corr",sep=",")
nrow(steps)
steps <-my_apply(steps,MARGIN=2,FUN=mean)

plot(x=1:length(steps),y=steps,type="l",main="Sarsa(1)",
     xlab="Episode Index",ylab="Average Steps",ylim=c(0,3000))

steps <- read.table(file="sarsa_100/B_steps.csv.corr",sep=",")
nrow(steps)
steps <-my_apply(steps,MARGIN=2,FUN=mean)

lines(x=1:length(steps),y=steps,col="red")


steps <- read.table(file="sarsa_100/C_steps.csv.corr",sep=",")
nrow(steps)
steps <-my_apply(steps,MARGIN=2,FUN=mean)

lines(x=1:length(steps),y=steps,col="blue")

legend(x=400,y=2500,col=c(palette[2],"red","blue"),legend=c("A","B","C"),lwd=2)


png('plot_sarsa90_return_smooth.png',width=1200,height=700,pointsize=20)
returns <- read.table(file="sarsa_90/A_return.csv",sep=",")
nrow(returns)
returns <-my_apply(returns,MARGIN=2,FUN=mean)
plot(x=1:length(returns),y=returns,type="l",main="Sarsa(0.90)",
     xlab="Episode Index",ylab="Average Return",)




returns <- read.table(file="sarsa_90/B_return.csv",sep=",")
nrow(returns)
returns <-my_apply(returns,MARGIN=2,FUN=mean)

lines(x=1:length(returns),y=returns,col="red")

returns <- read.table(file="sarsa_90/C_return.csv",sep=",")
nrow(returns)
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,col="blue")
legend(x=400,y=-2,col=c(palette[2],"red","blue"),legend=c("A","B","C"),lwd=2)
dev.off()

png('plot_sarsa90_steps_smooth.png',width=1200,height=700,pointsize=20)



steps <- read.table(file="sarsa_90/A_steps.csv.corr",sep=",")
nrow(steps)
steps <-my_apply(steps,MARGIN=2,FUN=mean)

plot(x=1:length(steps),y=steps,type="l",main="Sarsa(0.90)",
     xlab="Episode Index",ylab="Average Steps",ylim=c(0,700))

steps <- read.table(file="sarsa_90/B_steps.csv.corr",sep=",")
nrow(steps)
steps <-my_apply(steps,MARGIN=2,FUN=mean)

lines(x=1:length(steps),y=steps,col="red")


steps <- read.table(file="sarsa_90/C_steps.csv.corr",sep=",")
nrow(steps)
steps <-my_apply(steps,MARGIN=2,FUN=mean)

lines(x=1:length(steps),y=steps,col="blue")

legend(x=400,y=600,col=c(palette[2],"red","blue"),legend=c("A","B","C"),lwd=2)

dev.off()


png('plot_sarsa99_return_smooth.png',width=1200,height=700,pointsize=20)

returns <- read.table(file="sarsa_99/A_return.csv",sep=",")
nrow(returns)
returns <-my_apply(returns,MARGIN=2,FUN=mean)
plot(x=1:length(returns),y=returns,type="l",main="Sarsa(0.99)",
     xlab="Episode Index",ylab="Average Return",)




returns <- read.table(file="sarsa_99/B_return.csv",sep=",")
nrow(returns)
returns <-my_apply(returns,MARGIN=2,FUN=mean)

lines(x=1:length(returns),y=returns,col="red")

returns <- read.table(file="sarsa_99/C_return.csv",sep=",")
nrow(returns)
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,col="blue")
legend(x=400,y=-2,col=c(palette[2],"red","blue"),legend=c("A","B","C"),lwd=2)
dev.off()

png('plot_sarsa90_steps_smooth.png',width=1200,height=700,pointsize=20)

steps <- read.table(file="sarsa_99/A_steps.csv.corr",sep=",")
nrow(steps)
steps <-my_apply(steps,MARGIN=2,FUN=mean)

plot(x=1:length(steps),y=steps,type="l",main="Sarsa(0.99)",
     xlab="Episode Index",ylab="Average Steps",ylim=c(0,3000))

steps <- read.table(file="sarsa_99/B_steps.csv.corr",sep=",")
nrow(steps)
steps <-my_apply(steps,MARGIN=2,FUN=mean)

lines(x=1:length(steps),y=steps,col="red")


steps <- read.table(file="sarsa_99/C_steps.csv.corr",sep=",")
nrow(steps)
steps <-my_apply(steps,MARGIN=2,FUN=mean)

lines(x=1:length(steps),y=steps,col="blue")

legend(x=50,y=2500,col=c(palette[2],"red","blue"),legend=c("A","B","C"),lwd=2)

dev.off()

png('plot_sarsa30_return_smooth.png',width=1200,height=700,pointsize=20)

returns <- read.table(file="sarsa_30/A_return.csv",sep=",")
nrow(returns)
returns <-my_apply(returns,MARGIN=2,FUN=mean)
plot(x=1:length(returns),y=returns,type="l",main="Sarsa(0.30)",
     xlab="Episode Index",ylab="Average Return",)




returns <- read.table(file="sarsa_30/B_return.csv",sep=",")
nrow(returns)
returns <-my_apply(returns,MARGIN=2,FUN=mean)

lines(x=1:length(returns),y=returns,col="red")

returns <- read.table(file="sarsa_30/C_return.csv",sep=",")
nrow(returns)
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,col="blue")
legend(x=400,y=-2,col=c(palette[2],"red","blue"),legend=c("A","B","C"),lwd=2)

dev.off()
png('plot_sarsa30_steps_smooth.png',width=1200,height=700,pointsize=20)


steps <- read.table(file="sarsa_30/A_steps.csv.corr",sep=",")
nrow(steps)
steps <-my_apply(steps,MARGIN=2,FUN=mean)

plot(x=1:length(steps),y=steps,type="l",main="Sarsa(0.30)",
     xlab="Episode Index",ylab="Average Steps",ylim=c(0,2500))

steps <- read.table(file="sarsa_30/B_steps.csv.corr",sep=",")
nrow(steps)
steps <-my_apply(steps,MARGIN=2,FUN=mean)

lines(x=1:length(steps),y=steps,col="red")


steps <- read.table(file="sarsa_30/C_steps.csv.corr",sep=",")
nrow(steps)
steps <-my_apply(steps,MARGIN=2,FUN=mean)

lines(x=1:length(steps),y=steps,col="blue")

legend(x=400,y=1800,col=c(palette[2],"red","blue"),legend=c("A","B","C"),lwd=2)
dev.off()

png('plot_sarsa00_return_smooth.png',width=1200,height=700,pointsize=20)

returns <- read.table(file="sarsa_00/A_return.csv",sep=",")
nrow(returns)
returns <-my_apply(returns,MARGIN=2,FUN=mean)
plot(x=1:length(returns),y=returns,type="l",main="Sarsa(0)",
     xlab="Episode Index",ylab="Average Return",)

returns <- read.table(file="sarsa_00/B_return.csv",sep=",")
nrow(returns)
returns <-my_apply(returns,MARGIN=2,FUN=mean)

lines(x=1:length(returns),y=returns,col="red")

returns <- read.table(file="sarsa_00/C_return.csv",sep=",")
nrow(returns)
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,col="blue")
legend(x=400,y=-2,col=c(palette[2],"red","blue"),legend=c("A","B","C"),lwd=2)
dev.off()

png('plot_sarsa00_steps_smooth.png',width=1200,height=700,pointsize=20)

steps <- read.table(file="sarsa_00/A_steps.csv.corr",sep=",")
nrow(steps)
steps <-my_apply(steps,MARGIN=2,FUN=mean)

plot(x=1:length(steps),y=steps,type="l",main="Sarsa(0)",
     xlab="Episode Index",ylab="Average Steps",ylim=c(0,2500))

steps <- read.table(file="sarsa_00/B_steps.csv.corr",sep=",")
nrow(steps)
steps <-my_apply(steps,MARGIN=2,FUN=mean)

lines(x=1:length(steps),y=steps,col="red")


steps <- read.table(file="sarsa_00/C_steps.csv.corr",sep=",")
nrow(steps)
steps <-my_apply(steps,MARGIN=2,FUN=mean)

lines(x=1:length(steps),y=steps,col="blue")

legend(x=400,y=1800,col=c(palette[2],"red","blue"),legend=c("A","B","C"),lwd=2)
dev.off()

png('plot_sarsa50_return_smooth.png',width=1200,height=700,pointsize=20)

returns <- read.table(file="sarsa_50/A_return.csv",sep=",")
nrow(returns)
returns <-my_apply(returns,MARGIN=2,FUN=mean)
plot(x=1:length(returns),y=returns,type="l",main="Sarsa(0.50)",
     xlab="Episode Index",ylab="Average Return",)




returns <- read.table(file="sarsa_50/B_return.csv",sep=",")
nrow(returns)
returns <-my_apply(returns,MARGIN=2,FUN=mean)

lines(x=1:length(returns),y=returns,col="red")

returns <- read.table(file="sarsa_50/C_return.csv",sep=",")
nrow(returns)
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,col="blue")
legend(x=400,y=-2,col=c(palette[2],"red","blue"),legend=c("A","B","C"),lwd=2)
dev.off()


png('plot_sarsa50_return_smooth.png',width=1200,height=700,pointsize=20)



steps <- read.table(file="sarsa_50/A_steps.csv.corr",sep=",")
nrow(steps)
steps <-my_apply(steps,MARGIN=2,FUN=mean)

plot(x=1:length(steps),y=steps,type="l",main="Sarsa(0.50)",
     xlab="Episode Index",ylab="Average Steps",ylim=c(0,1500))

steps <- read.table(file="sarsa_50/B_steps.csv.corr",sep=",")
nrow(steps)
steps <-my_apply(steps,MARGIN=2,FUN=mean)

lines(x=1:length(steps),y=steps,col="red")


steps <- read.table(file="sarsa_50/C_steps.csv.corr",sep=",")
nrow(steps)
steps <-my_apply(steps,MARGIN=2,FUN=mean)

lines(x=1:length(steps),y=steps,col="blue")

legend(x=400,y=1000,col=c(palette[2],"red","blue"),legend=c("A","B","C"),lwd=2)
dev.off()

png('plot_q_return_smooth.png',width=1200,height=700,pointsize=20)
returns <- read.table(file="q_learning/A/qA_return.csv",sep=",")
nrow(returns)
returns <-my_apply(returns,MARGIN=2,FUN=mean)
plot(x=1:length(returns),y=returns,type="l",main="Q-Learning",
     xlab="Episode Index",ylab="Average Return",)

returns <- read.table(file="q_learning/B/qB_return.csv",sep=",")
nrow(returns)
returns <-my_apply(returns,MARGIN=2,FUN=mean)

lines(x=1:length(returns),y=returns,col="red")

returns <- read.table(file="q_learning/C/qC_return.csv",sep=",")
nrow(returns)
returns <-my_apply(returns,MARGIN=2,FUN=mean)
lines(x=1:length(returns),y=returns,col="blue")
legend(x=400,y=-2,col=c(palette[2],"red","blue"),legend=c("A","B","C"),lwd=2)

dev.off()

png('plot_q_steps_smooth.png',width=1200,height=700,pointsize=20)
steps <- read.table(file="q_learning/A/qA_steps.csv.corr",sep=",",stringsAsFactors=FALSE)
nrow(steps)
steps <-my_apply(steps,MARGIN=2,FUN=mean)

plot(x=1:length(steps),y=steps,type="l",main="Q-Learning",
     xlab="Episode Index",ylab="Average Steps",ylim=c(0,600))

steps <- read.table(file="q_learning/B/qB_steps.csv.corr",sep=",",stringsAsFactors=FALSE)
nrow(steps)
steps <-my_apply(steps,MARGIN=2,FUN=mean)

lines(x=1:length(steps),y=steps,col="red")


steps <- read.table(file="q_learning/C/qC_steps.csv.corr",sep=",",stringsAsFactors=FALSE)
nrow(steps)
steps <-my_apply(steps,MARGIN=2,FUN=mean)

lines(x=1:length(steps),y=steps,col="blue")

legend(x=400,y=500,col=c(palette[2],"red","blue"),legend=c("A","B","C"),lwd=2)
dev.off()
