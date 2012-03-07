%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

Summary: CSS Cascading Style Sheets library for Python
Name: python-cssutils
Version: 0.9.7
Release: 2%{?dist}
License: LGPLv3+
Group: Development/Libraries
URL: http://cthedot.de/cssutils/
Source: http://cssutils.googlecode.com/files/cssutils-0.9.7.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# Required at runtime for the css* executables
Requires: python-setuptools
BuildRequires: python-devel
BuildRequires: python-setuptools
BuildRequires: dos2unix
BuildArch: noarch

%description
A Python package to parse and build CSS Cascading Style Sheets. DOM only, not
any rendering facilities.


%package doc
Summary: Documentation for the CSS Cascading Style Sheets library for Python
Group: Documentation

%description doc
This is the documentation for python-cssutils, a Python package to parse and
build CSS Cascading Style Sheets.


%prep
%setup -q -n cssutils-0.9.7
# Convert all CRLF files, keeping original timestamps
find . -type f -exec dos2unix -k {} \;


%build
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install \
    --single-version-externally-managed \
    -O1 --skip-build --root %{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
# The sources have some 2755 mode directories (as of 0.9.5.1), fix here
#defattr(-,root,root,0755)
%defattr(-,root,root,-)
%doc CHANGELOG.txt COPYING* README.txt
%{_bindir}/csscapture
%{_bindir}/csscombine
%{_bindir}/cssparse
%{python_sitelib}/cssutils-*.egg-info/
%{python_sitelib}/cssutils/
%{python_sitelib}/encutils/

%files doc
%defattr(-,root,root,-)
%doc docs/* examples/


%changelog
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 12 2011 Kevin Fenzi <kevin@tummy.com> - 0.9.7-1
- Update to final 0.9.7

* Sun Sep 12 2010 Kevin Fenzi <kevin@tummy.com> - 0.9.7-0.0.b3
- Update to 0.9.7 beta 3

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Feb 25 2010 Matthias Saou <http://freshrpms.net/> 0.9.6-1
- Update to 0.9.6.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.9.5.1-4
- Rebuild for Python 2.6

* Fri Oct 10 2008 Matthias Saou <http://freshrpms.net/> 0.9.5.1-3
- Add missing python-setuptools BR, split off doc sub-package (mschwendt).

* Thu Oct  9 2008 Matthias Saou <http://freshrpms.net/> 0.9.5.1-2
- Update license, group, add python-setuptools requirement (mschwendt).

* Tue Aug 19 2008 Matthias Saou <http://freshrpms.net/> 0.9.5.1-1
- Update to 0.9.5.1.

* Fri Aug  8 2008 Matthias Saou <http://freshrpms.net/> 0.9.5-1
- Update to 0.9.5 final.

* Tue Jul 15 2008 Matthias Saou <http://freshrpms.net/> 0.9.5b2-0.2.rc2
- Convert CRLF end of lines.
- Patch out #!/... magic from python files meant to be included and not run.

* Tue Jul 15 2008 Matthias Saou <http://freshrpms.net/> 0.9.5b2-0.1.rc2
- Initial RPM release.

