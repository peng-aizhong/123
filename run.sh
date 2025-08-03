#!/bin/bash

echo "编译Java程序..."
javac HelloWorld.java

if [ $? -eq 0 ]; then
    echo "编译成功！"
    echo "运行程序..."
    echo "=================="
    java HelloWorld
    echo "=================="
    echo "程序执行完成！"
else
    echo "编译失败！"
    exit 1
fi