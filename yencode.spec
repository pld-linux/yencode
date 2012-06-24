Summary:	Powerful yEnc decoder/encoder
Summary(pl):	Pot�ny koder/dekoder yEnc
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
pe�ni umi�dzynarodowiony przez GNU gettext. Koder mo�e wyprodujowa�
jedn� cz�� lub archiwum w wielu cz�ciach o dowolnym rozmiarze.
Inteligentny dekoder mo�e obs�u�y� wiele plik�w, w tym pliki podane w
z�ej kolejno�ci lub z bezsensownymi nazwami. Za��czone narz�dzie do
wysy�ania post�w na Usenet wysy�a pliki szybko i �atwo, z
automatycznym powtarzaniem i wznawianiem przerwanego wysy�ania oraz
automatycznym tworzeniem archiw�w i plik�w sum kontrolnych SFV/CRC,
je�li u�ytkownik ich sobie za�yczy. Opcjonalny tryb skanowania
automatycznie znajduje i dekoduje archiwa pojedyncze lub
wielocz�ciowe w podanych katalogach lub rekurencyjnie. Obs�uguje
tworzenie plik�w SFV do wielocz�ciowych archiw�w.

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
