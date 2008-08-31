Summary:	HCIDump - HCI packet analyzer
Summary(pl.UTF-8):	HCIDump - analizator pakietów HCI
Name:		bluez-hcidump
Version:	1.42
Release:	2
License:	GPL v2+
Group:		Networking/Utilities
#Source0Download: http://www.bluez.org/download.html
Source0:	http://bluez.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	5704737aaf72104eeaf77335218a1827
URL:		http://www.bluez.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bluez-libs-devel >= 3.14
Requires:	bluez-libs >= 3.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HCIDump - HCI packet analyzer.

%description -l pl.UTF-8
HCIDump - analizator pakietów HCI.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
%attr(755,root,root) %{_sbindir}/hcidump
%{_mandir}/man8/hcidump.8*
