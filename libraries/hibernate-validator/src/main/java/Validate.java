import jakarta.validation.Validation;
import jakarta.validation.Validator;
import jakarta.validation.ValidatorFactory;
import jakarta.validation.constraints.Email;
import jakarta.validation.ConstraintViolation;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Set;

public class Validate {

    // Wrapper class to use @Email annotation with validateValue()
    public static class EmailWrapper {
        @Email
        private String email;
    }

    public static void main(String[] args) {
        if (args.length < 1) {
            System.err.println("Usage: java Validate <addresslist> | --check");
            System.exit(1);
        }

        ValidatorFactory factory = Validation.buildDefaultValidatorFactory();
        Validator validator = factory.getValidator();

        if ("--check".equals(args[0])) {
            // Sanity check mode
            boolean valid = isValidEmail(validator, "foo@example.com");
            if (!valid) {
                System.err.println("Sanity check failed: foo@example.com should be valid");
                System.exit(1);
            }
            System.out.println("OK");
            factory.close();
            return;
        }

        String filename = args[0];
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String email = line;
                if (email.isEmpty()) {
                    continue;
                }
                String result = isValidEmail(validator, email) ? "valid   " : "invalid ";
                System.out.println(result + email);
            }
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
            System.exit(1);
        }

        factory.close();
    }

    private static boolean isValidEmail(Validator validator, String email) {
        Set<ConstraintViolation<EmailWrapper>> violations =
            validator.validateValue(EmailWrapper.class, "email", email);
        return violations.isEmpty();
    }
}
