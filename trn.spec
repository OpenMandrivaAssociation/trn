%define Werror_cflags %nil
%define debug_package %nil

Summary:	A news reader that displays postings in threaded format
Name:		trn 
Version:	3.6
Release:	22
License:	Distributable
Group:		Networking/News
Url:		https://trn.sourceforge.net/
Source0:	ftp://ftp.uu.net:/networking/news/readers/trn/trn-3.6.tar.bz2
Source1:	trn.wmconfig
Patch0:		trn-3.6-linux.patch.bz2
Patch1:		trn-3.6-sigtstp.patch.bz2
Patch2:		trn-3.6-make.patch.bz2
Patch3:		trn-3.6-bool.patch.bz2
Patch4:		trn-3.6-jbj.patch.bz2
Patch5:		trn-3.6-rh.patch.bz2 

BuildRequires:	byacc, termcap-devel

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
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/trn
mkdir -p %{buildroot}%{_mandir}/man1/

chmod 755 filexp
chmod 755 makedir

make install	rnbin="%{buildroot}%{_bindir}" \
		rnlib="%{buildroot}%{_libdir}/trn" \
		mansrc="%{buildroot}%{_mandir}/man1" \
		installfilexp="%{buildroot}%{_libdir}/trn/filexp"

chmod 755 %{buildroot}%{_bindir}/*
chmod 755 %{buildroot}%{_libdir}/*

%files
%doc README INSTALL MANIFEST HINTS.TRN HACKERSGUIDE NEW
%{_bindir}/*
%{_libdir}/trn/*
%{_mandir}/man1/*
