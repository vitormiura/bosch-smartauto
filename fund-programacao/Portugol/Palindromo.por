programa{
	
	funcao inicio(){	
		logico primeiravez = verdadeiro
		inteiro numero
		escreva("Digite o número que deseja conferir se é palíndromo: ")
		leia(numero)
		inteiro numerocopia = numero
		inteiro inverso = 0
		inteiro digito
		enquanto (numero > 0){
			se (primeiravez != verdadeiro){
				inverso *= 10
			}
			digito = numero % 10
			numero /= 10
			inverso += digito
			primeiravez = falso
		}
		se(numerocopia == inverso){
			escreva("O número é palíndromo.")
		}senao{
			escreva("O número não é palíndromo.")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 311; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */