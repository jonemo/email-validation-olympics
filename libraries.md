## The Libraries

| Name                         | Repository                                                                            | Package                                                                                 | Language   |
| ---------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ---------- |
| **validator.js**             | [validatorjs/validator.js](https://github.com/validatorjs/validator.js)               | [NPM](https://www.npmjs.com/package/validator)                                          | JavaScript |
| **deep-email-validator**     | [mfbx9da4/deep-email-validator](https://github.com/mfbx9da4/deep-email-validator)     | [NPM](https://www.npmjs.com/package/deep-email-validator)                               | TypeScript |
| **email-validator**          | [manishsaraan/email-validator](https://github.com/manishsaraan/email-validator)       | [NPM](https://www.npmjs.com/package/email-validator)                                    | JavaScript |
| **Zod**                      | [colinhacks/zod](https://github.com/colinhacks/zod)                                   | [NPM](https://www.npmjs.com/package/zod)                                                | JavaScript |
| **Joi**                      | [hapijs/joi](https://github.com/hapijs/joi)                                           | [NPM](https://www.npmjs.com/package/joi)                                                | JavaScript |
| **python-email-validator**   | [JoshData/python-email-validator](https://github.com/JoshData/python-email-validator) | [PyPI](https://pypi.org/project/email-validator/)                                       | Python     |
| **pyIsEmail**                | [michaelherold/pyIsEmail](https://github.com/michaelherold/pyIsEmail)                 | [PyPI](https://pypi.org/project/pyIsEmail/)                                             | Python     |
| **PHP** `filter_var()`       | N/A                                                                                   | N/A                                                                                     | PHP        |
| **EmailValidator**           | [egulias/EmailValidator](https://github.com/egulias/EmailValidator)                   | [Packagist](https://packagist.org/packages/egulias/email-validator)                     | PHP        |
| **WordPress**                | [WordPress/WordPress](https://github.com/WordPress/WordPress)                         | N/A                                                                                     | PHP        |
| **Symfony Validator**        | [symfony/validator](https://github.com/symfony/validator)                             | [Packagist](https://packagist.org/packages/symfony/validator)                           | PHP        |
| **Apache Commons Validator** | [apache/commons-validator](https://github.com/apache/commons-validator)               |                                                                                         | Java       |
| **Hibernate Validator**      | [hibernate/hibernate-validator](https://github.com/hibernate/hibernate-validator)     | [Maven](https://mvnrepository.com/artifact/org.hibernate.validator/hibernate-validator) | Java       |
| **AfterShip/email-verifier** | [AfterShip/email-verifier](https://github.com/AfterShip/email-verifier)               |                                                                                         | Go         |
| **net/mail**                 | [golang/go](https://github.com/golang/go)                                             | [pkg.go.dev](https://pkg.go.dev/net/mail)                                               | Go         |
| **checkmail**                | [badoux/checkmail](https://github.com/badoux/checkmail)                               | [pkg.go.dev](https://pkg.go.dev/github.com/badoux/checkmail)                            | Go         |
| **truemail**                 | [truemail-rb/truemail](https://github.com/truemail-rb/truemail)                       |                                                                                         | Ruby       |
| **valid_email2**             | [micke/valid_email2](https://github.com/micke/valid_email2)                           |                                                                                         | Ruby       |
| **EmailValidation**          | [jstedfast/EmailValidation](https://github.com/jstedfast/EmailValidation)             | [NuGet](https://www.nuget.org/packages/EmailValidation/)                                | .NET       |
| **email_address**            | [johnstonskj/rust-email_address](https://github.com/johnstonskj/rust-email_address)   | [crates.io](https://crates.io/crates/email_address)                                     | Rust       |
| **validator**                | [Keats/validator](https://github.com/Keats/validator)                                 | [crates.io](https://crates.io/crates/validator)                                         | Rust       |

### validator.js

- GitHub: https://github.com/validatorjs/validator.js
- npm: https://www.npmjs.com/package/validator
- Version tested: 13.12.0

A library of string validators and sanitizers for JavaScript with over 23,000 GitHub stars.
Provides an `isEmail()` function with configurable options for allowing display names, UTF-8 local parts, and more.

Actively maintained.

### deep-email-validator

- GitHub:
- Version tested: 0.1.21, last published in 2021

Validates regex, typos, disposable, DNS, and SMTP. Node.js only.

### email-validator

- GitHub:
- Version tested: Version 2.0.4, last published in 2018

Simple, fast syntax validator.

### Zod (Javascript)

- GitHub: https://github.com/colinhacks/zod
- npm: https://www.npmjs.com/package/zod
- Version tested: 4.3.5

Zod is a Javascript object validation library that has a [field type for email addresses](https://zod.dev/api#emails):

```js
import { z } from "zod";

z.string().email();
```

Zod intentionally does not support many RFC-compliant but unusual email formats.
For example: No comments, no quotes, no IP addresses, no emojis.
From their docs:

> By default, Zod uses a comparatively strict email regex designed to validate normal email addresses containing common characters.
> It's roughly equivalent to the rules enforced by Gmail.
> To learn more about this regex, refer to [this post](https://colinhacks.com/essays/reasonable-email-regex).
>
> ```
> /^(?!\.)(?!.*\.\.)([a-z0-9_'+\-\.]*)[a-z0-9_+-]@([a-z0-9][a-z0-9\-]*\.)+[a-z]{2,}$/i
> ```

The library also bundles a handful of alternative email regexes and allows you to bring your own.

### Joi (Javascript)

https://joi.dev

Version tested: 18.0.2

Joi is another Javascript validation library that includes a [field type for email addresses](https://joi.dev/api/?v=17.13.3#stringemailoptions):

```js
const schema = Joi.string().email();
```

The documentation mentions one edge case:

> Note that quoted email addresses (e.g. "test"@example.com) are not supported and will fail validation.

### python-email-validator

- GitHub: https://github.com/JoshData/python-email-validator
- PyPI: https://pypi.org/project/email-validator/
- Version tested: 2.3.0

This is currently the most popular option in Python with over 4 million weekly downloads.
[Pydantic uses it](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.EmailStr) for its `EmailStr` field type.

The Readme declares:

> This is an opinionated library. You should definitely also consider using the less-opinionated pyIsEmail if it works better for you.

### pyIsEmail

- GitHub: https://github.com/michaelherold/pyIsEmail
- PyPI: https://pypi.org/project/pyIsEmail/
- Version tested: 2.0.1

A Python port of Dominic Sayers' `is_email` PHP library. Provides detailed diagnostic information when validation fails. The `python-email-validator` README describes itself as "opinionated" and recommends pyIsEmail as a "less-opinionated" alternative.

Supports optional DNS checking via the `check_dns` parameter, which validates that a domain has MX records.

```python
from pyisemail import is_email

# Simple validation
is_valid = is_email("test@example.com")

# With diagnostics
result = is_email("test@example.com", diagnose=True)
print(result.description)
```

### PHP Standard Library

PHP has an email validator built into the standard library:

```php
filter_var($email, FILTER_VALIDATE_EMAIL)
```

https://www.php.net/manual/en/function.filter-var.php

This advertises RFC 5321 compliance.

### WordPress (PHP)

- GitHub: https://github.com/WordPress/WordPress
- Source: [wp-includes/formatting.php](https://github.com/WordPress/WordPress/blob/master/wp-includes/formatting.php)
- Version tested: 6.7.1

The [`is_email()`](https://developer.wordpress.org/reference/functions/is_email/) function is WordPress's built-in email validator. Given WordPress powers over 40% of websites, this is likely one of the most widely executed email validation functions in existence.

```php
if (is_email($email)) {
    // Valid email
}
```

The function performs these checks:

- Minimum length of 6 characters
- Must contain `@` after the first position
- Local part: only allows `a-z0-9!#$%&'*+/=?^_`{|}~.-`
- Domain: must have at least two parts, each containing only `a-z0-9-`
- No leading/trailing hyphens or whitespace in domain parts

The docs are refreshingly honest about its limitations:

> Verifies that an email is valid.
> Does not grok i18n domains. Not RFC compliant.

Notably, WordPress rejects quoted local parts (`"hi@you"@example.com`) and IP address domains, making it stricter than RFC 5321 in some ways while being more permissive in others.

### Symfony Validator (PHP)

- GitHub: https://github.com/symfony/validator
- Packagist: https://packagist.org/packages/symfony/validator
- Docs: https://symfony.com/doc/current/reference/constraints/Email.html
- Version tested: 7.4.3

Symfony's Validator component provides an `Email` constraint with multiple validation modes. In `strict` mode, it uses [egulias/EmailValidator](https://github.com/egulias/EmailValidator) under the hood for RFC 5322 compliance.

```php
use Symfony\Component\Validator\Constraints\Email;
use Symfony\Component\Validator\Validation;

$validator = Validation::createValidator();
$constraint = new Email(['mode' => Email::VALIDATION_MODE_STRICT]);
$violations = $validator->validate($email, $constraint);
```

Despite using egulias internally, Symfony's strict mode does not produce identical results. For example, Symfony rejects quoted local parts like `"quoted"@example.com` while egulias with `RFCValidation` accepts them. This may be due to additional validation logic in the Symfony wrapper.

### EmailValidator (PHP)

- Github: [egulias/EmailValidator](https://github.com/egulias/EmailValidator)
- Version tested: 4.0.4

The most comprehensive PHP validator with multiple validation strategies.
Supports strict RFC 5321/5322 compliance and can warn about technically-valid-but-unusual addresses that you may want to reject in practice.

### Apache Commons Validator (Java)

- GitHub: https://github.com/apache/commons-validator
- Maven: https://mvnrepository.com/artifact/commons-validator/commons-validator
- Version tested: 1.10.1

Part of the Apache Commons project.
Provides an `EmailValidator` class that can be configured to allow local addresses and TLDs.

### Hibernate Validator (Java)

- GitHub: https://github.com/hibernate/hibernate-validator
- Maven: https://mvnrepository.com/artifact/org.hibernate.validator/hibernate-validator
- Version tested: 9.0.0.Final

The reference implementation of Jakarta Bean Validation (formerly JSR 380). Provides the `@Email` annotation for declarative validation. Widely used in Spring Boot and Jakarta EE applications.

For this benchmark, we use `validateValue()` to validate email strings directly without creating full bean instances:

```java
import jakarta.validation.constraints.Email;

public class EmailWrapper {
    @Email
    private String email;
}

// Validate using:
validator.validateValue(EmailWrapper.class, "email", emailString);
```

### Go net/mail (Standard Library)

- pkg.go.dev: https://pkg.go.dev/net/mail
- Version tested: Go 1.23

Go's standard library `net/mail` package provides RFC 5322 email address parsing via `mail.ParseAddress()`. It parses addresses in formats like `"Barry Gibbs <bg@example.com>"` or bare addresses like `foo@example.com`.

This is a parser rather than a dedicated validator, so it may accept some unusual but technically valid RFC 5322 addresses. It does not perform DNS or SMTP verification.

```go
import "net/mail"

_, err := mail.ParseAddress("test@example.com")
if err == nil {
    // Valid
}
```

### checkmail (Go)

- GitHub: https://github.com/badoux/checkmail
- pkg.go.dev: https://pkg.go.dev/github.com/badoux/checkmail
- Version tested: 1.2.4

A simple Go package for email validation with three levels of checking: format validation (regexp-based), domain validation (DNS lookup), and user validation (SMTP check).

For this benchmark, we use only `ValidateFormat()` which performs syntax validation using a simple regexp based on the W3C HTML5 email specification:

```go
import "github.com/badoux/checkmail"

err := checkmail.ValidateFormat("test@example.com")
if err == nil {
    // Valid format
}
```

The library intentionally uses a simple validation approach. From its documentation:

> Format (simple regexp, see: https://www.w3.org/TR/html5/forms.html#valid-e-mail-address and https://davidcel.is/posts/stop-validating-email-addresses-with-regex/)

### AfterShip email-verifier (Go)

- GitHub: https://github.com/AfterShip/email-verifier
- Version tested: 1.4.1

A full-featured Go library that supports syntax validation, MX lookup, SMTP verification, disposable email detection, and typo suggestions.
For this comparison, I disabled all verification features and only tested syntax validation via `ret.Syntax.Valid`.

### truemail (Ruby)

- Github:
- Version tested:

Zero dependencies. Regex, DNS, SMTP validation. Also available in Go.

TODO

### valid_email2 (Ruby)

- Github:
- Version tested:

TODO: Edit this section. Add an explanation of what ActiveModel is, maybe link?

ActiveModel validation. MX lookup, disposable blocklist.

This is widely used in Rails applications and integrates with ActiveModel. It's probably the most common choice in the Ruby ecosystem.

TODO Example code snippet, use for implementing test, then remove here:

```ruby
#!/usr/bin/env ruby
require 'valid_email2'

if ARGV.length < 1
  STDERR.puts "Usage: validate.rb <addresslist.txt>"
  exit 1
end

File.readlines(ARGV[0]).each do |line|
  email = line.strip
  next if email.empty?

  result = ValidEmail2::Address.new(email).valid? ? "valid   " : "invalid "
  puts "#{result}#{email}"
end
```

TODO

### EmailValidation (.NET)

- Github:
- Version tested:

Simple, correct .NET validator. RFC 6531 (internationalized) support.

TODO

### email_address (Rust)

- GitHub: https://github.com/johnstonskj/rust-email_address
- crates.io: https://crates.io/crates/email_address
- Version tested: 0.2.9

An RFC 5322 compliant email address newtype for Rust.
Supports both ASCII and UTF-8 (internationalized) addresses.
This library is the most permissive of those tested, accepting some edge cases that others reject.

### validator (Rust)

- GitHub: https://github.com/Keats/validator
- crates.io: https://crates.io/crates/validator
- Version tested: 0.20.0

Comprehensive validation library for Rust, akin to Zod in Node and Pydantic in Python.
Validates email addresses based on the HTML5 spec rather than RFC 5322.

```rust
use validator::ValidateEmail;

fn validate(email: &str) -> bool {
    email.validate_email()
}
```

## Other Options not Reviewed

- **pydantic** because it delegates email validation to python-email-validator.
- **isemail**: because it is no longer maintained. It was a port of PHP is_email.
- **go-mail** ([wneessen/go-mail](https://github.com/wneessen/go-mail)) because it delegates email validation to Go's standard library `net/mail`. Note: the naming history is confusing - go-gomail/gomail was the original (~2016), go-mail/mail was a fork (~2019), and wneessen/go-mail is the currently maintained version (2022+).
- **Mailchecker** ([FGRibreau/mailchecker](https://github.com/FGRibreau/mailchecker)) is a cross-language library that primarily compares an email address against a list of disposable email address providers. It also offers validation and defers this to PHP's `filter_var` and the regex from **validator.js** for all other languages.
- Libraries that send each email address to an API, for example [email-verifier](https://www.npmjs.com/package/email-verifier).
