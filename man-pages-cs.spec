%define coreutils_version 20081218
Summary: Czech man pages from the Linux Documentation Project
Name: man-pages-cs
Version: 0.18.20090209
Release: 2.1%{?dist}
License: GFDL and GPL+
Group: Documentation
URL: http://sweb.cz/tropikhajma/man-pages-cs/index.html
Source: http://tropikhajma.sweb.cz/%{name}/%{name}-%{version}.tar.lzma
Patch1: man-pages-cs-01.patch
Patch2: man-pages-cs-02.patch
Patch3: man-pages-cs-03.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
Manual pages from the Linux Documentation Project, translated into
Czech.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
# coreutils directory contains newer version
rm ./procps/kill.1
rm ./procps/uptime.1
rm ./man-pages/man1/du.1
# links to ls - better version in coreutils directory
rm ./man-pages/man1/dir.1
rm ./man-pages/man1/vdir.1

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_mandir}
make install DESTDIR=$RPM_BUILD_ROOT MANDIR=%{_mandir}/cs

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CONTRIB README README.Czech
%dir %{_mandir}/cs
%{_mandir}/cs/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.18.20090209-2.1
- Rebuilt for RHEL 6

* Tue Sep 15 2009 Ivana Varekova <varekova@redhat.com> - 0.18.20090209-2
- fix instalation part
- remove duplicate files
- add patches created by Ludek Dolihal

* Tue Sep 15 2009 Ivana Varekova <varekova@redhat.com> - 0.18.20090209-1
- update to 0.18.20090209

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.20080113-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.20080113-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Ivana Varekova <varekova@redhat.com> - 0.17.20080113-6
- update another part of coreutils man-pages (patches are from Kamil Dudka)

* Thu Dec  8 2008 Ivana Varekova <varekova@redhat.com> - 0.17.20080113-5
- update another part of coreutils man-pages (patches are from Kamil Dudka)

* Thu Dec  4 2008 Ivana Varekova <varekova@redhat.com> - 0.17.20080113-4
- update another part of coreutils man-pages (patches are from Kamil Dudka)

* Mon Dec  1 2008 Ivana Varekova <varekova@redhat.com> - 0.17.20080113-3
- update part of coreutils man-pages (patches are from Kamil Dudka)

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.17.20080113-2
- fix license tag

* Tue Jan 15 2008 Ivana Varekova <varekova@redhat.com> - 0.17.20080113-1
- update to 0.17.20080113

* Thu Nov 22 2007 Ivana Varekova <varekova@redhat.com> - 0.17.20070905-1
- update to 0.17.20070905
- patch to build in RPM_BUILD_ROOT (thanks Milan Kerslager)

* Fri Mar  2 2007 Ivana Varekova <varekova@redhat.com> - 0.16-7
- Resolves: 226121
  incorporate the package review feedback

* Fri Aug 11 2006 Ivana Varekova <varekova@redhat.com> - 0.16-6
- remove at.1 man page to right directory (#202049)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.16-5.1.1
- rebuild

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Aug  5 2005 Ivana Varekova <varekova@redhat.com> 0.16-5
- remove lastlog man page (man page is removed to shadow-utils)

* Wed Sep 29 2004 Adrian Havill <havill@redhat.com> 0.16-4
- rebuilt, n-v-r

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 10 2004 Akira TAGOH <tagoh@redhat.com> 0.16-2
- removed man.1 because the latest man contains it.

* Thu Feb 06 2003 Adrian Havill <havill@redhat.com>
- make iconv use UTF8 (#78717)
- update to 0.16

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Nov 25 2002 Tim Powers <timp@redhat.com>
- remove the shadow manpage since it conflicts with shadow-utils now

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Aug 14 2001 Tim Powers <timp@redhat.com>
- rebuilt to hopefully fix the rpm verify problem

* Thu Aug  2 2001 Trond Eivind Glomsrød <teg@redhat.com>
- s/Copyright/License/
- Own %%{_mandir}/cs

* Tue Apr  3 2001 Trond Eivind Glomsrød <teg@redhat.com>
- make pdf2dsc(1) use hyphen.cs, not hyphens.cs (#34181)

* Tue Dec 19 2000 Trond Eivind Glomsrød <teg@redhat.com>
- 0.14
- new location

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun 20 2000 Jeff Johnson <jbj@redhat.com>
- rebuild to compress man pages.

* Sun Jun 11 2000 Trond Eivind Glomsrød <teg@redhat.com>
- first build
