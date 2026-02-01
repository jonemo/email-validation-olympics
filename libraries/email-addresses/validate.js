#!/usr/bin/env node
const fs = require('fs');
const addrs = require('email-addresses');

function validate(email) {
    // parseOneAddress returns an object if valid, null if invalid
    // This parses according to RFC 5322 (full email address format)
    const result = addrs.parseOneAddress(email);
    return result !== null;
}

const content = fs.readFileSync(process.argv[2], 'utf-8');
for (const line of content.split('\n')) {
    const email = line.replace(/\r$/, '');
    if (!email) continue;
    const result = validate(email) ? 'valid   ' : 'invalid ';
    console.log(`${result}${email}`);
}
