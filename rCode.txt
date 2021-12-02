source("http://zzlab.net/GAPIT/GAPIT.library.R")
source("http://zzlab.net/GAPIT/gapit_functions.txt")

#Import data from Zhiwu Zhang Lab
myY <- read.table("C:/testStudy/pgen.1007217.s010.txt", head = TRUE, sep = '\t')
myG <- read.table("C:/testStudy/studyHapmap.hmp.txt", head = FALSE)

# selects taxa and variable to run GWAS on
myY <- myY[,c(1, 4, 5, 6, 7)]

# SNP.MAF to filter SNPs

myGAPIT_MLM <- GAPIT(
  Y=myY,
  G=myG,
  model='MLM',
  SNP.MAF = 0.02,
  Inter.Plot = T,
  Model.selection = TRUE)


print("Done")