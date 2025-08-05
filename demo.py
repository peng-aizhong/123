#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的Python程序演示版本
自动运行，无需用户输入
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
    """主函数 - 演示版本"""
    print("=" * 50)
    print("简单Python程序 - 演示版本")
    print("=" * 50)
    
    # 问候演示
    print(greet("小明"))
    
    print("\n计算器功能演示：")
    
    # 演示各种计算
    calculations = [
        (10, 5, '+'),
        (10, 5, '-'),
        (10, 5, '*'),
        (10, 5, '/'),
        (10, 0, '/'),  # 除零演示
    ]
    
    for a, b, op in calculations:
        result = calculate(a, b, op)
        print(f"{a} {op} {b} = {result}")
    
    # 列表操作演示
    print("\n列表操作演示：")
    fruits = ["苹果", "香蕉", "橙子", "葡萄", "草莓"]
    print(f"水果列表: {fruits}")
    print(f"第一个水果: {fruits[0]}")
    print(f"最后一个水果: {fruits[-1]}")
    print(f"水果总数: {len(fruits)}")
    
    # 字符串操作演示
    print("\n字符串操作演示：")
    message = "Python编程很有趣！"
    print(f"原始字符串: {message}")
    print(f"字符串长度: {len(message)}")
    print(f"转换为大写: {message.upper()}")
    print(f"重复3次: {message * 3}")
    
    # 循环演示
    print("\n循环演示 - 数字1到5：")
    for i in range(1, 6):
        print(f"数字: {i}, 平方: {i**2}")
    
    print("\n感谢使用这个简单的Python程序！")

if __name__ == "__main__":
    main()