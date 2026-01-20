using EmailValidation;

var inputFile = args[0];
foreach (var line in File.ReadLines(inputFile))
{
    var email = line.TrimEnd('\r');
    if (string.IsNullOrEmpty(email)) continue;

    var isValid = EmailValidator.Validate(email);
    var prefix = isValid ? "valid   " : "invalid ";
    Console.WriteLine($"{prefix}{email}");
}
