Summary:	Tool that allows you to change type of file system in the lack of backup space
Summary(pl):	Narzêdzie pozwalaj±ce zmieniæ typ systemu plików bez miejsca na kopiê zapasow±
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
Ten prosty zestaw narzêdzi pozwala zmieniæ typ systemu plików w
przypadku braku miejsca na kopiê zapasow±. Idea polega na
wykorzystaniu obs³ugi rzadkich plików na g³ównym systemie plików.
Narzêdzie tworzy rzadki obraz urz±dzenia blokowego, przy u¿yciu mkfs
robi na nim nowy system plików, montuje go, przy u¿yciu mv przenosi
pliki z g³ównego systemu plików na podmontowany obraz, a nastêpnie
mapuje obraz na urz±dzenie.

Narzêdzie do remapowania u¿ywa rodzaju kroniki, aby zapobiec
uszkodzeniom w przypadku awarii zasilania. Narzêdzia s± pisane dla
Linuksa 2.4, glibc 2.2, nowych wersji util-linux i fileutils.

Mo¿na konwertowaæ z prawie ka¿dego typu systemu plików na prawie
ka¿dy, o ile oba s± zorientowane blokowo oraz ich odczyt i zapis s±
obs³ugiwane przez Linuksa, a g³ówny system plików obs³uguje pliki
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
