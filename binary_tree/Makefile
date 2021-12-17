CC 		= gcc
CFLAGS 	= -g

objects = binary_tree.o

default: all
all: bin

bin: $(objects)
	$(CC) $(CFLAGS) -o bin $(objects)

binary_tree.o: binary_tree.h

.PHONY: test
test:
	./bin

.PHONY: clean
clean:
	rm bin $(objects)

