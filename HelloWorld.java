public class HelloWorld {
    public static void main(String[] args) {
        // 打印欢迎信息
        System.out.println("欢迎使用Java程序！");
        
        // 演示基本数据类型
        int number = 42;
        String message = "Hello, World!";
        double pi = 3.14159;
        
        System.out.println("数字: " + number);
        System.out.println("消息: " + message);
        System.out.println("圆周率: " + pi);
        
        // 演示简单的计算
        int a = 10;
        int b = 5;
        int sum = a + b;
        int product = a * b;
        
        System.out.println(a + " + " + b + " = " + sum);
        System.out.println(a + " * " + b + " = " + product);
        
        // 演示条件语句
        if (sum > 10) {
            System.out.println("和大于10");
        } else {
            System.out.println("和小于或等于10");
        }
        
        // 演示循环
        System.out.println("计数到5:");
        for (int i = 1; i <= 5; i++) {
            System.out.print(i + " ");
        }
        System.out.println();
        
        System.out.println("程序执行完毕！");
    }
}