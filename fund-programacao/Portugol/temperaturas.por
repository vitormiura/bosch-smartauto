programa{
	
	funcao inicio(){
		inteiro tamanho = 14
		inteiro temperaturas[14]
		para (inteiro i = 0; i < tamanho; i++){
			escreva("Digite a temperatura do dia "+ (i+1) + ": ")
			leia(temperaturas[i])
		}
		escreva("---------------------------------------------\n")
		para (inteiro i = 0; i < tamanho; i++){
			para (inteiro j=0; j < tamanho - 1; j++){
				se (temperaturas[j] > temperaturas[j+1]){
					inteiro temp = temperaturas[j]
					temperaturas[j] = temperaturas[j+1]
					temperaturas[j+1] = temp
				}
			}
		}
		escreva("Temperaturas inseridas da mais baixa à mais alta:\n")
		para(inteiro i = 0; i < tamanho; i++){
			escreva(temperaturas[i] + " ")
		}
		escreva("\nTemperatura mais alta: " + temperaturas[13] + "\n")
		escreva("Temperatura mais baixa: " + temperaturas[0])
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 648; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */