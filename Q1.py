#Questão 1 da P1- Cálculo de raízes

def raizes():

	a=int(input("Entre com o coeficiente a: "))
	b=int(input("Entre com o coeficiente b: "))
	c=int(input("Entre com o coeficiente c: "))

	delta=(b**2-4*a*c)

	if (delta>=0):

		raiz_1= (-b+delta**(1/2))/(2*a)
		raiz_2= (-b-delta**(1/2))/(2*a)

		print("Raiz 1=",raiz_1,"\nRaiz 2=",raiz_2)
		return 0

	else:

		parte_real=-b/(2*a)
		parte_imaginaria=((-delta)**(1/2))/(2*a)

		print("Raizes:", parte_real,"+-",parte_imaginaria,"i")
		return 1

raizes()