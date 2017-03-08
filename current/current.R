
data1<-read.csv('data.csv',header=T)

b=0
cdf=0
len=length(data1[,1])
for(j in 1:len){
  
  matrix1=matrix(0,nrow=len,ncol=j,F)
  matrix2=matrix(0,nrow=len-j+1,ncol=len,T)
  matrix3=matrix(0,nrow=len-j+1,ncol=len,T)
  
  for(u in 1:j){
    matrix1[u:len,u]=1
  }    
  
  for(v in j:len){
    matrix2[v-j+1,1:v]=data1[1:v,2]
    
    matrix3[v-j+1,1:v]=data1[1:v,3]
  }
  
  numerator=matrix2 %*% matrix1
  denominator=matrix2 %*% matrix1 + matrix3 %*% matrix1
  
  all=numerator/denominator
  
  a=0
  for(z in 1:j)
    if(min(all[,z])>a)a=min(all[,z])
  
  cdf[j]=a
}