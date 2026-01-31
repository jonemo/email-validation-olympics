ADDRESSLIST ?= ../../addresslist.txt
BINARY := validate
LIBVLDMAIL_DIR := libvldmail
LIBVLDMAIL_SRC := $(LIBVLDMAIL_DIR)/src

.PHONY: build run check version clean

build: $(BINARY)

$(LIBVLDMAIL_DIR):
	git clone --quiet https://github.com/dertuxmalwieder/libvldmail.git $(LIBVLDMAIL_DIR)

$(BINARY): validate.c $(LIBVLDMAIL_DIR)
	gcc -o $(BINARY) validate.c $(LIBVLDMAIL_SRC)/vldmail.c -I$(LIBVLDMAIL_SRC)

run: build
	@./$(BINARY) $(ADDRESSLIST)

check: build
	@echo "test@example.com" | ./$(BINARY) /dev/stdin | grep -q "valid" && echo "libvldmail check passed"

version:
	@echo "libvldmail (git master)"

clean:
	rm -f $(BINARY)
	rm -rf $(LIBVLDMAIL_DIR)
