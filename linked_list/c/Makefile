CC 		= gcc
CFLAGS 	= -g

objects = linked_list.o

default: all
all: bin

bin: $(objects)
	$(CC) $(CFLAGS) -o bin $(objects)

linked_list.o: linked_list.h

.PHONY: test
test: bin
	./bin

.PHONY: clean
clean:
	-@rm bin *.puml *.png $(objects) 2>/dev/null || true

