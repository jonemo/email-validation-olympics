#!/usr/bin/env node
const fs = require('fs');
const validator = require('email-validator');

const content = fs.readFileSync(process.argv[2], 'utf-8');
for (const line of content.split('\n')) {
    const email = line.replace(/\r$/, '');
    if (!email) continue;
    const result = validator.validate(email) ? 'valid   ' : 'invalid ';
    console.log(`${result}${email}`);
}
