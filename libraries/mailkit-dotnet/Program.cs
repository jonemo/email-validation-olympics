using MimeKit;

var inputFile = args[0];
foreach (var line in File.ReadLines(inputFile))
{
    var email = line.TrimEnd('\r');
    if (string.IsNullOrEmpty(email)) continue;

    var isValid = MailboxAddress.TryParse(email, out var _);
    var prefix = isValid ? "valid   " : "invalid ";
    Console.WriteLine($"{prefix}{email}");
}
