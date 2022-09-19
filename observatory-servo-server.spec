Name:      observatory-servo-server
Version:   20220919
Release:   0
Url:       https://github.com/warwick-one-metre/servod
Summary:   Servo control server for Physik Instrumente C-863 hardware.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3 python3-Pyro4 python3-pyserial python3-warwick-observatory-common python3-warwick-observatory-servo

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_udevrulesdir}

%{__install} %{_sourcedir}/servod %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/servod@.service %{buildroot}%{_unitdir}

%files
%defattr(0755,root,root,-)
%{_bindir}/servod
%defattr(0644,root,root,-)
%{_unitdir}/servod@.service

%changelog
