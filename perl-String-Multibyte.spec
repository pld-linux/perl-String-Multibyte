#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	String
%define		pnam	Multibyte
Summary:	String::Multibyte - Perl module to manipulate multibyte character strings
Summary(pl.UTF-8):	String::Multibyte - moduł Perla do obróbki łańcuchów znaków wielobajtowych
Name:		perl-String-Multibyte
Version:	1.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	82821825e95ed2e608b2a687a95c8189
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides some functions which emulate the corresponding
CORE functions to manipulate multiple-byte character strings.

%description -l pl.UTF-8
Ten moduł udostępnia trochę funkcji emulujących odpowiadające im
funkcje CORE, służących do obróbki łańcuchów znaków wielobajtowych.

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
