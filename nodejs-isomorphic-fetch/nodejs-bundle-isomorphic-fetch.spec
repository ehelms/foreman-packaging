# FIXME
# Remove nodejs_symlink_deps if installing bundled module with NPM

%global npm_name isomorphic-fetch
%global enable_tests 0

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 2.2.1
Release: 1%{?dist}
Summary: Isomorphic WHATWG Fetch API, for Node & Browserify
License: MIT
URL: https://github.com/matthew-andrews/isomorphic-fetch/issues
Source0: http://registry.npmjs.org/isomorphic-fetch/-/isomorphic-fetch-2.2.1.tgz
Source1: http://registry.npmjs.org/node-fetch/-/node-fetch-1.7.3.tgz
Source2: http://registry.npmjs.org/whatwg-fetch/-/whatwg-fetch-2.0.3.tgz
Source3: http://registry.npmjs.org/encoding/-/encoding-0.1.12.tgz
Source4: http://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz
Source5: http://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.19.tgz
Source6: isomorphic-fetch-2.2.1-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(isomorphic-fetch) = 2.2.1
Provides: bundled-npm(node-fetch) = 1.7.3
Provides: bundled-npm(whatwg-fetch) = 2.0.3
Provides: bundled-npm(encoding) = 0.1.12
Provides: bundled-npm(is-stream) = 1.1.0
Provides: bundled-npm(iconv-lite) = 0.4.19
AutoReq: no
AutoProv: no


%description
%{summary}

%prep
mkdir npm_cache
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache ./npm_cache $tgz
done

%setup -T -q -a 6 -D -n npm_cache

%build
npm install --cache-min Infinity --cache . --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/isomorphic-fetch
cp -pfr .editorconfig .jshintrc .npmignore .travis.yml README.md bower.json fetch-bower.js fetch-npm-browserify.js fetch-npm-node.js package.json test node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf README.md ../../
# If any binaries are included, symlink them to bindir here

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
#$CHECK
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc README.md

%changelog
