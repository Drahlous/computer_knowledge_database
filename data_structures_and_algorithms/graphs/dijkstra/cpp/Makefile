CC 		= g++
CFLAGS 	= -g

objects = dijkstra.o

default: all
all: bin

bin: $(objects)
	$(CC) $(CFLAGS) -o bin $(objects)

dijkstra.o:

.PHONY: test
test: bin
	./bin


.PHONY: clean
clean:
	-@rm bin *.puml *.png $(objects) 2>/dev/null || true

