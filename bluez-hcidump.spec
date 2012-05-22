Summary:	HCIDump - HCI packet analyzer
Summary(pl.UTF-8):	HCIDump - analizator pakietów HCI
Name:		bluez-hcidump
Version:	2.4
Release:	1
License:	GPL v2+
Group:		Networking/Utilities
#Source0Download: http://www.bluez.org/download.html
Source0:	http://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.xz
# Source0-md5:	6395229b4c6c1e59df0f2f13ac84226f
URL:		http://www.bluez.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	bluez-libs-devel >= 3.14
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
%configure \
	--disable-silent-rules

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
