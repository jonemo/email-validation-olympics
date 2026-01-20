DOTNET := dotnet
ADDRESSLIST ?= ../../addresslist.txt

.PHONY: build run clean check version

build: emailvalidation-dotnet.csproj
	@$(DOTNET) build --nologo -v q

emailvalidation-dotnet.csproj:
	@printf '<Project Sdk="Microsoft.NET.Sdk">\n  <PropertyGroup>\n    <OutputType>Exe</OutputType>\n    <TargetFramework>net8.0</TargetFramework>\n    <ImplicitUsings>enable</ImplicitUsings>\n  </PropertyGroup>\n  <ItemGroup>\n    <PackageReference Include="EmailValidation" Version="*" />\n  </ItemGroup>\n</Project>\n' > emailvalidation-dotnet.csproj
	@$(DOTNET) restore --nologo -v q

run: build
	@$(DOTNET) run --no-build --nologo -- $(ADDRESSLIST)

check: build
	@echo "Testing basic validation..."
	@$(DOTNET) run --no-build --nologo -- /dev/stdin <<< "foo@example.com" | grep -q "^valid" && echo "OK"

version: build
	@$(DOTNET) list package | grep EmailValidation | awk '{print "Version:", $$NF}'

clean:
	rm -rf bin/ obj/ emailvalidation-dotnet.csproj
