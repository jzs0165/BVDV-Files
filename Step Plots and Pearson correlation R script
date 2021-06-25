data=read.csv(file = "step-plot2.csv")


# Overlap of Reactivity values

Z1=read.csv(file = "Zone1_reactivity values.csv")

plot(Z1$Nucloetides, Z1$Short, type = "S", col = "red", xlab="Nucleotides", ylab="Reactivity values", xlim=c(25,250), ylim=c(0,4))
lines(Z1$Nucloetides, Z1$Long, type = "S", col = "blue")


#Zone 2
Z2=read.csv(file = "Zone2_Reactivity values1.csv")

plot(Z2$Nucleotides, Z2$Short, type = "S", col = "red", xlab="Nucleotides", ylab="Reactivity values", xlim=c(251,478), ylim=c(0,5))
lines(Z2$Nucleotides, Z2$Long, type = "S", col = "blue")


# Scatter Plot

Scatter=read.csv(file = "step-plot2.csv")
x <- Scatter$Short
y <- Scatter$Long
# Plot with main and axis titles
# Change point shape (pch = 19) and remove frame.

plot(x, y,
     xlab = "Short Transcript Reactivity values", ylab = "Long Transcript Reactivity values",
     pch = 19, frame = FALSE, col = "blue")
# Add regression line
plot(x, y,
     xlab = "Short Transcript Reactivity values", ylab = "Long Transcript Reactivity values",
     pch = 19, frame = FALSE, col = "blue")
abline(lm(y ~ x, data = Scatter), col = "black")

res <- cor.test(x, y, 
                method = "pearson")
res



