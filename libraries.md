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
| **Django EmailValidator**    | [django/django](https://github.com/django/django)                                     | [PyPI](https://pypi.org/project/Django/)                                                 | Python     |
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
| **MailAddress**              | [dotnet/runtime](https://github.com/dotnet/runtime)                                   | N/A                                                                                     | .NET       |
| **EmailValidation**          | [jstedfast/EmailValidation](https://github.com/jstedfast/EmailValidation)             | [NuGet](https://www.nuget.org/packages/EmailValidation/)                                | .NET       |
| **MailKit**                  | [jstedfast/MailKit](https://github.com/jstedfast/MailKit)                             | [NuGet](https://www.nuget.org/packages/MailKit)                                         | .NET       |
| **email_address**            | [johnstonskj/rust-email_address](https://github.com/johnstonskj/rust-email_address)   | [crates.io](https://crates.io/crates/email_address)                                     | Rust       |
| **validator**                | [Keats/validator](https://github.com/Keats/validator)                                 | [crates.io](https://crates.io/crates/validator)                                         | Rust       |
| **Email::Valid**             | [Perl-Email-Project/Email-Valid](https://github.com/Perl-Email-Project/Email-Valid)   | [CPAN](https://metacpan.org/pod/Email::Valid)                                           | Perl       |
| **libvldmail**               | [dertuxmalwieder/libvldmail](https://github.com/dertuxmalwieder/libvldmail)           | N/A                                                                                     | C          |

### validator.js

- Github: https://github.com/validatorjs/validator.js
- NPM: https://www.npmjs.com/package/validator
- Version tested: 13.12.0
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/validator-js)

A library of string validators and sanitizers for JavaScript with over 23,000 Github stars.
Provides an `isEmail()` function with configurable options for allowing display names, UTF-8 local parts, and more.

```js
import isEmail from "validator/lib/isEmail";

validator.isEmail("foo@bar.com");
```


Actively maintained.

### email-validator (Javascript)

- Github: https://github.com/manishsaraan/email-validator
- NPM: https://npmjs.com/package/email-validator
- Version tested: Version 2.0.4
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/email-validator)

The second most downloaded email validation library on NPM, by a wide margin, behind validator.js.
Advertised as "a simple module", and simple it is:
The entire library is 33 lines of code in a single file, plus 100 lines of tests.
The last update was pushed in 2018, which some may call "abandoned" and others "finished".

```js
const validator = require("email-validator");

validator.validate("foo@bar.com"); // true
```

No configuration options available.

### deep-email-validator (Javascript, Node.js only)

- Github: https://github.com/mfbx9da4/deep-email-validator
- NPM: https://npmjs.com/package/deep-email-validator
- Version tested: 0.1.21
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/deep-email-validator)

The "deep" in the name refers to the list of features beyond validation: Typos, disposable check, DNS lookup, and SMTP.

Note that deep-email-validator is Node.js only Javascript, so no good for your web form.

### Zod (Javascript)

- Github: https://github.com/colinhacks/zod
- NPM: https://www.npmjs.com/package/zod
- Version tested: 4.3.5
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/zod)

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

- Github: https://github.com/hapijs/joi
- NPM: https://www.npmjs.com/package/joi
- Version tested: 18.0.2
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/joi)

[Joi](https://joi.dev) is another Javascript validation library that includes a [field type for email addresses](https://joi.dev/api/?v=17.13.3#stringemailoptions):

```js
const Joi = require("joi");

const schema = Joi.string().email();
```

The documentation mentions one edge case:

> Note that quoted email addresses (e.g. "test"@example.com) are not supported and will fail validation.

### python-email-validator

- Github: https://github.com/JoshData/python-email-validator
- PyPI: https://pypi.org/project/email-validator/
- Version tested: 2.3.0
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/python-email-validator)

This is currently the most popular option for Python with 20 million weekly PyPI downloads.
[Pydantic uses it](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.EmailStr) for its `EmailStr` field type.

```python
from email_validator import validate_email, EmailNotValidError

try:
    emailinfo = validate_email(
        "my+address@example.org",
        check_deliverability=False,
        allow_quoted_local=True,
        allow_domain_literal=True,
    )
except EmailNotValidError as e:
    print(str(e))  # Prints a human-readable explanation.
```

The default settings allow UTF-8 and verifies with a DNS check, but disallow quotes and IP addresses.
I enable the default-off flags for a fair comparison.

The Readme declares:

> This is an opinionated library. You should definitely also consider using the less-opinionated pyIsEmail if it works better for you.

### pyIsEmail (Python)

- Github: https://github.com/michaelherold/pyIsEmail
- PyPI: https://pypi.org/project/pyIsEmail/
- Version tested: 2.0.1
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/pyisemail)

A Python port of [the `is_email` PHP library](https://github.com/dominicsayers/isemail) (which is not covered again in this blog post).
Provides detailed diagnostic information when validation fails.

```python
from pyisemail import is_email

address = "test@example.com"
bool_result = is_email(address)
detailed_result = is_email(address, diagnose=True)
```

**Configuration options:**

- `check_dns` - Validate that the domain has MX records. Default: `False`.
- `diagnose` - Return detailed diagnostic information instead of a boolean. Default: `False`.

### Django EmailValidator (Python)

- Github: https://github.com/django/django
- PyPI: https://pypi.org/project/Django/
- Docs: https://docs.djangoproject.com/en/6.0/ref/validators/#django.core.validators.EmailValidator
- Version tested: 5.2.10
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/django-emailvalidator)

Django's built-in email validator is used throughout the framework for model fields and form validation. It's one of the most widely deployed email validators given Django's popularity in Python web development.

```python
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

validator = EmailValidator()
try:
    validator("test@example.com")
    # Valid
except ValidationError:
    # Invalid
```

The validator uses a regex-based approach that aims to match the HTML5 email input specification while allowing some RFC 5322 edge cases. It's designed to be practical for web forms rather than strictly RFC-compliant.

### PHP Standard Library

- Version tested: 8.3.30
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/php-filter-var)

PHP has an email validator built into the standard library:

```php
filter_var($email, FILTER_VALIDATE_EMAIL)
```

https://www.php.net/manual/en/function.filter-var.php

This advertises RFC 5321 compliance.

### WordPress (PHP)

- Github: https://github.com/WordPress/WordPress
- Version tested: 6.7.1
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/wordpress-is-email)

The [`is_email()`](https://developer.wordpress.org/reference/functions/is_email/) function is WordPress's built-in email validator.
WordPress powers over 40% of websites, this is likely one of the most widely executed email validation functions in existence.

Because Wordpress' internal functions aren't normally used as a library, for my test I copied the `is_email` source code from [wp-includes/formatting.php](https://github.com/WordPress/WordPress/blob/master/wp-includes/formatting.php).

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

> "Does not grok i18n domains." [...] "Not RFC compliant."

No configuration options available.

### Symfony Validator (PHP)

- Github: https://github.com/symfony/validator
- Version tested: 7.4.3
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/symfony-validator)

Symfony's Validator component provides an `Email` constraint with multiple validation modes.
In `strict` mode, it uses [egulias/EmailValidator](https://github.com/egulias/EmailValidator).
The default mode is `VALIDATION_MODE_HTML5` and uses a regex that you can see in [this file](https://github.com/symfony/validator/blob/c65aa0495769dd03d2c094f784545dc202c2b675/Constraints/EmailValidator.php#L12).

```php
use Symfony\Component\Validator\Constraints\Email;
use Symfony\Component\Validator\Validation;

$validator = Validation::createValidator();
$constraint = new Email(['mode' => Email::VALIDATION_MODE_HTML5]);
$violations = $validator->validate($email, $constraint);
```

Despite using egulias internally, Symfony's strict mode does not produce identical results. For example, Symfony rejects quoted local parts like `"quoted"@example.com` while egulias with `RFCValidation` accepts them. This may be due to additional validation logic in the Symfony wrapper.

### EmailValidator (PHP)

- Github: https://github.com/egulias/EmailValidator
- Version tested: 4.0.4
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/egulias-email-validator)

The most comprehensive PHP validator with multiple validation strategies.
Supports strict RFC 5321/5322 compliance and can warn about technically-valid-but-unusual addresses that you may want to reject in practice.

```php
use Egulias\EmailValidator\EmailValidator;
use Egulias\EmailValidator\Validation\RFCValidation;

$validator = new EmailValidator();
$validator->isValid("example@example.com", new RFCValidation());
```

### Apache Commons Validator (Java)

- Github: https://github.com/apache/commons-validator
- Maven: https://mvnrepository.com/artifact/commons-validator/commons-validator
- Version tested: 1.10.1
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/apache-commons-validator)

Part of the Apache Commons project.
Provides an `EmailValidator` [class](https://github.com/apache/commons-validator/blob/43ff9695d7bb4ca8d7ac2284d209e0bfd84b61a3/src/main/java/org/apache/commons/validator/routines/EmailValidator.java#L35) that can be configured to allow local addresses and TLDs.

```java
import org.apache.commons.validator.routines.EmailValidator;

EmailValidator validator = EmailValidator.getInstance();
boolean isValid = validator.isValid("test@example.com");
```

**Configuration options:**

- `getInstance()` - Default instance, no local addresses or TLD-only domains.
- `getInstance(allowLocal)` - Allow local addresses (e.g., `user@localhost`).
- `getInstance(allowLocal, allowTld)` - Also allow TLD-only domains (e.g., `user@io`).

The docs are [here](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/EmailValidator.html).

This code is nearly 20 years old and references a long-gone website https://javascript.internet.com as inspiration, and it's still [getting polished](https://github.com/apache/commons-validator/commit/c8d4a8f6270f7714a0cac0a5ea82c7a39bbd5940) today.

### Hibernate Validator (Java)

- Github: https://github.com/hibernate/hibernate-validator
- Maven: https://mvnrepository.com/artifact/org.hibernate.validator/hibernate-validator
- Version tested: 9.0.0.Final
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/hibernate-validator)

I am way out of my depth on this, but Claude asked me to tell you:

> This is the reference implementation of Jakarta Bean Validation (formerly JSR 380).
> Provides the `@Email` annotation for declarative validation.
> Widely used in Spring Boot and Jakarta EE applications.

To keep the test script minimal, ~I use~ Claude uses `validateValue()` to validate the strings directly without creating full bean instances:

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
- Version tested: 1.23
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/net-mail)

Go's standard library `net/mail` package provides RFC 5322 email address parsing via `mail.ParseAddress()`.

This is a parser rather than a dedicated validator, so it may accept some unusual but technically valid RFC 5322 addresses. It does not perform DNS or SMTP verification.

```go
import "net/mail"

_, err := mail.ParseAddress("test@example.com")
if err == nil {
    // Valid
}
```

### checkmail (Go)

- Github: https://github.com/badoux/checkmail
- Version tested: 1.2.4
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/checkmail)

127 lines of Go that cover format validation, DNS lookup, and verification with SMTP.

For the test I call `ValidateFormat()` which performs syntax validation using a simple regexp based on the W3C HTML5 email specification:

```go
import "github.com/badoux/checkmail"

err := checkmail.ValidateFormat("test@example.com")
if err == nil {
    // Valid format
}
```

The library intentionally uses a simple validation approach. From its documentation:

> Format (simple regexp, see: https://www.w3.org/TR/html5/forms.html#valid-e-mail-address and https://davidcel.is/posts/stop-validating-email-addresses-with-regex/)

### email-verifier (Go)

- Github: https://github.com/AfterShip/email-verifier
- Version tested: 1.4.1
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/aftership-email-verifier)

A full-featured Go library that supports syntax validation, MX lookup, SMTP verification, disposable email detection, and typo suggestions.
For this comparison, I disabled all verification features and only tested syntax validation via `ret.Syntax.Valid`.

```go
import emailverifier "github.com/AfterShip/email-verifier"

verifier := emailverifier.NewVerifier().
    DisableSMTPCheck().
    DisableDomainSuggest().
    DisableAutoUpdateDisposable()

ret, _ := verifier.Verify("test@example.com")
isValid := ret != nil && ret.Syntax.Valid
```

### truemail (Ruby)

- Github: https://github.com/truemail-rb/truemail
- Rubygems: https://rubygems.org/gems/truemail
- Version tested: 3.3.1
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/truemail)

**Note:** This library's test runner failed during benchmarking. Results are not included in the comparison table.

truemail offers the full menu of checks: Domain allow/deny lists, regex (the part we care about), DNS check, SMTP check.

> By default this validation not performs strictly following RFC 5322 standard, so you can override Truemail default regex pattern if you want.

To run syntax validation only:

```rb
require 'truemail'

Truemail.configure do |config|
  config.verifier_email = 'verifier@example.com'
  config.default_validation_type = :regex  # syntax-only, no DNS/SMTP
end

def valid?(email)
  Truemail.valid?(email)
end
```

To use a custom regex:

```rb
Truemail.configure do |config|
  config.verifier_email = 'verifier@example.com'
  config.default_validation_type = :regex  # syntax-only, no DNS/SMTP
  config.email_pattern = /regex_pattern/  # <-- your custom regex here
end
```

To add allow list or deny list checking:

```rb
Truemail.configure do |config|
  config.verifier_email = 'verifier@example.com'
  config.default_validation_type = :regex  # syntax-only, no DNS/SMTP
  config.whitelist_validation=true
  config.whitelisted_domains=['stavros.io']
  config.blacklist_validation=true
  config.blacklisted_domains=['jonasneubert.com']
```

You can also provide a list of allowed or denied emails in `whitelisted_emails` and `blacklisted_emails`.
But if you do that, then why use a validation library at all?

[truemail-go](https://github.com/truemail-rb/truemail-go) is a Go port of the truemail's syntax validation features only.
Both Ruby original and Go port received their most recent commit in 2024.

### valid_email2 (Ruby)

- Github: https://github.com/micke/valid_email2
- Rubygems: https://rubygems.org/gems/valid_email2
- Version tested: 7.0.13
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/valid-email2)

This is widely used in Rails applications and integrates with [ActiveModel](https://guides.rubyonrails.org/active_model_basics.html), Rails' system for object validation. It's probably the most common choice in the Ruby ecosystem.

```ruby
require 'valid_email2'

email = ValidEmail2::Address.new("test@example.com")
email.valid?  # true
```

### System.Net.Mail.MailAddress (.NET Standard Library)

- GitHub: https://github.com/dotnet/runtime
- Version tested: .NET 8.0
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/mailaddress-dotnet)

.NET's built-in email address parser.
As is typical for .NET, the [documentation](https://learn.microsoft.com/en-us/dotnet/api/system.net.mail.mailaddress?view=net-10.0) goes into detail about what is and what isn't supported.
One interesting detail:

> .NET 9 and earlier ONLY: Consecutive and trailing dots in user names. For example, `user...name..@host`. (Starting in .NET 10, consecutive dots aren't allowed.)

```csharp
using System.Net.Mail;

try {
    var addr = new MailAddress(email);
    // Valid if Address matches input (rejects display name format)
    bool isValid = addr.Address == email;
} catch {
    // Invalid
}
```
### EmailValidation (.NET)

- Github: https://github.com/jstedfast/EmailValidation
- NuGet: https://www.nuget.org/packages/EmailValidation/
- Version tested: 1.3.0
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/emailvalidation-dotnet)

Simple, correct .NET validator with RFC 6531 (internationalized) support. Written by Jeffrey Stedfast, who also authored MailKit.

```csharp
using EmailValidation;

bool isValid = EmailValidator.Validate("test@example.com");
```

### MailKit (.NET)

- Github: https://github.com/jstedfast/MailKit
- NuGet: https://www.nuget.org/packages/MailKit
- Version tested: 4.10.0
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/mailkit-dotnet)

MailKit is a cross-platform mail client library for .NET, written by Jeffrey Stedfast (who also wrote EmailValidation). While primarily an IMAP/SMTP client, it includes email address parsing via `MailboxAddress.TryParse()` from the MimeKit dependency.

```csharp
using MimeKit;

bool isValid = MailboxAddress.TryParse("test@example.com", out var _);
```

### email_address (Rust)

- Github: https://github.com/johnstonskj/rust-email_address
- crates.io: https://crates.io/crates/email_address
- Version tested: 0.2.9
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/rust-email-address)

An RFC 5322 compliant email address newtype for Rust.
Supports both ASCII and UTF-8 (internationalized) addresses.
This library is the most permissive of those tested, accepting some edge cases that others reject.

```rust
use email_address::EmailAddress;

let is_valid = EmailAddress::is_valid("test@example.com");
```

No configuration options available.

### validator (Rust)

- Github: https://github.com/Keats/validator
- crates.io: https://crates.io/crates/validator
- Version tested: 0.20.0
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/validator-rust)

Comprehensive validation library for Rust, akin to Zod in Node and Pydantic in Python.
Validates email addresses based on the HTML5 spec rather than RFC 5322.

```rust
use validator::ValidateEmail;

fn validate(email: &str) -> bool {
    email.validate_email()
}
```

No configuration options available for email validation.

### Email::Valid (Perl)

- Github: https://github.com/Perl-Email-Project/Email-Valid
- CPAN: https://metacpan.org/pod/Email::Valid
- Version tested: 1.204
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/email-valid-perl)

The closest I've ever come to Perl is as a marketing (sic) intern at Nestoria where I was sitting next to some Perl wizards.
Lacking first hand knowledge I have no choice but to believe the Google wisdom that this library with 18 Github stars is indeed the premier Perl solution for email validation.

The syntax of the basic usage example looks Perlish indeed:

```perl
use Email::Valid;

my $email = 'example@domain.com';
my $valid = Email::Valid->address($email);
print $valid ? "Valid email" : "Invalid email";
```

### libvldmail (C)

- Github: https://github.com/dertuxmalwieder/libvldmail
- Version tested: git master
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/libvldmail)

A C library for email syntax validation only.
Follows RFC 6531 by default with fallback to RFC 5321.

```c
#include <vldmail.h>

valid_mail_t validator = validate_email(L"foo@bar.com");
if (validator.success != 0) {
    // Valid
}
```

**Configuration options (preprocessor parameters):**

- `NO_UNICODE_MAIL_PLEASE` - Restrict validation to ASCII characters only.
- `STRICT_VALIDATION` - Apply stricter RFC standards, marking deprecated formats as invalid.

## Other Options not Reviewed

- **pydantic** because it delegates email validation to python-email-validator.
- **isemail**: because it is no longer maintained. It was a port of PHP is_email.
- [**go-mail**](https://github.com/wneessen/go-mail) because it delegates email validation to Go's standard library `net/mail`. Note: The naming history is confusing - go-gomail/gomail was the original (~2016), go-mail/mail was a fork (~2019), and wneessen/go-mail is the currently maintained version (2022+).
- [**Mailchecker**](https://github.com/FGRibreau/mailchecker) is a cross-language library that primarily compares an email address against a list of disposable email address providers. It also offers validation and defers this to PHP's `filter_var` and to the regex from **validator.js** for all other languages.
- [**mailcheck.js**](https://github.com/mailcheck/mailcheck)) because it is not a full validator, it finds domain misspellings for a fixed list of domains. And because it's been unmaintained for 10 years, after a successful run as jQuery plugin.
- Libraries that send each email address to an API, for example [email-verifier](https://www.npmjs.com/package/email-verifier).
