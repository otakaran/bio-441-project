source("http://zzlab.net/GAPIT/GAPIT.library.R")
source("http://zzlab.net/GAPIT/gapit_functions.txt")
library(GuessCompx)

#Import data from Zhiwu Zhang Lab
myY <- read.table("C:/Users/slate/bio-441-project/raw_data/pgen.1007217.s010.txt", head = TRUE, sep = '\t')
myG <- read.table("C:/Users/slate/bio-441-project/raw_data/studyHapmap.hmp/studyHapmap.hmp.txt", head = FALSE)

# selects taxa and variable to run GWAS on
myY <- myY[,c(1, 4, 5, 6, 7)]

myG_header = myG[1,]
myG = myG[2:nrow(myG),]

# SNP.MAF to filter SNPs

f1 = function(df){
  df[1,] = myG_header
  myGAPIT_MLM <- GAPIT(
    Y=myY,
    G=df,
    model='MLM',
    SNP.MAF = 0.02,
    Inter.Plot = T,
    Model.selection = TRUE)
}

CompEst(d = myG, f = f1, random.sampling = FALSE, replicates=2, start.size = 100, plot.result = TRUE)

# CompEst(d = ggplot2::diamonds[, 5:10], f = dist, replicates = 10, max.time = 10, plot.result = TRUE)





