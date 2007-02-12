Summary:	Simple svgalib dropin replacement that utilizes aalib
Summary(pl.UTF-8):   Prosta biblioteka zastępująca svgalib, oparta o aalib
Name:		aavga
Version:	1.0rc1
Release:	3
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/aa-project/%{name}-%{version}.tar.gz
# Source0-md5:	75c7c0be6d22ef52768568d5ec5c5c05
Patch0:		%{name}-update.patch
URL:		http://aa-project.sourceforge.net/aavga/
BuildRequires:	aalib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
# note: no obsoletes for svgalib - vgagl.so.1 may be useful

%description
Drop-in replacement for svgalib to wrap around aa, a wonderful ascii
art library. Allows squake to run in text mode.

%description -l pl.UTF-8
Prosta biblioteka zastępująca svgalib, odwołująca się do aalib -
biblioteki wyświetlającej grafikę jako ascii art. aavga pozwala
uruchamiać programy korzystające z svgalib w trybie tekstowym.

%prep
%setup -q -n %{name}-1.0
%patch0 -p1

%build
%{__cc} aavga.c -Wl,-soname,libvga.so.1 -o libvga.so.1.99.1 \
	-shared -nostdlib -fPIC %{rpmldflags} %{rpmcflags} -laa

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

install libvga.so.* $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/*
