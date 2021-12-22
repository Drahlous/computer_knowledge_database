#!/bin/bash

echo '
There are a few different ways to generate sequences in the terminal.
If you want to generate a sequence of numbers, you might use 
    $seq

For example, say you want all of the numbers up until 5
    $seq 5'
seq 5


echo '
What if we want a range of numbers? Maybe 7 through 13
    $seq 7 13'
seq 7 13



echo '
Finally, we might want to provide a step-size.
Maybe we want all even numbers from 0 through 10
    $seq 0 2 10'
seq 0 2 10


echo '
If we do not want to use the seq command, we can get similar results with bash brace-expansion.
    $echo {1..5}'
echo {1..5}

echo '
    $echo {7..13}'
echo {7..13}

echo '
    $echo {0..2..10}'
echo {0..10..2}


echo '
Note however that sequences generated with this method are separated with spaces rather than newlines.
If we want to get the newlines back, we can wrap the statement in a for-loop
    $for num in {1..5}; do echo "$num"; done'
for num in {1..5}; do echo "$num"; done

echo '
A major advantage of using bash brace-expansion is that it allows us to generate sequences from non-numerical sets
    $echo {A..Z}'
echo {A..Z}


echo '
You can use the same step-size syntax for these sets as well
    $echo {A..Z..2}'
echo {A..Z..2}

