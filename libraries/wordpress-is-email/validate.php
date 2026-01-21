#!/usr/bin/env php
<?php
/**
 * Email validation using WordPress's is_email() function.
 *
 * This loads the actual WordPress is_email() function from wordpress-core,
 * with minimal stubs for WordPress functions it depends on.
 */

if ($argc < 2) {
    fwrite(STDERR, "Usage: php validate.php <addresslist>\n");
    exit(1);
}

// Stub WordPress functions that is_email() depends on
if (!function_exists('apply_filters')) {
    /**
     * Stub for WordPress apply_filters - just returns the first argument unchanged.
     */
    function apply_filters($hook_name, $value, ...$args) {
        return $value;
    }
}

if (!function_exists('_deprecated_argument')) {
    /**
     * Stub for WordPress _deprecated_argument - does nothing.
     */
    function _deprecated_argument($function_name, $version, $message = '') {
        // Silently ignore deprecated argument warnings
    }
}

// Load WordPress's is_email() function
require_once __DIR__ . '/formatting.php';

// Validate emails
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

    $result = is_email($email) !== false ? 'valid   ' : 'invalid ';
    echo $result . $email . "\n";
}

fclose($handle);
