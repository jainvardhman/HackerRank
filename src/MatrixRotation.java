import java.util.Scanner;

/**
 * Created by Vardhman on 10/17/2015.
 */
public class MatrixRotation {
    int M;
    int N;
    int R;
    int[][] matrix;
    public static void main(String args[]){
        MatrixRotation mRotOb = new MatrixRotation();
        mRotOb.scanInput();
        mRotOb.rotate();
    }

    // scans input from the user/system
    private void scanInput(){
        Scanner scn =  new Scanner(System.in);
        this.M = scn.nextInt();
        this.N = scn.nextInt();
        this.R = scn.nextInt();
        matrix = new int[M][N];
        for(int i = 0 ; i < M ; i++){
            for(int j = 0 ; j < N ; j++){
                int n = scn.nextInt();
                matrix[i][j] = n;
            }
        }
    }

    private void rotate(){
        int level = 0;
        int startM = M;
        int startN = N;
        while(true){
            for(int i=0 ; i < M ; i++){

            }
        }

        for(int i = 0; i < M)
    }

}
