#!/bin/bash

# TODO: This guide is a work in progress




# Numberic
echo {1..10}
echo {1..10..2}

# Alpha
echo {A..Z}
echo {A..Z..2}

# Arbitrary Strings
echo {first,second,third}

# Combining Sets
echo {{A..C},{1..3}}

# Prefix
echo sample_prefix_{A..C}

# Prefix
echo sample_prefix_{A..C}

# Suffix
echo {A..C}_sample_suffix

# Newline Separated
for item in {A..C}; do echo "$item"; done

### Usecases

# Hex Digits
echo {{0..9},{A..F}}

