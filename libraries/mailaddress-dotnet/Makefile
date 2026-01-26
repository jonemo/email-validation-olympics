DOTNET := dotnet
ADDRESSLIST ?= ../../addresslist.txt

.PHONY: build run clean check version

build: mailaddress-dotnet.csproj
	@$(DOTNET) build --nologo -v q

mailaddress-dotnet.csproj:
	@printf '<Project Sdk="Microsoft.NET.Sdk">\n  <PropertyGroup>\n    <OutputType>Exe</OutputType>\n    <TargetFramework>net8.0</TargetFramework>\n    <ImplicitUsings>enable</ImplicitUsings>\n  </PropertyGroup>\n</Project>\n' > mailaddress-dotnet.csproj
	@$(DOTNET) restore --nologo -v q

run: build
	@$(DOTNET) run --no-build -- $(ADDRESSLIST)

check: build
	@echo "Testing basic validation..."
	@$(DOTNET) run --no-build -- /dev/stdin <<< "foo@example.com" | grep -q "^valid" && echo "OK"

version:
	@$(DOTNET) --version | xargs -I{} echo "Version: .NET {}"

clean:
	rm -rf bin/ obj/ mailaddress-dotnet.csproj
