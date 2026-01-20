package main

import (
	"bufio"
	"fmt"
	"net/mail"
	"os"
)

func validate(email string) bool {
	_, err := mail.ParseAddress(email)
	return err == nil
}

func main() {
	if len(os.Args) < 2 {
		fmt.Fprintln(os.Stderr, "Usage: validate <addresslist.txt>")
		os.Exit(1)
	}

	// Quick check mode
	if os.Args[1] == "--check" {
		if validate("foo@example.com") {
			os.Exit(0)
		}
		os.Exit(1)
	}

	file, err := os.Open(os.Args[1])
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error opening file: %v\n", err)
		os.Exit(1)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		email := scanner.Text()
		if email == "" {
			continue
		}

		result := "invalid "
		if validate(email) {
			result = "valid   "
		}
		fmt.Printf("%s%s\n", result, email)
	}
}
