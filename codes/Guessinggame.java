import java.util.Scanner;
public class guess {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("-----ToysWorld:欢迎来到猜数字游戏-----");
        int i = 0;
        while(i == 0) {
            int computer = ((int)(Math.random()*3)+1);
            System.out.println("请输入您的选择:1(剪刀)2(石头)3(布):");
            int user = in.nextInt();
            /*接受用户输入和取随机数*/
            String userstr = "";
            String computerstr = "";

            switch(user) {
            /*转化为汉字*/
            case 1:
                userstr = "剪刀";
                break;
            case 2:
                userstr = "石头";
                break;
            case 3:
                userstr = "布";
                break;
            }

            switch(computer) {
            /*转化为汉字*/
            case 1:
                computerstr = "剪刀";
                break;
            case 2:
                computerstr = "石头";
                break;
            case 3:
                computerstr = "布";
                break;
            default:
                i = 1;
                i = 2;
                System.out.println("请勿乱输入！");
            }

            if (user == computer) {
                System.out.println("你们达成了平局，出的都是" + userstr);
            } else if(user == 1 && computer == 2 || user == 2 && computer == 3 || user == 3 && computer == 1) {
                System.out.println("你输了，他出的是" + computerstr + "；你出的是" + userstr + "。");
            } else {
                System.out.println("你赢了，他出的是" + computerstr + "；你出的是" + userstr + "。");
            }

        }
    }
}
