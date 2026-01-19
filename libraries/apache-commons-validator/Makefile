MVN := mvn
ADDRESSLIST ?= ../../addresslist.txt

.PHONY: build run clean check version

build:
	$(MVN) package -q -DskipTests

run: build
	@java -cp "target/emailvalidator-1.0.jar:target/lib/*" Validate $(ADDRESSLIST)

check: build
	@echo "Testing basic validation..."
	@java -cp "target/emailvalidator-1.0.jar:target/lib/*" Validate --check

version:
	@$(MVN) dependency:list -q -DincludeArtifactIds=commons-validator 2>/dev/null | grep commons-validator | sed 's/.*:commons-validator:jar:\([^:]*\).*/\1/' | head -1

clean:
	$(MVN) clean -q
	rm -rf target
