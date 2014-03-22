%define dracutmoddir %{_prefix}/share/dracut/modules.d/90zgmcrypt

Name:		dracut-gmcrypt
Version:	1.2
Release:	1%{?dist}
Summary:	Provides passwordless unlocking of LUKS root volumes

Group:		System Environment/Base
License:	GPL
URL:		https://bitbucket.org/geekman/dracut-gmcrypt
Source0:	%{name}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

Requires:	dracut
Requires:	bash
Requires:	dmidecode
Requires:	cryptsetup-luks

%description
Provides passwordless unlocking of LUKS-encrypted root volumes.

%prep
%setup -q -n %{name}

%build

%install
rm -rf %{buildroot}

install -m 0755 -d $RPM_BUILD_ROOT/%{dracutmoddir}

install -m 0644 README.md $RPM_BUILD_ROOT/%{dracutmoddir}
for f in 90zgmcrypt/*; do
    install -m 0755 $f $RPM_BUILD_ROOT/%{dracutmoddir}
done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{dracutmoddir}
%{dracutmoddir}/check
%{dracutmoddir}/install
%{dracutmoddir}/installkernel
%{dracutmoddir}/add-key.sh
%{dracutmoddir}/gmcrypt-*.sh

%doc %{dracutmoddir}/README.md

%changelog
* Sun Mar 23 2014 - Darell Tan <darell.tan@gmail.com>
- increased iteration time to 3000ms
- use network card MAC address(es) for key generation

* Tue Mar 18 2014 - Darell Tan <darell.tan@gmail.com>
- bugfix

* Sat Mar 15 2014 - Darell Tan <darell.tan@gmail.com>
- initial build

