import org.apache.commons.validator.routines.EmailValidator;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Validate {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.err.println("Usage: java Validate <addresslist> | --check");
            System.exit(1);
        }

        EmailValidator validator = EmailValidator.getInstance();

        if ("--check".equals(args[0])) {
            // Sanity check mode
            boolean valid = validator.isValid("foo@example.com");
            if (!valid) {
                System.err.println("Sanity check failed: foo@example.com should be valid");
                System.exit(1);
            }
            System.out.println("OK");
            return;
        }

        String filename = args[0];
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String email = line.trim();
                if (email.isEmpty()) {
                    continue;
                }
                String result = validator.isValid(email) ? "valid   " : "invalid ";
                System.out.println(result + email);
            }
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
            System.exit(1);
        }
    }
}
