smooth <- function(x){
  y <- x
  for(i in 6:length(x)){
    y[i] <- mean(x[(i-5):i])
  }
  return (y)
}

my_apply <- function(x,MARGIN=y,FUN=z){
  return (smooth(apply(x,MARGIN=MARGIN,FUN=FUN)))
}
