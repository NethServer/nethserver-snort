Summary: NethServer Snort IPS module
Name: nethserver-snort
Version: 1.0.0
Release: 1%{?dist}
License: GPL
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

Requires: snort >= 1:2.9.6.2-1 , snortalog
Requires: nethserver-base, nethserver-pulledpork

BuildRequires: nethserver-devtools
AutoReq: no

%description
Snort IPS module for NethServer.


%prep
%setup -q

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist


%post

%preun

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)

%changelog
* Wed Aug 20 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1.ns6
- IDS/IPS (snort) - Feature #1771 [NethServer]

