#!/usr/bin/env node
/**
 * Validate email addresses using Zod
 */

const fs = require('fs');
const { z } = require('zod');

const emailSchema = z.string().email();

function validate(email) {
    const result = emailSchema.safeParse(email);
    return result.success;
}

function main() {
    if (process.argv.length < 3) {
        console.error('Usage: validate.js <addresslist.txt>');
        process.exit(1);
    }

    const inputFile = process.argv[2];
    const content = fs.readFileSync(inputFile, 'utf-8');
    const lines = content.split('\n');

    for (const line of lines) {
        const email = line.replace(/\r$/, '');  // Handle CRLF
        if (!email) continue;

        const result = validate(email) ? 'valid   ' : 'invalid ';
        console.log(`${result}${email}`);
    }
}

main();
