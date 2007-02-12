Summary:	Powerful yEnc decoder/encoder
Summary(pl.UTF-8):	Potężny koder/dekoder yEnc
Name:		yencode
Version:	0.46
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	6af054f69c781cafa620063878a831ea
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

%description -l pl.UTF-8
yencode to koder/dekoder do usenetowego formatu kodowania yEnc. Jest w
pełni umiędzynarodowiony przez GNU gettext. Koder może wyprodukować
jedną część lub archiwum w wielu częściach o dowolnym rozmiarze.
Inteligentny dekoder może obsłużyć wiele plików, w tym pliki podane w
złej kolejności lub z bezsensownymi nazwami. Załączone narzędzie do
wysyłania postów na Usenet wysyła pliki szybko i łatwo, z
automatycznym powtarzaniem i wznawianiem przerwanego wysyłania oraz
automatycznym tworzeniem archiwów i plików sum kontrolnych SFV/CRC,
jeśli użytkownik ich sobie zażyczy. Opcjonalny tryb skanowania
automatycznie znajduje i dekoduje archiwa pojedyncze lub
wieloczęściowe w podanych katalogach lub rekurencyjnie. Obsługuje
tworzenie plików SFV do wieloczęściowych archiwów.

%prep
%setup -q

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[15]/*
