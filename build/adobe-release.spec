Name:       adobe-release
Version:    1.0
Release:    2%{?dist}
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

BuildArch: noarch

%description
Adobe Linux repository configuration.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
install -m 644 adobe.repo $RPM_BUILD_ROOT/etc/yum.repos.d/

install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
install -m 644 RPM-GPG-KEY-adobe $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
/etc/pki/rpm-gpg/RPM-GPG-KEY-adobe
/etc/yum.repos.d/adobe.repo

%changelog
* Sun May 20 2012 Chris Smart <chris@kororaa.org> - 1.1
- Small changes to spec file, update for Kororaa 17.

* Mon Dec 26 2011 Chris Smart <chris@kororaa.org> - 1.0
- Initial package.
