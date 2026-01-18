use email_address::EmailAddress;
use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::process;

fn validate(email: &str) -> bool {
    EmailAddress::is_valid(email)
}

fn parse_csv_line(line: &str) -> Vec<String> {
    let mut result = Vec::new();
    let mut current = String::new();
    let mut in_quotes = false;

    for ch in line.chars() {
        match ch {
            '"' => in_quotes = !in_quotes,
            ',' if !in_quotes => {
                result.push(current.clone());
                current.clear();
            }
            _ => current.push(ch),
        }
    }
    result.push(current);
    result
}

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        eprintln!("Usage: emailvalidator <addresslist.csv>");
        process::exit(1);
    }

    // Quick check mode
    if args[1] == "--check" {
        if validate("foo@example.com") {
            process::exit(0);
        }
        process::exit(1);
    }

    let file = File::open(&args[1]).unwrap_or_else(|e| {
        eprintln!("Error opening file: {}", e);
        process::exit(1);
    });

    println!("email,expected,actual,match");

    let reader = BufReader::new(file);
    for line in reader.lines() {
        let line = line.unwrap();
        if line.trim().is_empty() {
            continue;
        }

        let row = parse_csv_line(&line);
        let email = &row[0];
        let expected = row.get(1).map(|s| s.trim().to_lowercase()).unwrap_or_default();

        let actual = if validate(email) { "valid" } else { "invalid" };
        let matched = if actual == expected { "true" } else { "false" };

        // Quote email if it contains comma
        let email_out = if email.contains(',') {
            format!("\"{}\"", email)
        } else {
            email.clone()
        };

        println!("{},{},{},{}", email_out, expected, actual, matched);
    }
}
