Summary:	Tool that allows you to change type of file system in the lack of backup space
Name:		convertfs
Version:	18mar2002
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://tzukanov.narod.ru/convertfs/%{name}-%{version}.tar.gz
# Source0-md5:	10fcab200d3722f008274ed11fe643af
URL:		http://tzukanov.narod.ru/convertfs/
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
case of power failure. It's expected that you have linux 2.4, glibc
2.2, recent util-linux, fileutils.

You can convert from virtually any filesystem type to virtually any
one as long as they are both block-oriented and supported by Linux for
read/write, and as long as primary filesystem supports sparse files.

%prep
%setup  -q -n %{name}

%build
sed -i -e 's#gcc#%{__cc}#g' Makefile
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sbindir}

install convertfs_dumb devclone devremap prepindex contrib/convertfs $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
