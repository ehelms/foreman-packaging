%global npm_name react-overlays

Name: nodejs-react-overlays
Version: 0.8.3
Release: 1%{?dist}
Summary: Utilities for creating robust overlay components
License: MIT
Group: Development/Libraries
URL: https://github.com/react-bootstrap/react-overlays#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(classnames) >= 2.2.5
Requires: npm(classnames) < 3.0.0
Requires: npm(dom-helpers) >= 3.2.1
Requires: npm(dom-helpers) < 4.0.0
Requires: npm(prop-types) >= 15.5.10
Requires: npm(prop-types) < 16.0.0
Requires: npm(prop-types-extra) >= 1.0.1
Requires: npm(prop-types-extra) < 2.0.0
Requires: npm(react-transition-group) >= 2.2.0
Requires: npm(react-transition-group) < 3.0.0
Requires: npm(warning) >= 4.0.0
Requires: npm(warning) < 5.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package
# https://github.com/react-bootstrap/react-overlays/pull/270
%nodejs_fixdep warning '^4.0.0'

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
* Wed Oct 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.8.3-1
- Add nodejs-react-overlays generated by npm2rpm using the single strategy

