#include <stdio.h>
#include <string.h>

int main() {
    // 打印欢迎信息
    printf("欢迎使用简单的C程序！\n");
    printf("===================\n");
    
    // 声明变量
    char name[100];
    int age;
    float height;
    
    // 获取用户输入
    printf("请输入您的姓名: ");
    fgets(name, sizeof(name), stdin);
    // 移除换行符
    name[strcspn(name, "\n")] = 0;
    
    printf("请输入您的年龄: ");
    scanf("%d", &age);
    
    printf("请输入您的身高(米): ");
    scanf("%f", &height);
    
    // 输出用户信息
    printf("\n个人信息摘要:\n");
    printf("姓名: %s\n", name);
    printf("年龄: %d 岁\n", age);
    printf("身高: %.2f 米\n", height);
    
    // 简单的计算
    if (age >= 18) {
        printf("状态: 成年人\n");
    } else {
        printf("状态: 未成年人\n");
    }
    
    // BMI范围提示（假设合理体重）
    float ideal_weight_min = (height * height) * 18.5;
    float ideal_weight_max = (height * height) * 24.9;
    printf("建议体重范围: %.1f - %.1f 公斤\n", ideal_weight_min, ideal_weight_max);
    
    printf("\n谢谢使用！\n");
    
    return 0;
}