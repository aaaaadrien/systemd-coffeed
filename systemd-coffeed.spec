%global debug_package %{nil}

Name:           systemd-coffeed
Version:        1.0.0
Release:        1%{?dist}
Group:          Applications/Productivity
Summary:        systemd does it all, it even makes the coffee !

License:        GPL-3.0-or-later
URL:            https://github.com/aaaaadrien/systemd-coffeed
Source0:        https://github.com/aaaaadrien/%{name}/archive/refs/heads/main.zip
BuildArch:      noarch

BuildRequires: systemd

Requires:       systemd
Requires:       bash

%description
systemd does it all, it even makes the coffee !

%prep
%setup -qn systemd-coffeed-main

%build

%install
install -d %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_unitdir}
install -m 644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service


%files
%defattr(-,root,root,-)
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service




%changelog
* Thu Apr 09 2026 Ines WALLON <missd@drupalista.dev> - 1.0.0-1
- Version 1.0.0
