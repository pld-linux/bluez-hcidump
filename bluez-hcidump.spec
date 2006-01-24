Summary:	HCIDump - HCI packet analyzer
Summary(pl):	HCIDump - analizator pakiet�w HCI
Name:		bluez-hcidump
Version:	1.29
Release:	1
License:	GPL v2+
Group:		Networking/Utilities
Source0:	http://bluez.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	4e72efe8b67c3558eb776ad14e60de3e
URL:		http://bluez.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bluez-libs-devel >= 2.20
Requires:	bluez-libs >= 2.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HCIDump - HCI packet analyzer.

%description -l pl
HCIDump - analizator pakiet�w HCI.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
