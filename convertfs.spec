Summary:	Tool that allows you to change type of file system in the lack of backup space
Summary(pl):	Narz�dzie pozwalaj�ce zmieni� typ systemu plik�w bez miejsca na kopi� zapasow�
Name:		convertfs
Version:	13jan2005
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/System
Source0:	http://tzukanov.narod.ru/convertfs/%{name}-%{version}.tar.gz
# Source0-md5:	71e8065e321898e259a55c8cefdfd75d
Patch0:		%{name}-safety.patch
Patch1:		%{name}-Makefile.patch
URL:		http://tzukanov.narod.ru/convertfs/
BuildRequires:	sed >= 4.0
Requires:	util-linux
Requires:	coreutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This simple toolset allows you to change type of file system in the
lack of backup space. The idea is to use sparse files support of
primary filesystem. We create a sparse image of block device, mkfs
secondary filesystem on it, mount it, mv files from primary filesystem
to mounted image and then map image to the device.

Remapping utility uses some kind of journaling to avoid breakage in
case of power failure. It's expected that you have Linux 2.4, glibc
2.2, recent util-linux, fileutils.

You can convert from virtually any filesystem type to virtually any
one as long as they are both block-oriented and supported by Linux for
read/write, and as long as primary filesystem supports sparse files.

%description -l pl
Ten prosty zestaw narz�dzi pozwala zmieni� typ systemu plik�w w
przypadku braku miejsca na kopi� zapasow�. Idea polega na
wykorzystaniu obs�ugi rzadkich plik�w na g��wnym systemie plik�w.
Narz�dzie tworzy rzadki obraz urz�dzenia blokowego, przy u�yciu mkfs
robi na nim nowy system plik�w, montuje go, przy u�yciu mv przenosi
pliki z g��wnego systemu plik�w na podmontowany obraz, a nast�pnie
mapuje obraz na urz�dzenie.

Narz�dzie do remapowania u�ywa rodzaju kroniki, aby zapobiec
uszkodzeniom w przypadku awarii zasilania. Narz�dzia s� pisane dla
Linuksa 2.4, glibc 2.2, nowych wersji util-linux i fileutils.

Mo�na konwertowa� z prawie ka�dego typu systemu plik�w na prawie
ka�dy, o ile oba s� zorientowane blokowo oraz ich odczyt i zapis s�
obs�ugiwane przez Linuksa, a g��wny system plik�w obs�uguje pliki
rzadkie.

%prep
%setup  -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install convertfs_dumb devclone devremap prepindex contrib/convertfs $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
