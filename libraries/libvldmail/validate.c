#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <wchar.h>
#include <locale.h>
#include "vldmail.h"

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <addresslist>\n", argv[0]);
        return 1;
    }

    // Set locale to support wide characters
    setlocale(LC_ALL, "");

    FILE *f = fopen(argv[1], "r");
    if (!f) {
        perror("fopen");
        return 1;
    }

    char line[4096];
    while (fgets(line, sizeof(line), f)) {
        // Remove trailing newline
        size_t len = strlen(line);
        if (len > 0 && line[len - 1] == '\n') {
            line[len - 1] = '\0';
            len--;
        }
        if (len > 0 && line[len - 1] == '\r') {
            line[len - 1] = '\0';
            len--;
        }

        // Skip empty lines
        if (len == 0) {
            continue;
        }

        // Convert to wide string for libvldmail
        wchar_t wline[4096];
        mbstowcs(wline, line, sizeof(wline) / sizeof(wchar_t));

        // Validate email
        valid_mail_t result = validate_email(wline);

        // Output result (success != 0 means valid)
        if (result.success != 0) {
            printf("valid   %s\n", line);
        } else {
            printf("invalid %s\n", line);
        }
    }

    fclose(f);
    return 0;
}
