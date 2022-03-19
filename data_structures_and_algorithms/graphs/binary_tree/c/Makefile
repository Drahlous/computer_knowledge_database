CC = gcc
CFLAGS = -g

objects = binary_tree.o

default: all
all: bin

bin: $(objects)
	$(CC) $(CFLAGS) -o bin $(objects)

binary_tree.o: binary_tree.h

.PHONY: test
test: bin
	./bin 10 5 15

.PHONY: puml
puml: bin
	./bin 10 5 15 20 21 11 7 3 6 > treeDiagram.puml
	java -jar ~/.local/bin/plantuml.jar treeDiagram.puml
	feh treeDiagram.png

.PHONY: puml-live
puml-live: bin
	./bin 10 5 15 20 21 11 7 3 6 > treeDiagram.puml
	water-uml live treeDiagram.puml

.PHONY: clean
clean:
	-@rm bin *.puml *.png $(objects) 2>/dev/null || true

