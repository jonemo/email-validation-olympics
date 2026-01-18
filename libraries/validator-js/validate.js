#!/usr/bin/env node
/**
 * Validate email addresses using validator.js
 */

const fs = require('fs');
const validator = require('validator');

function validate(email) {
    return validator.isEmail(email);
}

function parseCSVLine(line) {
    const result = [];
    let current = '';
    let inQuotes = false;

    for (const char of line) {
        if (char === '"') {
            inQuotes = !inQuotes;
        } else if (char === ',' && !inQuotes) {
            result.push(current);
            current = '';
        } else {
            current += char;
        }
    }
    result.push(current);
    return result;
}

function main() {
    if (process.argv.length < 3) {
        console.error('Usage: validate.js <addresslist.csv>');
        process.exit(1);
    }

    const inputFile = process.argv[2];
    const content = fs.readFileSync(inputFile, 'utf-8');
    const lines = content.split('\n');

    // Output CSV header
    console.log('email,expected,actual,match');

    for (const line of lines) {
        if (!line.trim()) continue;

        const row = parseCSVLine(line);
        const email = row[0] || '';
        const expected = (row[1] || '').trim().toLowerCase();

        const actual = validate(email) ? 'valid' : 'invalid';
        const match = actual === expected ? 'true' : 'false';

        // Quote email if it contains comma
        const emailOut = email.includes(',') ? `"${email}"` : email;
        console.log(`${emailOut},${expected},${actual},${match}`);
    }
}

main();
