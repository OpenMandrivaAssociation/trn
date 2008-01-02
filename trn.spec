Summary:	A news reader that displays postings in threaded format
Name:		trn 
Version:	3.6
Release:	%mkrel 18
License:	Distributable
Group:		Networking/News
Url:		http://trn.sourceforge.net/
Source0:	ftp://ftp.uu.net:/networking/news/readers/trn/trn-3.6.tar.bz2
Source1:	trn.wmconfig
Patch0:		trn-3.6-linux.patch.bz2
Patch1:		trn-3.6-sigtstp.patch.bz2
Patch2:		trn-3.6-make.patch.bz2
Patch3:		trn-3.6-bool.patch.bz2
Patch4:		trn-3.6-jbj.patch.bz2
Patch5:		trn-3.6-rh.patch.bz2 

Buildroot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	byacc, libtermcap-devel

%description
Trn is a basic news reader that supports threading. This version is
configured to read news from an NNTP news server.

Install trn if you need a basic news reader that shows you newsgroup
postings in threaded format.

%prep

%setup -q 
%patch0 -p1 -b .linux
%patch1 -p1 -b .sigstp
%patch2 -p1 -b .make
%patch3 -p1 -b .bool
%patch4 -p1 -b .jbj
%patch5 -p1 -b .rh 

%build
%make CFLAGS="-DI_TIME %optflags"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/trn
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/

chmod 755 filexp
chmod 755 makedir

make install	rnbin="$RPM_BUILD_ROOT%{_bindir}" \
		rnlib="$RPM_BUILD_ROOT%{_libdir}/trn" \
		mansrc="$RPM_BUILD_ROOT%{_mandir}/man1" \
		installfilexp="$RPM_BUILD_ROOT%{_libdir}/trn/filexp"

chmod 755 $RPM_BUILD_ROOT%{_bindir}/*
chmod 755 $RPM_BUILD_ROOT%{_libdir}/*

%clean 
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README INSTALL MANIFEST HINTS.TRN HACKERSGUIDE NEW
%{_bindir}/*
%{_libdir}/trn/*
%{_mandir}/man1/*

