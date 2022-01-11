package 다이나믹프로그래밍;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BOJ14501퇴사 {
    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int totalDay = Integer.parseInt(bufferedReader.readLine());

        int[] period = new int[totalDay+1];
        int[] money = new int[totalDay+1];
        // 결과값
        int[] result = new int[totalDay+1];

        for (int i = 0; i < totalDay; i++) {
            String[] data = bufferedReader.readLine().split(" ");
            period[i] = Integer.parseInt(data[0]);
            money[i] = Integer.parseInt(data[1]);
        }


        for (int i = totalDay-1 ; i >= 0; i--) {
            if (period[i] + i <= totalDay) {
                result[i] = Integer.max(money[i] + result[i + period[i]], result[i + 1]);
            }else {
                result[i] = result[i+1];
            }
        }
        System.out.println(result[0]);
    }
}
