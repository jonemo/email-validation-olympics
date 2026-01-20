## The Libraries

| Name                         | Repository                                                                            | Package                                                   | Language   | Verification |
| ---------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------- | ---------- | :----------: |
| **validator.js**             | [validatorjs/validator.js](https://github.com/validatorjs/validator.js)               | [NPM](https://www.npmjs.com/package/validator)            | JavaScript |              |
| **deep-email-validator**     | [mfbx9da4/deep-email-validator](https://github.com/mfbx9da4/deep-email-validator)     | [NPM](https://www.npmjs.com/package/deep-email-validator) | TypeScript |      ✓       |
| **email-validator**          | [manishsaraan/email-validator](https://github.com/manishsaraan/email-validator)       | [NPM](https://www.npmjs.com/package/email-validator)      | JavaScript |              |
| **Zod**                      | [colinhacks/zod](https://github.com/colinhacks/zod)                                   | [NPM](https://www.npmjs.com/package/zod)                  | JavaScript |              |
| **Joi**                      | [hapijs/joi](https://github.com/hapijs/joi)                                           | [NPM](https://www.npmjs.com/package/joi)                  | JavaScript |              |
| **python-email-validator**   | [JoshData/python-email-validator](https://github.com/JoshData/python-email-validator) | [PyPI](https://pypi.org/project/email-validator/)         | Python     |      ✓       |
| **pyIsEmail**                | [michaelherold/pyIsEmail](https://github.com/michaelherold/pyIsEmail)                 | [PyPI](https://pypi.org/project/pyIsEmail/)               | Python     |      ✓       |
| **PHP** `filter_var()`       | N/A                                                                                   | N/A                                                       | PHP        |              |
| **EmailValidator**           | [egulias/EmailValidator](https://github.com/egulias/EmailValidator)                   |                                                           | PHP        |      ✓       |
| **Wordpress**                |                                                                                       |                                                           | PHP        |              |
| **Symfony**                  |                                                                                       |                                                           | PHP        |              |
| **Apache Commons Validator** | [apache/commons-validator](https://github.com/apache/commons-validator)               |                                                           | Java       |              |
| **Hibernate Validator**      | [hibernate/hibernate-validator](https://github.com/hibernate/hibernate-validator)     |                                                           | Java       |              |
| **AfterShip/email-verifier** | [AfterShip/email-verifier](https://github.com/AfterShip/email-verifier)               |                                                           | Go         |      ✓       |
| **truemail**                 | [truemail-rb/truemail](https://github.com/truemail-rb/truemail)                       |                                                           | Ruby       |      ✓       |
| **valid_email2**             | [micke/valid_email2](https://github.com/micke/valid_email2)                           |                                                           | Ruby       |      ✓       |
| **EmailValidation**          | [jstedfast/EmailValidation](https://github.com/jstedfast/EmailValidation)             | [NuGet](https://www.nuget.org/packages/EmailValidation/)  | .NET       |              |
| **email_address**            | [johnstonskj/rust-email_address](https://github.com/johnstonskj/rust-email_address)   | [crates.io](https://crates.io/crates/email_address)       | Rust       |              |
| **validator**                | [Keats/validator](https://github.com/Keats/validator)                                 | [crates.io](https://crates.io/crates/validator)           | Rust       |              |
| **MailChecker**              | [FGRibreau/mailchecker](https://github.com/FGRibreau/mailchecker)                     |                                                           | Multi      |              |

### validator.js

- GitHub: https://github.com/validatorjs/validator.js
- npm: https://www.npmjs.com/package/validator
- Version tested: 13.12.0

A library of string validators and sanitizers for JavaScript with over 23,000 GitHub stars.
Provides an `isEmail()` function with configurable options for allowing display names, UTF-8 local parts, and more.

Actively maintained.

### deep-email-validator

Validates regex, typos, disposable, DNS, and SMTP. Node.js only.

0.1.21, last published in 2021

TODO

### email-validator

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


### EmailValidator (PHP)

- Github: [egulias/EmailValidator](https://github.com/egulias/EmailValidator)
- Version tested: 4.0.4

The most comprehensive PHP validator with multiple validation strategies.
Supports strict RFC 5321/5322 compliance and can warn about technically-valid-but-unusual addresses that you may want to reject in practice.

### Apache Commons Validator (Java)

- GitHub: https://github.com/apache/commons-validator
- Maven: https://mvnrepository.com/artifact/commons-validator/commons-validator
- Language: Java
- Version tested: 1.10.1

Part of the Apache Commons project.
Provides an `EmailValidator` class that can be configured to allow local addresses and TLDs.

### Hibernate Validator (Java)

- Github:
- Version tested:

Reference implementation of Jakarta Bean Validation. `@Email` annotation.

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

### MailChecker

Cross-language library available for JS, Python, PHP, Ruby, Go, Rust, and Elixir. Includes blocklist of 55k+ disposable email domains.

TODO

## Other Options not Reviewed

- **pydantic** because it delegates email validation to python-email-validator.
- **isemail**: because it is no longer maintained. It was a port of PHP is_email.
- Libraries that send each email address to an API, for example [email-verifier](https://www.npmjs.com/package/email-verifier).
