# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global scl_ruby_bin /usr/bin/%{?scl:%{scl_prefix}}ruby

%global gem_name puppet

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 6.12.0
Release: 1%{?dist}
Summary: Puppet, an automated configuration management tool
Group: Development/Languages
License: FIXME
URL: https://github.com/puppetlabs/puppet
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.3.0
Requires: %{?scl_prefix_ruby}ruby(rubygems) > 1.3.1
Requires: %{?scl_prefix}rubygem(facter) > 2.0.1
Requires: %{?scl_prefix}rubygem(facter) < 4
Requires: %{?scl_prefix}rubygem(hiera) >= 3.2.1
Requires: %{?scl_prefix}rubygem(hiera) < 4
Requires: %{?scl_prefix}rubygem(semantic_puppet) >= 1.0
Requires: %{?scl_prefix}rubygem(semantic_puppet) < 2
Requires: %{?scl_prefix}rubygem(fast_gettext) >= 1.1
Requires: %{?scl_prefix}rubygem(fast_gettext) < 2
Requires: %{?scl_prefix}rubygem(locale) >= 2.1
Requires: %{?scl_prefix}rubygem(locale) < 3
Requires: %{?scl_prefix_ror}rubygem(multi_json) >= 1.10
Requires: %{?scl_prefix_ror}rubygem(multi_json) < 2
Requires: %{?scl_prefix}rubygem(httpclient) >= 2.8
Requires: %{?scl_prefix}rubygem(httpclient) < 3
Requires: %{?scl_prefix}rubygem(puppet-resource_api) >= 1.5
Requires: %{?scl_prefix}rubygem(puppet-resource_api) < 2
Requires: %{?scl_prefix_ror}rubygem(concurrent-ruby) >= 1.0
Requires: %{?scl_prefix_ror}rubygem(concurrent-ruby) < 2
Requires: %{?scl_prefix}rubygem(deep_merge) >= 1.0
Requires: %{?scl_prefix}rubygem(deep_merge) < 2
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.3.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel > 1.3.1
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Puppet, an automated configuration management tool.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
%if %{?scl:1}%{!?scl:0}
  # shebangs
  for f in .%{_bindir}/* ; do
    sed -ri '1sX(^#!.*)X#!%{scl_ruby_bin}X' $f
  done
%endif
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/puppet
%{gem_instdir}/CODEOWNERS
%{gem_instdir}/CODE_OF_CONDUCT.md
%license %{gem_instdir}/COMMITTERS.md
%{gem_instdir}/Guardfile.example
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%exclude %{gem_instdir}/conf
%exclude %{gem_instdir}/ext
%exclude %{gem_instdir}/install.rb
%{gem_libdir}
%{gem_instdir}/locales
%{gem_instdir}/man
%{gem_instdir}/tasks
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.lock
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/spec

%changelog
* Thu Jan 16 2020 Eric D. Helms <ericdhelms@gmail.com> 6.12.0-1
- Add rubygem-puppet generated by gem2rpm using the scl template

