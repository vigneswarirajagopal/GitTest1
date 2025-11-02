#!/bin/bash

# Read input
read -p "Enter a number: " num

# Initialize factorial to 1
fact=1

# Loop to calculate factorial
for (( i=1; i<=num; i++ ))
do
  fact=$((fact * i))
done

# Output the result
echo "Factorial of $num is: $fact"
