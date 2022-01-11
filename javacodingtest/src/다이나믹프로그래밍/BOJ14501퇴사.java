package 다이나믹프로그래밍;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BOJ14501퇴사 {


    static int comparison(int a, int b, int c){
        return (a > b) ? ((a > c) ? a : c) : (b > c) ? b : c;
    }


    public static void main(String[] args) throws Exception{
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder stringBuilder = new StringBuilder();

        String[] size = bufferedReader.readLine().split(" ");
        int row = Integer.parseInt(size[0]);
        int column = Integer.parseInt(size[1]);

        int[][] maze = new int[row][column];
        int[][] result = new int[row][column];

        for (int i = 0; i < row; i++) {
            String[] candy = bufferedReader.readLine().split(" ");
            for (int j = 0; j < column; j++) {
                maze[i][j] = Integer.parseInt(candy[j]);
            }
        }

        result[0][0] = maze[0][0];

        for (int i = 1; i < column; i++) {
            result[0][i] = maze[0][i] + result[0][i-1];
        }

        for (int i = 1; i < row; i++) {
            result[i][0] = maze[i][0] + result[i-1][0];
        }

        if (row > 1 && column > 1) {
            for (int i = 1; i < row; i++) {
                for (int j = 1; j < column; j++) {
                    result[i][j] = maze[i][j] + comparison(result[i-1][j-1], result[i-1][j], result[i][j-1]);
                }
            }
        }

        System.out.println(result[row-1][column-1]);
    }
}
