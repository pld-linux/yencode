Summary:	Powerful yEnc decoder/encoder
Summary(pl):	Powerful yEnc decoder/encoder
Name:		yencode
Version:	0.46
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://www.yencode.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
yencode is an encoder/decoder package for the Usenet yEnc encoding
format. 
Full internationalization (multilingual) support provided by
GNU gettext. Encoder can output single part or multipart encoded
archives of any size. Smart decoder can handle multiple files,
including files specified out of order or with nonsense file names.
Included Usenet posting software posts files to Usenet quickly and
easily, including automatic retries and resumption of aborted
postings, plus automatic creation of encoded multipart archives and
SFV/CRC checksum files, if desired. Optional scan mode: automatically
locate and decode single or multipart encoded archives in specified
directories or recursively. Supports SFV file creation for
multiple-file archives.

%prep
%setup -q -n %{name}-%{version}

%build
aclocal
%{__autoconf}
autoheader
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/
%{_mandir}/man5/
