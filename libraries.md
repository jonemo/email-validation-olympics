## The Libraries

| Name                         | Repository                                                                            | Package                                                   | Language   | Verification | Disposable |
| ---------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------- | ---------- | :----------: | :--------: |
| **validator.js**             | [validatorjs/validator.js](https://github.com/validatorjs/validator.js)               | [NPM](https://www.npmjs.com/package/validator)            | JavaScript |              |            |
| **deep-email-validator**     | [mfbx9da4/deep-email-validator](https://github.com/mfbx9da4/deep-email-validator)     | [NPM](https://www.npmjs.com/package/deep-email-validator) | TypeScript |      ✓       |     ✓      |
| **email-validator**          | [manishsaraan/email-validator](https://github.com/manishsaraan/email-validator)       | [NPM](https://www.npmjs.com/package/email-validator)      | JavaScript |              |            |
| **python-email-validator**   | [JoshData/python-email-validator](https://github.com/JoshData/python-email-validator) | [PyPI](https://pypi.org/project/email-validator/)         | Python     |      ✓       |            |
| **pyIsEmail**                | [michaelherold/pyIsEmail](https://github.com/michaelherold/pyIsEmail)                 |                                                           | Python     |      ?       |     ?      |
| **EmailValidator**           | [egulias/EmailValidator](https://github.com/egulias/EmailValidator)                   |                                                           | PHP        |      ✓       |            |
| **Apache Commons Validator** | [apache/commons-validator](https://github.com/apache/commons-validator)               |                                                           | Java       |              |            |
| **Hibernate Validator**      | [hibernate/hibernate-validator](https://github.com/hibernate/hibernate-validator)     |                                                           | Java       |              |            |
| **AfterShip/email-verifier** | [AfterShip/email-verifier](https://github.com/AfterShip/email-verifier)               |                                                           | Go         |      ✓       |     ✓      |
| **truemail**                 | [truemail-rb/truemail](https://github.com/truemail-rb/truemail)                       |                                                           | Ruby       |      ✓       |            |
| **valid_email2**             | [micke/valid_email2](https://github.com/micke/valid_email2)                           |                                                           | Ruby       |      ✓       |     ✓      |
| **EmailValidation**          | [jstedfast/EmailValidation](https://github.com/jstedfast/EmailValidation)             | [NuGet](https://www.nuget.org/packages/EmailValidation/)  | .NET       |              |            |
| **email_address**            | [johnstonskj/rust-email_address](https://github.com/johnstonskj/rust-email_address)   | [crates.io](https://crates.io/crates/email_address)       | Rust       |              |            |
| **check-if-email-exists**    | [reacherhq/check-if-email-exists](https://github.com/reacherhq/check-if-email-exists) |                                                           | Rust       |      ✓       |     ✓      |
| **validator**                | [Keats/validator](https://github.com/Keats/validator)                                 |                                                           | Rust       |              |            |
| **MailChecker**              | [FGRibreau/mailchecker](https://github.com/FGRibreau/mailchecker)                     |                                                           | Multi      |              |     ✓      |

### validator.js

- GitHub: https://github.com/validatorjs/validator.js
- npm: https://www.npmjs.com/package/validator
- Language: JavaScript
- Version tested: 13.12.0

The most popular JavaScript validation library with over 23,000 GitHub stars.
Provides an `isEmail()` function with configurable options for allowing display names, UTF-8 local parts, and more.

Actively maintained.

### deep-email-validator

Validates regex, typos, disposable, DNS, and SMTP. Node.js only.

0.1.21, last published in 2021

TODO

### email-validator

Simple, fast syntax validator.

Version 2.0.4, last published in 2018

TODO

### python-email-validator

- GitHub: https://github.com/JoshData/python-email-validator
- PyPI: https://pypi.org/project/email-validator/
- Language: Python
- Version tested: 2.3.0

This is currently the most popular option in Python with over 4 million weekly downloads.
[Pydantic uses it](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.EmailStr) for its `EmailStr` field type.

The Readme declares:

> This is an opinionated library. You should definitely also consider using the less-opinionated pyIsEmail if it works better for you.

### pyIsEmail

TODO

### EmailValidator (PHP)

Validates against multiple RFCs. Supports DNS and spoof checking.

### Apache Commons Validator

- GitHub: https://github.com/apache/commons-validator
- Maven: https://mvnrepository.com/artifact/commons-validator/commons-validator
- Language: Java
- Version tested: 1.10.1

Part of the Apache Commons project.
Provides an `EmailValidator` class that can be configured to allow local addresses and TLDs.

### Hibernate Validator

Reference implementation of Jakarta Bean Validation. `@Email` annotation.

### AfterShip email-verifier

- GitHub: https://github.com/AfterShip/email-verifier
- Language: Go
- Version tested: 1.4.1

A full-featured Go library that supports syntax validation, MX lookup, SMTP verification, disposable email detection, and typo suggestions.
For this comparison, I disabled all verification features and only tested syntax validation via `ret.Syntax.Valid`.

### truemail

Zero dependencies. Regex, DNS, SMTP validation. Also available in Go.

TODO

### valid_email2

ActiveModel validation. MX lookup, disposable blocklist.

TODO

### EmailValidation (.NET)

Simple, correct .NET validator. RFC 6531 (internationalized) support.

TODO

### email_address (Rust)

- GitHub: https://github.com/johnstonskj/rust-email_address
- crates.io: https://crates.io/crates/email_address
- Language: Rust
- Version tested: 0.2.9

An RFC 5322 compliant email address newtype for Rust.
Supports both ASCII and UTF-8 (internationalized) addresses.
This library is the most permissive of those tested, accepting some edge cases that others reject.

### check-if-email-exists (Rust)

Full verification without sending email. AGPL license. Powers [Reacher](https://reacher.email/).

TODO

### validator (Rust)

Struct validation with `#[validate(email)]` derive macro.

TODO

### MailChecker

Cross-language library available for JS, Python, PHP, Ruby, Go, Rust, and Elixir. Includes blocklist of 55k+ disposable email domains.

TODO

## Other Options not Reviewed

- **isemail**: Port of PHP is_email. No longer maintened.
