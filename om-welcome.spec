Name:		om-welcome
Version:	2.9.5
Release:	1
Summary:	OpenMandriva Lx Welcome Page
License:	GPLv2
Group:		System/Configuration/Other
URL:		https://github.com/OpenMandrivaAssociation/om-welcome
Source0:	%{name}-%version.tar.gz
Requires:	(kdialog or plasma6-kdialog)
Requires:	htmlscript >= 1.2.0
BuildRequires:	make
BuildRequires:	gettext
Obsoletes:	om-control-center
BuildArch:	noarch
%rename oma-welcome

%description
Startup and configuration tool for OpenMandriva Lx.

%prep
%autosetup -p1

%build
# Nothing to do here...

%install
%make_install

%find_lang om-welcome

# Adding update script
install -d %{buildroot}%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/om-update.desktop
[Desktop Entry]
Name=System Update
GenericName=System Update
Comment=Check for available system update and then install them
Exec=/usr/share/om-welcome/apps/updatesys.run
Icon=/usr/share/om-welcome/images/system-update.svg
Terminal=false
Type=Application
Categories=System
EOF

%files -f om-welcome.lang
%{_sysconfdir}/xdg/autostart/om-welcome.desktop
%{_bindir}/om-welcome
%{_bindir}/om-welcome-launcher
%{_datadir}/%{name}/*
%{_datadir}/applications/om-update.desktop
%{_datadir}/applications/om-welcome.desktop
