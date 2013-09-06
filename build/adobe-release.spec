Name:       adobe-release
Version:    1.2
Release:    2%{?dist}.1
Summary:    Adobe repository configuration

Group:      System Environment/Base
License:    BSD
URL:        http://adobe.com
Source0:    %{name}-%{version}.tar.gz
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Provides:   adobe-release-i386
Provides:   adobe-release-x86_64
Obsoletes:  adobe-release-i386
Obsoletes:  adobe-release-x86_64

# In order to provide 32bit flash to 64bit systems,
# we need to split these packages again
#BuildArch: noarch

%description
Adobe Linux repository configuration.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
%ifarch x86_64
install -m 644 adobe.repo-64 $RPM_BUILD_ROOT/etc/yum.repos.d/adobe.repo
%else
install -m 644 adobe.repo $RPM_BUILD_ROOT/etc/yum.repos.d/adobe.repo
%endif

install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
install -m 644 RPM-GPG-KEY-adobe $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
/etc/pki/rpm-gpg/RPM-GPG-KEY-adobe
%config(noreplace) /etc/yum.repos.d/adobe.repo

%changelog
* Fri Sep 6 2013 Chris Smart <csmart@kororaproject.org> - 1.2-2
- Disable 32bit flash in 64bit repo by default

* Sun Feb 7 2013 Chris Smart <csmart@kororaproject.org> - 1.2-1
- Split out packages into archs, so that users can install 32bit flash on 64bit systems.

* Sun May 20 2012 Chris Smart <chris@kororaa.org> - 1.1
- Small changes to spec file, update for Kororaa 17.

* Mon Dec 26 2011 Chris Smart <chris@kororaa.org> - 1.0
- Initial package.
