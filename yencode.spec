Summary:	Powerful yEnc decoder/encoder
Summary(pl):	Potê¿ny koder/dekoder yEnc
Name:		yencode
Version:	0.46
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://www.yencode.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
yencode is an encoder/decoder package for the Usenet yEnc encoding
format. Full internationalization (multilingual) support provided by
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

%description -l pl
yencode to koder/dekoder do usenetowego formatu kodowania yEnc. Jest w
pe³ni umiêdzynarodowiony przez GNU gettext. Koder mo¿e wyprodujowaæ
jedn± czê¶æ lub archiwum w wielu czê¶ciach o dowolnym rozmiarze.
Inteligentny dekoder mo¿e obs³u¿yæ wiele plików, w tym pliki podane w
z³ej kolejno¶ci lub z bezsensownymi nazwami. Za³±czone narzêdzie do
wysy³ania postów na Usenet wysy³a pliki szybko i ³atwo, z
automatycznym powtarzaniem i wznawianiem przerwanego wysy³ania oraz
automatycznym tworzeniem archiwów i plików sum kontrolnych SFV/CRC,
je¶li u¿ytkownik ich sobie za¿yczy. Opcjonalny tryb skanowania
automatycznie znajduje i dekoduje archiwa pojedyncze lub
wieloczê¶ciowe w podanych katalogach lub rekurencyjnie. Obs³uguje
tworzenie plików SFV do wieloczê¶ciowych archiwów.

%prep
%setup -q -n %{name}-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
%{_mandir}/man[15]/*
