# Generated from openscap-0.4.9.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name openscap

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.4.9
Release: 1%{?dist}
Summary: A FFI wrapper around the OpenSCAP library
Group: Development/Languages
License: GPL-2.0
URL: https://github.com/OpenSCAP/ruby-openscap
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(ffi) >= 1.0.9
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
A FFI wrapper around the OpenSCAP library.
Currently it provides only subset of libopenscap functionality.


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
%license %{gem_instdir}/COPYING
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Tue Sep 17 2019 Eric D. Helms <ericdhelms@gmail.com> 0.4.9-1
- Update to 0.4.9-1

* Tue Feb 14 2017 Dominic Cleal <dominic@cleal.org> 0.4.7-1
- Update openscap to 0.4.7 (mhulan@redhat.com)

* Mon Jan 04 2016 Dominic Cleal <dcleal@redhat.com> 0.4.3-2
- Fix dep to install correct test framework for F21 (dcleal@redhat.com)

* Fri Nov 06 2015 Dominic Cleal <dcleal@redhat.com> 0.4.3-1
- openscap version bump to 0.4.3, changed to non-SCL (shlomi@ben-hanna.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 0.4.2-3
- Converted to tfm SCL (dcleal@redhat.com)

* Fri Jan 23 2015 Marek Hulan <mhulan@redhat.com> 0.4.2-2
- new package built based on upstream spec

* Mon Jan 12 2015 Šimon Lukašík <slukasik@redhat.com> - 0.4.2-1
- upgrade to the new upstream version

* Sat Jan 10 2015 Šimon Lukašík <slukasik@redhat.com> - 0.4.1-1
- upgrade to the new upstream version

* Tue Dec 02 2014 Šimon Lukašík <slukasik@redhat.com> - 0.4.0-1
- upgrade to the new upstream version

* Thu Oct 23 2014 Šimon Lukašík <slukasik@redhat.com> - 0.3.0-1
- upgrade to the new upstream version

* Sat Sep 27 2014 Šimon Lukašík <slukasik@redhat.com> - 0.2.0-2
- fix dependency issue

* Fri Jul 25 2014 Šimon Lukašík <slukasik@redhat.com> - 0.2.0-1
- upgrade to the new upstream version

* Wed Jul 16 2014 Šimon Lukašík <slukasik@redhat.com> - 0.1.1-1
- upgrade to the new upstream version

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-5
- Avoid requires on a specific soname

* Wed May 21 2014 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-4
- Fallback to cp command

* Tue May 20 2014 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-3
- Moved COPYING and readme to the main package
- Created -devel sub-package out of -doc sub-package
- Dropped the word 'currently' from the package description
- Make a use of install instead of cp

* Tue May 06 2014 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-2
- corrected license tag
- avoided macro in comment

* Tue Apr 22 2014 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-1
- Initial package
