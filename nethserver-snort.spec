Summary: NethServer Snort IPS module
Name: nethserver-snort
Version: 1.1.0
Release: 1%{?dist}
License: GPL
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

Requires: snort >= 2.9.8, snortalog
Requires: perl-GDGraph
Requires: nethserver-firewall-base, nethserver-pulledpork

BuildRequires: nethserver-devtools

%description
Snort IPS module for NethServer.


%prep
%setup -q

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist


%post

%preun

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update

%changelog
* Thu Jul 07 2016 Stefano Fancello <stefano.fancello@nethesis.it> - 1.1.0-1
- First NS7 release

* Tue Sep 29 2015 Davide Principi <davide.principi@nethesis.it> - 1.0.3-1
- Make Italian language pack optional - Enhancement #3265 [NethServer]

* Wed Jul 15 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1
- snort HOME_NET should include trusted networks - Enhancement #3221 [NethServer]
- snort DNS_SERVERS var redefined - Bug #3211 [NethServer]

* Tue May 19 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- snort does not start if policy=security - Bug #3161 [NethServer]
- Dashboard: execute snortalog only when accessing IPS tab - Enhancement #2864 [NethServer]

* Wed Aug 20 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1.ns6
- IDS/IPS (snort) - Feature #1771 [NethServer]

