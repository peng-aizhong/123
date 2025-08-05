#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的Python程序示例
包含基本的功能演示
"""

def greet(name):
    """问候函数"""
    return f"你好，{name}！欢迎使用这个简单的Python程序。"

def calculate(a, b, operation):
    """简单的计算器函数"""
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "错误：除数不能为零"
    else:
        return "错误：不支持的操作"

def main():
    """主函数"""
    print("=" * 40)
    print("欢迎使用简单Python程序")
    print("=" * 40)
    
    # 问候用户
    name = input("请输入你的名字: ")
    print(greet(name))
    
    print("\n让我们做一些简单的计算：")
    
    try:
        # 获取用户输入
        num1 = float(input("请输入第一个数字: "))
        num2 = float(input("请输入第二个数字: "))
        op = input("请选择操作 (+, -, *, /): ")
        
        # 计算结果
        result = calculate(num1, num2, op)
        print(f"\n计算结果: {num1} {op} {num2} = {result}")
        
    except ValueError:
        print("错误：请输入有效的数字")
    
    # 显示一些有趣的信息
    print("\n一些有趣的Python信息：")
    print(f"Python版本信息可以通过 sys.version 查看")
    print(f"当前程序文件名: {__file__}")
    
    # 简单的列表操作演示
    fruits = ["苹果", "香蕉", "橙子", "葡萄"]
    print(f"\n水果列表: {fruits}")
    print(f"第一个水果: {fruits[0]}")
    print(f"水果总数: {len(fruits)}")
    
    print("\n感谢使用这个简单的Python程序！")

if __name__ == "__main__":
    main()