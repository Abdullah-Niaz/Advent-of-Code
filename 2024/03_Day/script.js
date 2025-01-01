const fs = require('fs');
const path = require('path');

// Helper function to add numbers
const add = (a, b) => a + b;

// Read input from input.txt
const inputFilePath = path.join(__dirname, 'input.txt');
const data = fs.readFileSync(inputFilePath, 'utf-8');

// Helper function to format input
const formatInput = (input) => input.trim().split('\n');

// Regular expression to match "mul(x, y)"
const MUL_PATTERN = /mul\(\d{1,3},\d{1,3}\)/g;

// Function to calculate the sum of multiplication matches
function sumMuls(muls) {
    return muls
        .map(match => {
            const [x, y] = match
                .replace('mul(', '')
                .replace(')', '')
                .split(',')
                .map(Number);

            return x * y;
        })
        .reduce(add, 0);
}


function solution1(input) {
    const lines = formatInput(input);
    const matches = lines.flatMap(line => line.match(MUL_PATTERN));
    return sumMuls(matches);
}

// Regular expression to match "mul(x, y)", "do()", and "don't()"
const MUL_DO_DONT_PATTERN = /mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)/g;

function solution2(input) {
    const lines = formatInput(input);
    const matches = lines.flatMap(line => line.match(MUL_DO_DONT_PATTERN));

    const kept = [];
    let keeping = true;
    for (const match of matches) {
        if (match === 'do()') {
            keeping = true;
            continue;
        }

        if (match === "don't()") {
            keeping = false;
            continue;
        }

        if (keeping) {
            kept.push(match);
        }
    }

    return sumMuls(kept);
}


console.log('Solution 1 Result:', solution1(data));
console.log('Solution 2 Result:', solution2(data)); 
