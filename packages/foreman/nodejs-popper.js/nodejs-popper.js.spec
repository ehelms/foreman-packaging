%global npm_name popper.js

Name: nodejs-popper.js
Version: 1.14.4
Release: 1%{?dist}
Summary: A kickass library to manage your poppers
License: MIT
Group: Development/Libraries
URL: https://popper.js.org
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.d.ts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js.flow %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%doc README.md

%changelog
* Wed Oct 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.14.4-1
- Add nodejs-popper.js generated by npm2rpm using the single strategy
