#!/usr/bin/env php
<?php
/**
 * Email validation using PHP's built-in filter_var() with FILTER_VALIDATE_EMAIL.
 * This is a syntax-only check, no DNS/SMTP verification.
 */

if ($argc < 2) {
    fwrite(STDERR, "Usage: php validate.php <addresslist>\n");
    exit(1);
}

$filepath = $argv[1];
$handle = fopen($filepath, 'r');

if ($handle === false) {
    fwrite(STDERR, "Error: Cannot open file: $filepath\n");
    exit(1);
}

while (($line = fgets($handle)) !== false) {
    $email = rtrim($line, "\r\n");

    if ($email === '') {
        continue;
    }

    $result = filter_var($email, FILTER_VALIDATE_EMAIL) !== false ? 'valid   ' : 'invalid ';
    echo $result . $email . "\n";
}

fclose($handle);
