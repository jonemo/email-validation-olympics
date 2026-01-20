#!/usr/bin/env php
<?php
/**
 * Email validation using egulias/email-validator with RFCValidation.
 * This is a syntax-only check, no DNS/SMTP verification.
 */

require_once __DIR__ . '/vendor/autoload.php';

use Egulias\EmailValidator\EmailValidator;
use Egulias\EmailValidator\Validation\RFCValidation;

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

$validator = new EmailValidator();
$rfcValidation = new RFCValidation();

while (($line = fgets($handle)) !== false) {
    $email = rtrim($line, "\r\n");

    if ($email === '') {
        continue;
    }

    $result = $validator->isValid($email, $rfcValidation) ? 'valid   ' : 'invalid ';
    echo $result . $email . "\n";
}

fclose($handle);
