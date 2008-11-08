%define	name		fltk
%define	lib_name	lib%{name}
%define	version		1.1.9
%define	lib_major	1.1
%define	libname		%mklibname %{name} %lib_major
%define develname	%mklibname %name -d

Name:		fltk
Version:	1.1.9
Release:	%mkrel 3
Group: System/Libraries
Summary:	Fast Light Tool Kit (FLTK)
License:	LGPLv2+
Source: ftp://ftp.easysw.com/pub/fltk/%{version}/%{name}-%{version}-source.tar.bz2
URL: http://www.fltk.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	X11-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	jpeg-devel
BuildRequires:	png-devel
BuildRequires:	man
BuildRequires:	cmake

%description
The Fast Light Tool Kit ("FLTK", pronounced "fulltick") is a LGPL'd
C++ graphical user interface toolkit for X (UNIX(r)), OpenGL(r),
and Microsoft(r) Windows(r) NT 4.0, 95, or 98. It was originally
developed by Mr. Bill Spitzak and is currently maintained by a
small group of developers across the world with a central
repository in the US.

%package -n	%{libname}
Summary:	Fast Light Tool Kit (FLTK) - main library
Group:		System/Libraries
Obsoletes:	%{name} < %{version}-%{release}
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
The Fast Light Tool Kit ("FLTK", pronounced "fulltick") is a LGPL'd
C++ graphical user interface toolkit for X (UNIX(r)), OpenGL(r),
and Microsoft(r) Windows(r) NT 4.0, 95, or 98. It was originally
developed by Mr. Bill Spitzak and is currently maintained by a
small group of developers across the world with a central
repository in the US.

%package -n	%{develname}
Summary:	Fast Light Tool Kit (FLTK) - development environment
Group:		Development/C
Requires:	%{libname} = %{version}
Obsoletes:	%{name}-devel < %{version}-%{release}
Obsoletes:	%{_lib}%{name}1.1-devel
Provides:	%{name}-devel = %{version}-%{release}, %{lib_name}-devel = %{version}-%{release}

%description -n	%{develname}
The Fast Light Tool Kit ("FLTK", pronounced "fulltick") is a LGPL'd
C++ graphical user interface toolkit for X (UNIX(r)), OpenGL(r),
and Microsoft(r) Windows(r) NT 4.0, 95, or 98. It was originally
developed by Mr. Bill Spitzak and is currently maintained by a
small group of developers across the world with a central
repository in the US.

Install libfltk1-devel if you need to develop FLTK applications.  You'll
need to install the libfltk1.1 package if you plan to run dynamically 
linked applications.

%prep
%setup -q

%build
%cmake

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std -C build

# CMake official teste requires that CMakeCache are present
install -m 644 build/CMakeCache.txt %{buildroot}%{_libdir}/FLTK-%{lib_major}

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libfltk*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc README CHANGES
%{_includedir}/F?
%{_bindir}/*
%{_libdir}/libfltk*.so
%dir %{_libdir}/FLTK-%{lib_major}
%{_libdir}/FLTK-%{lib_major}/*
