Summary:	Poldek Interaction library
Summary(pl.UTF-8):	Biblioteka interakcji z poldkiem
Name:		libpi
Version:	0.1.1
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://team.pld-linux.org/~wolf/pacman/%{name}-%{version}.tar.bz2
# Source0-md5:	a9fce2adb81897e8db43f4c92b605a24
URL:		http://team.pld-linux.org/~wolf/pacman/
BuildRequires:	libstdc++-devel
Requires:	poldek
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Poldek Interaction library.

%description -l pl.UTF-8
Biblioteka interakcji z poldkiem.

%package devel
Summary:	libpi header files
Summary(pl.UTF-8):	Pliki nagłówkowe libpi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
libpi header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe libpi.

%prep
%setup -q

%build
%{__make} \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags} -DNDEBUG -fPIC" \
	LDFLAGS="%{rpmldflags}" \
	PCH=0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/libpi}

install libpi.so.*.*.* $RPM_BUILD_ROOT%{_libdir}
install *.h $RPM_BUILD_ROOT%{_includedir}/libpi

cd $RPM_BUILD_ROOT%{_libdir}
ln -sf libpi.so.*.*.* libpi.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpi.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpi.so
%{_includedir}/libpi
#%exclude %{_includedir}/libpi/all.h*
