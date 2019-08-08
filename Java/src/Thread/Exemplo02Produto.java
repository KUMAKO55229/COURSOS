package Thread;

import java.util.ArrayList;
import java.util.List;

class Produto {
	private String nome;
	private Double preco;
	public Produto(String nome, Double preco) {
		super();
		this.nome = nome;
		this.preco = preco;
	}
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public Double getPreco() {
		return preco;
	}
	public void setPreco(Double preco) {
		this.preco = preco;
	}
	
	public  void imprime (){
		System.out.println(getNome()+ "="+getPreco());
	
	
	}
}

class Impressora {
	public static void imprime (Produto p){
		System.out.println(p.getNome()+ "="+ p.getPreco());
	}
}
public class Exemplo02Produto {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
       List<Produto> lista = new ArrayList<Produto>();
       
       lista.add(new Produto("TV 42", 2000.00));
       lista.add(new Produto("Geladeira 470l ", 3200.00));
       lista.add(new Produto("Fogao 4 bocas", 900.00));
       lista.add(new Produto("Videogame", 1999.00));
       lista.add(new Produto("Microondas", 550.00));
             
       //Lambda expression with argument 
      // lista.forEach((p)->System.out.println(p.getNome()+ "=" + p.getPreco()));
       //Lambda expression with 2 argument  
       //lista.sort((p1,p2) ->p1.getPreco().compareTo(p2.getPreco()));
      // lista.forEach((p)->System.out.println(p.getNome()+ "=" + p.getPreco()));
       
       //method references usando methodo
     //  lista.forEach(  Impressora::imprime);
       //method references usando objeto
       lista.forEach(Produto::imprime);
       
       
	}

}
