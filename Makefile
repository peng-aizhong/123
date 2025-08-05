# 编译器
CC = gcc

# 编译选项
CFLAGS = -Wall -Wextra -std=c99

# 目标文件
TARGET = hello

# 源文件
SOURCE = hello.c

# 默认目标
all: $(TARGET)

# 编译规则
$(TARGET): $(SOURCE)
	$(CC) $(CFLAGS) -o $(TARGET) $(SOURCE)

# 运行程序
run: $(TARGET)
	./$(TARGET)

# 清理生成的文件
clean:
	rm -f $(TARGET)

# 声明伪目标
.PHONY: all run clean