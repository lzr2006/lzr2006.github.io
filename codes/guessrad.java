import java.util.Scanner;
public class guess {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int computer = (int)(Math.random()*100) + 1;
        int count = 1;
        System.out.println("-----ToysWorld:欢迎来到猜数字游戏-----");
        while(true) {
            System.out.println("请输入您猜的的数字(1-100)");
            int user = in.nextInt();
            if(user == computer) {
                System.out.println("恭喜，猜对了。答案是" + computer + "，你一共猜了" + count + "次。");
                break;
            } else if(user < computer) {
                System.out.println("你的数字小了，已经猜了" + count + "次。");
                count++;
            } else if(user > computer) {
                System.out.println("你的数字大了，已经猜了" + count + "次。");
                count++;
            } else {
                System.out.println("woc?");
            }
        }
    }
}
