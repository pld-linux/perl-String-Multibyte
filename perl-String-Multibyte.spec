#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	Multibyte
Summary:	String::Multibyte - Perl module to manipulate multibyte character strings
Summary(pl):	String::Multibyte - modu³ Perla do obróbki ³añcuchów znaków wielobajtowych
Name:		perl-String-Multibyte
Version:	1.03
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides some functions which emulate the corresponding
CORE functions to manipulate multiple-byte character strings.

%description -l pl
Ten modu³ udostêpnia trochê funkcji emuluj±cych odpowiadaj±ce im
funkcje CORE, s³u¿±cych do obróbki ³añcuchów znaków wielobajtowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
