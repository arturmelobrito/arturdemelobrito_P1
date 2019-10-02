#Pratica pra P1 de comp

#Questão 3 da P1- Cálculo de pi
def seq(n):
	return (1/(2*n+1))

p1=4
p2=4*(1-1/3)
contador=2
inversor=1

while((p2-p1)>5*(10**-8) or (p2-p1)<-5*(10**-8) ):

	p1=p2
	p2=p2+4*seq(contador)*inversor

	contador+=1
	inversor= -inversor

print("Pi=",p2)



