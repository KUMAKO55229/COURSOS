package Thread;

interface Figura {
	void desenha ();
}

public class ExemploThread {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
      
		
		Figura fig1 = new Figura(){

			@Override
			public void desenha() {
				// TODO Auto-generated method stub
				System.out.println("Desenha figura 1");
			}
			
		};
		fig1.desenha();
		
		Figura fig2 = () -> System.out.println("Desenha figura 2");
		fig2.desenha();
		
	}

}
