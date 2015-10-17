import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Scanner;

/**
 * Created by Vardhman on 10/17/2015.
 */
public class Pairs {
    int N;
    int K;
    //int[] numbers;
    HashMap<Integer,Integer> numbers;
    public static void main(String args[]){
        Pairs pairsOb = new Pairs();
        pairsOb.scanInput();
        //System.out.println("Pairs with difference " + pairsOb.getK() + ": " + pairsOb.getPairCount());
        System.out.println(pairsOb.getPairCount());
    }

    public int getK(){
        return K;
    }

    // scans input from the user/system
    private void scanInput(){
        Scanner scn =  new Scanner(System.in);
        this.N = scn.nextInt();
        this.K = scn.nextInt();
        numbers = new HashMap<>();
        for(int i = 0 ; i < N ; i++){
            int n = scn.nextInt();
            if(!numbers.containsKey(n))
                numbers.put(n,n);
        }
    }

    private int getPairCount(){
        Iterator itr = numbers.entrySet().iterator();
        int pairCount= 0;
        while(itr.hasNext()){
            Map.Entry pair = (Map.Entry) itr.next();
            itr.remove();
            if(numbers.get((int)pair.getValue() - K) != null)
                pairCount++;
            if(numbers.get((int)pair.getValue() + K) != null)
                pairCount++;
        }
        return pairCount;
    }
}
