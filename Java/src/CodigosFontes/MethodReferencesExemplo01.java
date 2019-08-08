package CodigosFontes;

//Functional interface
interface Figura2D {
	void desenha(Double largura, Double altura);
}

//Observe que a classe Ret�ngulo n�o est� implementando a interface Figura
class Retangulo {
	
	public void desenhaRetangulo(Double largura, Double altura) {
		System.out.println("Desenha ret�ngulo de Largura: " + largura + " e Altura: " + altura);
	}
}

//Refer�ncia a um m�todo de inst�ncia de um objeto particular
public class MethodReferencesExemplo01 {

	public static void main(String[] args) {
		
		//Lambda expression
		Figura2D fig1 = (l, a) -> System.out.println("Desenha ret�ngulo de Largura: " + l + " e Altura: " + a);
		
		fig1.desenha(8.0, 1.5);
		
		/*************************************************************/
		
		//Objeto espec�fico
		Retangulo ret = new Retangulo();
		/*Method reference 
		* Refer�ncia a um m�todo de inst�ncia (desenhaRetangulo) de um objeto particular (ret)
		*/
		Figura2D fig2 = ret::desenhaRetangulo;
				
		fig2.desenha(10.5, 7.0);
	}

}
