#!/bin/bash

echo '
Bash offers a built-in command for generating sequences from a range of numbers, characters, or arbitrary strings.
This feature is called "Brace Expansion"'

# Numeric
echo '

You might use it to generate a sequence of numbers as follows.
    $echo {0..10}'
echo {0..10}

echo '
A step-size can be included to print a subset of the range.
This is shown below to print only even numbers.
    $echo {0..10..2}'
echo {0..10..2}


# Alphabetic
echo '

The same syntax can be used for ranges of alphabetic characters
    $echo {A..Z}'
echo {A..Z}

echo '
    $echo {A..Z..2}'
echo {A..Z..2}


# Arbitrary & Combined Sets
echo '

The brace expansion is not limited to sequential ranges of characters.
It can also be used to define an arbitrary set of strings
    $echo {first,second,third}'
echo {first,second,third}

echo '
Sets can be combined into super-sets as needed
    $echo {{A..C},{1..3},{first,second,third}}'
echo {{A..C},{1..3},{first,second,third}}


# Prefix & Suffix
echo '

Finally, the expansion syntax supports the addition of prefixes and suffixes
    $echo sample_prefix_{A..C}'
echo sample_prefix_{A..C}

echo '
    $echo {A..C}_sample_suffix'
echo {1..3}_sample_suffix


# Newline Separated
echo '

If you need items to be separated on newlines (like the output of seq), you can wrap the expression in a for-loop
    for item in {A..C}; do echo "$item"; done'
for item in {A..C}; do echo "$item"; done



### Usecases
echo '

--- Example Usecases ---'



echo '
Generate a set of temp files
    $touch temp_file_{A..C}.txt

Generate a set of directories
    $mkdir -p ./new_dir/{A..C}
'

# Hex Digits
echo '
Print all of the hex digits
    $echo {{0..9},{A..F}}'
echo {{0..9},{A..F}}

echo '
Print all possible 2-digit hex values
    $echo {{0..9},{A..F}}{{0..9},{A..F}}'
echo {{0..9},{A..F}}{{0..9},{A..F}}

