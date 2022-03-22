programa
{
	real peso, altura, imc
	
	funcao inicio()
	{
		escreva("CALCULADOR DE IMC")
		escreva("\n Digite seu Peso: ")
		leia(peso)
		escreva("\n Digite sua altura: ")
		leia(altura)

		imc = (peso/(altura*altura))
		escreva("\n Seu IMC é: "+imc)
		
		se (imc < 16){
			escreva("\n =============")
			escreva("\n Magreza grave")
			escreva("\n =============")
		}
		senao se (imc == 16 ou imc < 17){
			escreva("\n =============")
			escreva("\n Magreza moderada")
			escreva("\n =============")
		}
		senao se (imc == 17 ou imc < 18.5){
			escreva("\n =============")
			escreva("\n Magreza leve")
			escreva("\n =============")
		}
		senao se (imc == 18.5 ou imc < 25){
			escreva("\n =============")
			escreva("\n Saudavel")
			escreva("\n =============")
		}
		senao se (imc == 25 ou imc < 30){
			escreva("\n =============")
			escreva("\n Sobrepeso")
			escreva("\n =============")
		}
		senao se (imc == 30 ou imc < 35){
			escreva("\n =============")
			escreva("\n Obesidade Grau 1")
			escreva("\n =============")
		}
		senao se (imc == 35 ou imc < 40){
			escreva("\n =============")
			escreva("\n Obesidade Grau 2 (severa)")
			escreva("\n =============")
		}
		senao se (imc >= 40){
			escreva("\n =============")
			escreva("\n Obesidade Grau 3 (mórbida)")
			escreva("\n s=============")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1292; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */