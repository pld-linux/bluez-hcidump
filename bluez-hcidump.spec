Summary:	HCIDump - HCI packet analyzer
Summary(pl):	HCIDump - analizator pakietów HCI
Name:		bluez-hcidump
Version:	1.8
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://bluez.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	90aada08e16175a6effd4d4dd43fa4f5
Patch0:		%{name}-opt.patch
Patch1:		%{name}-amfix.patch
URL:		http://bluez.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bluez-libs-devel >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HCIDump - HCI packet analyzer.

%description -l pl
HCIDump - analizator pakietów HCI.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
