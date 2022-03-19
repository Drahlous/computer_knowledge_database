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

.PHONY: puml
puml: bin
	./bin > listDiagram.puml
	java -jar ~/.local/bin/plantuml.jar listDiagram.puml
	feh -E 100 -y 500 -s -m  listDiagram*

.PHONY: clean
clean:
	-@rm bin *.puml *.png $(objects) 2>/dev/null || true

