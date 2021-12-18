# Data Structures and Algorithms Practice



## PlantUML Diagrams


### Install Pre-requisites:
```bash
# Install Java
sudo apt install default-jre

# Install Graphvis
sudo apt install graphviz

# Download PlantUML jar to ~/.local/bin/plantuml.jar
curl -L -o ~/.local/bin/plantuml.jar https://sourceforge.net/projects/plantuml/files/plantuml.jar/download

# Check that PlantUML is installed correctly
java -jar ~/.local/bin/plantuml.jar

# Install feh to view output PNG
sudo apt install feh

# Alternative: Use water-uml to render a live view
sudo npm i -g water-plant-uml

```

### Generate Diagrams from puml file
```bash
# Render a PUML file into a PNG
java -jar ~/.local/bin/plantuml.jar exampleDiagram.puml

# View the PNG
feh exampleDiagram.png

# Live View:
water-uml live exampleDiagram.puml
```


