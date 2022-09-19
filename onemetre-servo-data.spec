Name:      onemetre-servo-data
Version:   20220919
Release:   0
Url:       https://github.com/warwick-one-metre/servod
Summary:   Servo controller configuration files.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch

%description

%build
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_sysconfdir}/servod/

%{__install} %{_sourcedir}/10-onemetre-redfocuser.rules %{buildroot}%{_udevrulesdir}
%{__install} %{_sourcedir}/onemetre.json %{buildroot}%{_sysconfdir}/servod/

%files
%defattr(0644,root,root,-)
%{_udevrulesdir}/10-onemetre-redfocuser.rules
%{_sysconfdir}/servod/onemetre.json

%changelog
