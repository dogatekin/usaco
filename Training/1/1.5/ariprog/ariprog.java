/*
ID: dtekin1
LANG: JAVA
TASK: ariprog
*/
import java.io.*;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.HashSet;

public class ariprog {

    public static void main(String[] args) throws IOException {
        BufferedReader f = new BufferedReader(new FileReader("ariprog.in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("ariprog.out")));

        int N = Integer.parseInt(f.readLine());
        int M = Integer.parseInt(f.readLine());
        HashSet<Integer> bisq = new HashSet<Integer>();

        for(int p = 0; p <= M; p++) {
            for(int q = p; q <= M; q++) {
                bisq.add(p*p + q*q);
            }
        }

        ArrayList<Integer> bisqs = new ArrayList<>(bisq);
        Collections.sort(bisqs);

        boolean atLeastOne = false;

        for(int b = 1; b < 2*M*M; b++) {
            for(int a : bisqs) {
                if(a + (N-1)*b > 2*M*M) {
                    break;
                }

                int cur = a;
                int cnt = 0;
                do {
                    cur += b;
                    cnt++;
                } while (bisq.contains(cur) && cnt < N);

                if(cnt == N) {
                    out.println(a + " " + b);
                    atLeastOne = true;
                }
            }
        }

        if(!atLeastOne) {
            out.println("NONE");
        }

        out.close();
    }
}
