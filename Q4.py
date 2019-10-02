#Questão 4- Sequência de Nob

def nob(n1,n2):

	dezena_n1= n1//10
	dezena_n2= n2//10
	unidade_n1= n1%10
	unidade_n2= n2%10

	resposta= dezena_n1+dezena_n2+unidade_n1+unidade_n2

	return resposta

num_1=21
num_2=36

resposta_nob=nob(num_1,num_2)

print("Resposta=",resposta_nob)