Name:		om-welcome
Version:	2.7.6
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

%files -f om-welcome.lang
%{_sysconfdir}/xdg/autostart/om-welcome.desktop
%{_bindir}/om-welcome
%{_bindir}/om-welcome-launcher
%{_datadir}/%{name}/*
%{_datadir}/applications/om-welcome.desktop
