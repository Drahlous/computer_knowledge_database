CC 		= gcc
CFLAGS 	= -g

objects = linked_list.o

default: all
all: bin

bin: $(objects)
	$(CC) $(CFLAGS) -o bin $(objects)

linked_list.o: linked_list.h

.PHONY: clean
clean:
	rm bin $(objects)

