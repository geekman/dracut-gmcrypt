%define dracutmoddir %{_prefix}/share/dracut/modules.d/90zgmcrypt
%if 0%{?el7}
%define dracutmoddir %{_prefix}/lib/dracut/modules.d/90zgmcrypt
%endif

Name:		dracut-gmcrypt
Version:	1.3
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
* Sat Nov 08 2014 - Darell Tan <darell.tan@gmail.com>
- updated scripts to work with dracut 033 used by CentOS 7
- updated install path for the dracut module

* Sun Mar 23 2014 - Darell Tan <darell.tan@gmail.com>
- increased iteration time to 3000ms
- use network card MAC address(es) for key generation

* Tue Mar 18 2014 - Darell Tan <darell.tan@gmail.com>
- bugfix

* Sat Mar 15 2014 - Darell Tan <darell.tan@gmail.com>
- initial build

