#!/usr/bin/env php
<?php
/**
 * Email validation using Symfony Validator component with strict mode.
 * Strict mode uses egulias/email-validator for RFC 5322 compliance.
 * This is a syntax-only check, no DNS/SMTP verification.
 */

require_once __DIR__ . '/vendor/autoload.php';

use Symfony\Component\Validator\Constraints\Email;
use Symfony\Component\Validator\Validation;

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

$validator = Validation::createValidator();
$constraint = new Email(['mode' => Email::VALIDATION_MODE_STRICT]);

while (($line = fgets($handle)) !== false) {
    $email = rtrim($line, "\r\n");

    if ($email === '') {
        continue;
    }

    $violations = $validator->validate($email, $constraint);
    $result = count($violations) === 0 ? 'valid   ' : 'invalid ';
    echo $result . $email . "\n";
}

fclose($handle);
