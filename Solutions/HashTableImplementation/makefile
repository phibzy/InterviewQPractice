CC = clang
CFLAGS = -Wall -Werror -Wextra -O

default: hash

hash:	hash.o test.o
		$(CC) $(CFLAGS) -o hash hash.o test.o

hash.o:	hash.c hash.h
		$(CC) $(CFLAGS) -c hash.c

test.o:	test.c hash.h
		$(CC) $(CFLAGS) -c test.c
