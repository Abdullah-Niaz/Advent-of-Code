// index.js
const fs = require('fs');

const formatInput = input =>
    input
        .trim()
        .split('\n')
        .map(line => line.split(' ').map(Number))

function isDecreasingCorrectly(arr) {
    for (let i = 0; i < arr.length - 1; i++) {
        const diff = arr[i] - arr[i + 1]
        if (diff <= 0 || diff >= 4) return false
    }
    return true
}

function isIncreasingCorrectly(arr) {
    return isDecreasingCorrectly(arr.reverse())
}

function isRowSafe(arr) {
    return isDecreasingCorrectly(arr) || isIncreasingCorrectly(arr)
}

function solution1(input) {
    const rows = formatInput(input)
    return rows.filter(isRowSafe).length
}

function getRowPermutations(arr) {
    return arr.map((_, idx) => arr.slice(0, idx).concat(arr.slice(idx + 1)))
}

function solution2(input) {
    const rows = formatInput(input)
    return rows.filter(
        row => isRowSafe(row) || getRowPermutations(row).some(isRowSafe)
    ).length
}

// Read input from input.txt
fs.readFile('input.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file:', err)
        return
    }


    console.log(solution1(data))
    console.log(solution2(data))

})
