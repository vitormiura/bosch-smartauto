programa
{
	
	real n, a1, an, r
	
	funcao inicio()
	{
		escreva("Enésimo: ")
		leia(n)
		escreva("Primeiro Termo: ")
		leia(a1)
		escreva("Utlimo Termo: ")
		leia(an)
		escreva("Razão: ")
		leia(r)
			
		an = (a1+(n-1)*-r)
		escreva("\nResultado PA:", an)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 170; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */