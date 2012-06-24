#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	Multibyte
Summary:	String::Multibyte - Perl module to manipulate multibyte character strings
Summary(pl):	String::Multibyte - modu� Perla do obr�bki �a�cuch�w znak�w wielobajtowych
Name:		perl-String-Multibyte
Version:	1.05
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7307b6ec8998ddbc4e5fd7e629950c21
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides some functions which emulate the corresponding
CORE functions to manipulate multiple-byte character strings.

%description -l pl
Ten modu� udost�pnia troch� funkcji emuluj�cych odpowiadaj�ce im
funkcje CORE, s�u��cych do obr�bki �a�cuch�w znak�w wielobajtowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
