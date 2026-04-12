Name:           systemd-coffeed
Version:        1.0
Release:        1%{?dist}
Group:          Applications/Productivity
Summary:        systemd does it all, it even makes coffee!

License:        GPL-3.0-or-later
URL:            https://github.com/aaaaadrien/systemd-coffeed
Source0:        https://github.com/aaaaadrien/%{name}/archive/refs/heads/main.zip
BuildArch:      noarch

BuildRequires:  systemd

Requires:       systemd
Requires:       bash

%description
systemd does it all, it even makes coffee!

%prep
%setup -qn systemd-coffeed

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
* Sun Apr 12 2026 Adrien_D <adriend@fedoraproject.org> - 1.0-1
- Version 1.0
- First version with official tag

* Thu Apr 09 2026 Ines WALLON <missd@drupalista.dev> - 1.0.0-1
- Version 1.0.0
