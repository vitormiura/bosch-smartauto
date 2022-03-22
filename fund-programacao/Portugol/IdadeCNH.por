programa
{
	
	funcao inicio()
	{
		inteiro ano, mes, dia, diaAtual, mesAtual, anoAtual
		escreva("Que dia estamos: ")
		leia(diaAtual)
		escreva("Que mes estamos: ")
		leia(mesAtual)
		escreva("Que ano estamos: ")
		leia(anoAtual)
		escreva("Digite o seu dia de nascimento: ")
		leia(dia)
		escreva("Digite o seu mes de nascimento: ")
		leia(mes)
		escreva("Digite o seu ano de nascimento: ")
		leia(ano)
		
		inteiro idade = anoAtual - ano
		
		se(idade >= 18){
		se(mes <= mesAtual){
			se(dia <= diaAtual){
				escreva("Você pode dar entrada na sua CNH")
			}senao{
				escreva("Não tem 18")
			}
		}senao{
			escreva("Não tem 18")
		}
		}senao{
			escreva("Não tem 18")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 608; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */