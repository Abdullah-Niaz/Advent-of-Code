const fs = require('fs');
const path = require('path');

// Function to sum an array of numbers
function sum(array) {
    return array.reduce((acc, num) => acc + num, 0);
}

// Function to read input from `input.txt`
function getInput(dirname) {
    const filePath = path.join(dirname, 'input.txt');
    try {
        return fs.readFileSync(filePath, 'utf8');
    } catch (err) {
        console.error(`Error reading input file: ${err.message}`);
        process.exit(1);
    }
}

const data = getInput(__dirname);

function formatInput(input) {
    const tuples = input
        .trim()
        .split('\n')
        .map(line => line.split(/\s+/).map(Number));

    const left = [];
    const right = [];

    for (const [a, b] of tuples) {
        left.push(a);
        right.push(b);
    }

    return [left, right];
}

function solution1(input) {
    const [left, right] = formatInput(input);

    const sortedLeft = left.slice().sort((a, b) => a - b); // `toSorted` alternative
    const sortedRight = right.slice().sort((a, b) => a - b);

    const distances = [];
    for (let i = 0; i < sortedLeft.length; i++) {
        distances.push(Math.abs(sortedLeft[i] - sortedRight[i]));
    }

    return sum(distances);
}

function solution2(input) {
    const [left, right] = formatInput(input);

    const rightCounts = {};

    for (const num of right) {
        if (rightCounts[num] === undefined) {
            rightCounts[num] = 0;
        }

        rightCounts[num]++;
    }

    let total = 0;
    for (const num of left) {
        const count = rightCounts[num] ?? 0;
        total += num * count;
    }

    return total;
}

// Test cases
const testInput = `
3   4
4   3
2   5
1   3
3   9
3   3
`;

function test(description, callback) {
    try {
        callback();
        console.log(`✔ ${description}`);
    } catch (error) {
        console.error(`✘ ${description}`);
        console.error(error);
    }
}

test('solution1', () => {
    if (solution1(testInput) !== 11) {
        throw new Error(`Expected 11, got ${solution1(testInput)}`);
    }
});

test('solution2', () => {
    if (solution2(testInput) !== 31) {
        throw new Error(`Expected 31, got ${solution2(testInput)}`);
    }
});


console.log('Solution 1 Output:', solution1(data));
console.log('Solution 2 Output:', solution2(data)); 
