Name:      observatory-servo-client
Version:   20220919
Release:   0
Url:       https://github.com/warwick-one-metre/servod
Summary:   Servo control client for Physik Instrumente C-863 hardware.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3 python3-Pyro4 python3-warwick-observatory-common python3-warwick-observatory-servo

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/servo %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/servo %{buildroot}/etc/bash_completion.d/servo

%files
%defattr(0755,root,root,-)
%{_bindir}/servo
/etc/bash_completion.d/servo

%changelog
