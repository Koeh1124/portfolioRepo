import java.util.Random;
import java.util.Scanner;

public class RPS {
    // version 3: main menue
    public static void main(String[] args) {
        // u1 inputs r,p,s
        // u2 inputs r,p,s
        Scanner ui = new Scanner(System.in);
        System.out.println("input 1 for pvp and 2 for pvc");
        System.out.print("Selection: ");
        String sel = ui.nextLine();
        if (sel.equals("1")) {
            // run pvp is user selects it
            twoPlayer();
        } else if (sel.equals("2")) {
            // runs pvc if user selects
            onePlayer();
        }
        ui.close();
    }

    // Pvp
    public static void twoPlayer() {
        Scanner ui = new Scanner(System.in);
        System.out.println("input 'r','p','s' for rock,papper,sisors");
        System.out.print("User 1: ");
        // user 1 input
        String u1 = ui.nextLine();
        System.out.print("User 2: ");
        // user 2 in put
        String u2 = ui.nextLine();
        // check who one
        int winner = check(u1, u2);
        // tell the user who won
        if (winner == 1) {
            System.out.println("User 1 won!");
        } else if (winner == 2) {
            System.out.println("User 2 won!");
        } else {
            System.out.println("It's a tie!");
        }
        ui.close();
    }

    // Pvc
    public static void onePlayer() {
        Scanner ui = new Scanner(System.in);
        System.out.println("input 'r','p','s' for rock,papper,sisors");
        System.out.print("User: ");
        // user inputs selection
        String u1 = ui.nextLine();

        String[] compSelStrings = { "r", "p", "s" };
        // int winner = check(u1, u2);
        Random rnd = new Random();
        int comp = rnd.nextInt(3);
        // computer makes selection
        String compSel = compSelStrings[comp];
        // tell user what the computer chose
        System.out.println("Computer: " + compSel);
        int winner = check(u1, compSel);
        // tell the user who won
        if (winner == 1) {
            System.out.println("User won!");
        } else if (winner == 2) {
            System.out.println("Computer won!");
        } else {
            System.out.println("It's a tie!");
        }
        ui.close();
    }

    // checks for winner
    // r>s,p>r,s>p
    // 0=tie,1=u1 win,2=u2 win
    public static int check(String u1, String u2) {
        int winner = 0;
        // u1 r
        if (u1.equals("r")) {
            if (u2.equals("r")) {
                winner = 0;
            } else if (u2.equals("p")) {
                winner = 2;
            } else if (u2.equals("s")) {
                winner = 1;
            }
        }
        // u1 p
        else if (u1.equals("p")) {
            if (u2.equals("r")) {
                winner = 1;
            } else if (u2.equals("p")) {
                winner = 0;
            } else if (u2.equals("s")) {
                winner = 2;
            }
        }
        // u1 s
        else if (u1.equals("s")) {
            if (u2.equals("r")) {
                winner = 2;
            } else if (u2.equals("p")) {
                winner = 1;
            } else if (u2.equals("s")) {
                winner = 0;
            }
        }

        return winner;
    }
}
