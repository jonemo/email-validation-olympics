use email_address::EmailAddress;
use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::process;

fn validate(email: &str) -> bool {
    EmailAddress::is_valid(email)
}

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        eprintln!("Usage: emailvalidator <addresslist.txt>");
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

    let reader = BufReader::new(file);
    for line in reader.lines() {
        let email = line.unwrap();
        if email.is_empty() {
            continue;
        }

        let result = if validate(&email) { "valid   " } else { "invalid " };
        println!("{}{}", result, email);
    }
}
