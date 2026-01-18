package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	emailverifier "github.com/AfterShip/email-verifier"
)

var verifier = emailverifier.NewVerifier().DisableSMTPCheck().DisableDomainSuggest().DisableAutoUpdateDisposable()

func validate(email string) bool {
	ret, _ := verifier.Verify(email)
	if ret == nil {
		return false
	}
	return ret.Syntax.Valid
}

func parseCSVLine(line string) []string {
	var result []string
	var current strings.Builder
	inQuotes := false

	for _, char := range line {
		switch {
		case char == '"':
			inQuotes = !inQuotes
		case char == ',' && !inQuotes:
			result = append(result, current.String())
			current.Reset()
		default:
			current.WriteRune(char)
		}
	}
	result = append(result, current.String())
	return result
}

func main() {
	if len(os.Args) < 2 {
		fmt.Fprintln(os.Stderr, "Usage: validate <addresslist.csv>")
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

	fmt.Println("email,expected,actual,match")

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if strings.TrimSpace(line) == "" {
			continue
		}

		row := parseCSVLine(line)
		email := row[0]
		expected := ""
		if len(row) > 1 {
			expected = strings.ToLower(strings.TrimSpace(row[1]))
		}

		actual := "invalid"
		if validate(email) {
			actual = "valid"
		}

		match := "false"
		if actual == expected {
			match = "true"
		}

		// Quote email if it contains comma
		emailOut := email
		if strings.Contains(email, ",") {
			emailOut = fmt.Sprintf(`"%s"`, email)
		}
		fmt.Printf("%s,%s,%s,%s\n", emailOut, expected, actual, match)
	}
}
