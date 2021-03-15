# Generated from zest-0.0.4.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name zest

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.4
Release: 2%{?dist}
Summary: Generated Api Bindings for Pulp3
Group: Development/Languages
License: GPLv2
URL: https://github.com/swagger-api/swagger-codegen
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 1.9
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(typhoeus) >= 1.0
Requires: %{?scl_prefix}rubygem(typhoeus) < 2
Requires: %{?scl_prefix}rubygem(typhoeus) >= 1.0.1
Requires: %{?scl_prefix_ruby}rubygem(json) >= 2.1
Requires: %{?scl_prefix_ruby}rubygem(json) < 3
Requires: %{?scl_prefix_ruby}rubygem(json) >= 2.1.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 1.9
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Generated Api bindings for Pulp3, built with the following components:
pulpcore-3.0.0b23 pulpcore-plugin-0.1.0b21 pulp_file-0.0.1b9 .


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
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/git_push.sh
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/docs
%{gem_instdir}/spec
%{gem_instdir}/zest.gemspec

%changelog
* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.0.4-2
- Rebuild for Ruby 2.7

* Tue Apr 02 2019 Tomer Brisker <tbrisker@gmail.com> 0.0.4-1
- Add rubygem-zest generated by gem2rpm using the scl template

