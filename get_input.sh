#!/bin/bash

read -p "Enter your Advent of Code Cookie: " session_cookie
read -p "Enter the Year (e.g. 2024): " year
read -p "Enter the Day" day

day = $(printf "%d", "$day")

url="https://adventofcode.com/$year/day/$day/input"
output_file="input_day${day}_$year.txt"

echo "Fetching input from $url..."

curl -s -b "session=$session_cookie" "$url" -o "$output_file"

if [[ $? -eq 0 ]]; then
  echo "Input for Day $day, $year saved to $output_file."
else
  echo "Failed to fetch input. Please check your session cookie, year, and day."
fi

mv "$output_file" "$year"
