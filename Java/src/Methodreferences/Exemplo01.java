package Methodreferences;
/*interface Figura2D {
	void desenha (Double largura, Double altura);
}*/
@FunctionalInterface
interface Figura2D {
	Retangulo desenha (Double largura, Double altura);
}
/*class Retangulo {
	public void desenhaRetangulo(Double largura, Double altura){
		System.out.println("Desenha retangulo de Largura: "+ largura + "e altura : " + altura);
		
	};
}*/
class Retangulo {
	public  Retangulo(Double largura, Double altura){
		System.out.println("Desenha retangulo de Largura: "+ largura + " e altura : " + altura);
		
	};}
public class Exemplo01 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	/*	//Lamda expression
		Figura2D fig1 = (l,a) -> System.out.println("Desenha figura de Largura: "+ l + " e altura : " + a);
		fig1.desenha(8.0, 1.5);
		Retangulo ret = new Retangulo();
		//method references usando methodo
		Figura2D fig2 = ret::desenhaRetangulo; 
		fig2.desenha(10.5,7.0);
		
*/      
		//method references usando construtor
		Figura2D fig1 = Retangulo::new;
		fig1.desenha(10.0,2.5);
		
	}

}
