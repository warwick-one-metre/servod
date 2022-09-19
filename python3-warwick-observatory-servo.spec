Name:           python3-warwick-observatory-servo
Version:        20220919
Release:        0
License:        GPL3
Summary:        Common backend code for servo controller daemon
Url:            https://github.com/warwick-one-metre/servod
BuildArch:      noarch

%description

%prep

rsync -av --exclude=build .. .

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
