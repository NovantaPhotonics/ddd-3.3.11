# $Id: ddd.spec.in,v 1.4 2004/01/14 12:10:18 arnaud02 Exp $ -*- text -*-
# Spec for building DDD RPM Packages

# Note that this is NOT a relocatable package
%define name     ddd
%define ver      3.3.11
%define rel      1

Name: %name
Summary: graphical debugger front-end; GDB, DBX, Ladebug, JDB, Perl, Python
Version: %ver
Release: %rel
Copyright: GPL
Group: Development/Debuggers
Source: ftp://ftp.gnu.org/gnu/ddd/%{name}-%{ver}.tar.gz
URL: http://www.gnu.org/software/ddd/
Prereq: /sbin/install-info
BuildRoot: /var/tmp/%{name}-root

%description
DDD is a graphical front-end for command-line debuggers such as GDB,
DBX, WDB, Ladebug, JDB, XDB, the Perl debugger, or the Python
debugger.  Besides "usual" front-end features such as viewing source
texts, DDD has become famous through its interactive graphical data
display, where data structures are displayed as graphs.

%changelog
[ddd-3.2.1]
* Wed Nov 8  2000 Daniel Serodio <dserodio@email.com>
- Added missing files ($PREFIX/share/*) and fixed replaces .gz for .* so
  it works with Mandrake (.bz2)
- Replaced 1 with "1" (the macro wasn't expanded)
[ddd-3.2.91]
- Data themes
- Support for JDB 1.2
- Bug fixes

* Wed Nov 3  1999 Mirko Streckenbach <strecken@fmi.uni-passau.de>
- Initial skeleton, based on the .specs from gnome-libs-1.0.17 and 
  redhat 6.1 tar-1.13.11

%prep
%setup

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{_prefix} install

( cd $RPM_BUILD_ROOT
  for dir in .%{_prefix}/bin
  do
    [ -d $dir ] || continue
    strip $dir/* || :
  done
  gzip -9nf .%{_prefix}/info/ddd.info*
# bzip2 -9z .%{_prefix}/info/ddd.info*
  rm -f .%{_prefix}/info/dir
)

%post
/sbin/install-info %{_prefix}/info/ddd.info.* %{_prefix}/info/dir

%preun
if [ $1 = 0 ]; then
   /sbin/install-info --delete %{_prefix}/info/ddd.info.* %{_prefix}/info/dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ANNOUNCE BUGS COPYING COPYING.LIB CREDITS NEWS NICKNAMES OPENBUGS
%doc PROBLEMS README TIPS TODO
%doc doc/ddd-paper.ps doc/ddd.pdf doc/ddd.ps         
%{_prefix}/bin/ddd
%{_prefix}/man/man1/ddd.1*
%{_prefix}/info/ddd.info*
%{_prefix}/share/%{name}-%{ver}/vsllib/*
%{_prefix}/share/%{name}-%{ver}/themes/*
%{_prefix}/share/%{name}-%{ver}/ddd/Ddd
