import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {
    static int connectingTowns(int n, int[] routes) {
        if (routes.length < 1) {
            return 0;
        }
        
        int md = 1234567;
        int r = 1;
        
        for(int d : routes) {
            r = ((r%md)*(d%md))%md;
        }
        
        return r;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = Integer.parseInt(scanner.nextLine().trim());

        for (int tItr = 0; tItr < t; tItr++) {
            int n = Integer.parseInt(scanner.nextLine().trim());

            int[] routes = new int[n-1];

            String[] routesItems = scanner.nextLine().split(" ");

            for (int routesItr = 0; routesItr < n-1; routesItr++) {
                int routesItem = Integer.parseInt(routesItems[routesItr].trim());
                routes[routesItr] = routesItem;
            }

            int result = connectingTowns(n, routes);

            bufferedWriter.write(String.valueOf(result));
            bufferedWriter.newLine();
        }

        bufferedWriter.close();
    }
}
