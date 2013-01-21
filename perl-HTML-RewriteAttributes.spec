%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	RewriteAttributes
Summary:	HTML::RewriteAttributes -  concise attribute rewriting
Name:		perl-HTML-RewriteAttributes
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	808ac50716f778f410a87658bd00f40c
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::RewriteAttributes is designed for simple yet powerful HTML
attribute rewriting.

You simply specify a callback to run for each attribute and we do the
rest for you.

This module is designed to be subclassable to make handling special
cases eaiser. See the source for methods you can override.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/RewriteAttributes
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
