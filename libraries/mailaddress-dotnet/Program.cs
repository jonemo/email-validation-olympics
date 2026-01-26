using System.Net.Mail;

var inputFile = args[0];
foreach (var line in File.ReadLines(inputFile))
{
    var email = line.TrimEnd('\r');
    if (string.IsNullOrEmpty(email)) continue;

    bool isValid;
    try
    {
        var addr = new MailAddress(email);
        // MailAddress accepts "Display Name <email>" format, so verify the Address matches
        isValid = addr.Address == email;
    }
    catch
    {
        isValid = false;
    }

    var prefix = isValid ? "valid   " : "invalid ";
    Console.WriteLine($"{prefix}{email}");
}
