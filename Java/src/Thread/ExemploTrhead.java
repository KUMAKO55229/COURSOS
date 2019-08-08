package Thread;

public class ExemploTrhead {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
          Thread t1 = new  Thread (new Runnable(){

			@Override
			public void run() {
				// TODO Auto-generated method stub
				System.out.println("Thread 1 em execucao");
			}
			
        	  
        	  
          });
          
          t1.start();
          
          Thread t2 = new Thread (()-> System.out.println("Thread 2 em execucao"));
          
          t2.start(); 
   	   
          
          
          
	}

}
