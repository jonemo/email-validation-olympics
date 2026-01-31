DOTNET := dotnet
ADDRESSLIST ?= ../../addresslist.txt

.PHONY: build run clean check version

build: mailkit-dotnet.csproj
	@$(DOTNET) build --nologo -v q

mailkit-dotnet.csproj:
	@printf '<Project Sdk="Microsoft.NET.Sdk">\n  <PropertyGroup>\n    <OutputType>Exe</OutputType>\n    <TargetFramework>net8.0</TargetFramework>\n    <ImplicitUsings>enable</ImplicitUsings>\n  </PropertyGroup>\n  <ItemGroup>\n    <PackageReference Include="MailKit" Version="*" />\n  </ItemGroup>\n</Project>\n' > mailkit-dotnet.csproj
	@$(DOTNET) restore --nologo -v q

run: build
	@$(DOTNET) run --no-build -- $(ADDRESSLIST)

check: build
	@echo "Testing basic validation..."
	@$(DOTNET) run --no-build -- /dev/stdin <<< "foo@example.com" | grep -q "^valid" && echo "OK"

version: build
	@$(DOTNET) list package | grep MailKit | awk '{print "Version:", $$NF}'

clean:
	rm -rf bin/ obj/ mailkit-dotnet.csproj
