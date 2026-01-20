#!/usr/bin/env node
const fs = require('fs');
const { validate } = require('deep-email-validator');

async function main() {
    const inputFile = process.argv[2];
    const content = fs.readFileSync(inputFile, 'utf-8');
    const lines = content.split('\n');

    for (const line of lines) {
        const email = line.replace(/\r$/, '');
        if (!email) continue;

        const result = await validate({
            email,
            validateRegex: true,
            validateMx: false,
            validateTypo: false,
            validateDisposable: false,
            validateSMTP: false
        });
        const prefix = result.valid ? 'valid   ' : 'invalid ';
        console.log(`${prefix}${email}`);
    }
}

main();
