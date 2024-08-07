CC = gcc
CFLAGS = -Wall -Iinclude -w

all: stack-vm

stack-vm: src/*.c
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm -f stack-vm
