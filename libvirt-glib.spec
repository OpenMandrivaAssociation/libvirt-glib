%define oname		virt

%define api		1.0
%define major		0

%define libname_glib		%mklibname %{oname}-glib %{api} %{major}
%define develname_glib		%mklibname %{oname}-glib %{api} -d

%define libname_gconfig		%mklibname %{oname}-gconfig %{api} %{major}
%define develname_gconfig	%mklibname %{oname}-gconfig %{api} -d

%define libname_gobject		%mklibname %{oname}-gobject %{api} %{major}
%define develname_gobject	%mklibname %{oname}-gobject %{api} -d


%define girmajor	1.0
%define girname_glib		%mklibname %{oname}-glib-gir %{girmajor}
%define girname_gconfig		%mklibname %{oname}-gconfig-gir %{girmajor}
%define girname_gobject		%mklibname %{oname}-gobject-gir %{girmajor}

%define _exclude_files_from_autoreq ^%{_datadir}/doc/libvirt-glib-python/event-test.py$

Name:		libvirt-glib
Version:	0.0.9
Release:	1
Summary:	libvirt glib integration for events
Group:		System/Libraries
License:	LGPLv2+
URL:		http://libvirt.org/
Source0:	http://libvirt.org/sources/glib/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(glib-2.0) >= 2.10.0
BuildRequires:	pkgconfig(libvirt) >= 0.9.10
BuildRequires:	python-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	libxml2-devel
# Hack due to https://bugzilla.redhat.com/show_bug.cgi?id=613466
BuildRequires:	libtool
BuildRequires:	vala
BuildRequires:	vala-tools

%description
This package provides integration between libvirt and the glib
event loop.


# ---------------------------------------------------------------------------


%package -n %{libname_glib}
Group:		System/Libraries
Summary:	libvirt object APIs for processing object configuration
Provides:	%{mklibname %{oname}-glib %{major}} = %{version}-%{release}

%description -n %{libname_glib}
This package provides APIs for processing the object configuration
data

%files -n %{libname_glib}
%doc README COPYING AUTHORS ChangeLog NEWS
%{_libdir}/libvirt-glib-%{api}.so.%{major}*


%package -n %{develname_glib}
Group:		System/Libraries
Summary:	libvirt glib integration for events development files
Requires:	%{libname_glib} = %{version}-%{release}
Provides:	%{name}-glib-devel = %version-%release
Provides:	%{oname}-glib-devel = %{version}-%{release}

%description -n %{develname_glib}
This package provides development header files and libraries for
integration between libvirt and the glib event loop.

%files -n %{develname_glib}
%doc examples/event-test.c
%{_libdir}/libvirt-glib-%{api}.so
%{_libdir}/pkgconfig/libvirt-glib-%{api}.pc
%dir %{_includedir}/libvirt-glib-%{api}
%dir %{_includedir}/libvirt-glib-%{api}/libvirt-glib
%{_includedir}/libvirt-glib-%{api}/libvirt-glib/libvirt-glib.h
%{_includedir}/libvirt-glib-%{api}/libvirt-glib/libvirt-glib-*.h
%{_datadir}/gir-1.0/LibvirtGLib-%{girmajor}.gir
%{_datadir}/gtk-doc/html/Libvirt-glib
%{_datadir}/vala/vapi/libvirt-glib-%{api}.vapi


%package -n %{girname_glib}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname_glib} = %{version}-%{release}

%description -n %{girname_glib}
GObject Introspection interface description for %{name}.

%files -n %{girname_glib}
%{_libdir}/girepository-1.0/LibvirtGLib-%{girmajor}.typelib


# ---------------------------------------------------------------------------


%package -n %{libname_gconfig}
Group:		System/Libraries
Summary:	libvirt object APIs for processing object configuration
Provides:	%{mklibname %{oname}-gconfig %{major}} = %{version}-%{release}

%description -n %{libname_gconfig}
This package provides APIs for processing the object configuration
data

%files -n %{libname_gconfig}
%{_libdir}/libvirt-gconfig-%{api}.so.%{major}*


%package -n %{develname_gconfig}
Group:		System/Libraries
Summary:	libvirt object APIs for processing object configuration development files
Requires:	%{libname_gconfig} = %{version}-%{release}
Provides:	%{name}-gconfig-devel = %version-%release
Provides:	%{oname}-gconfig-devel = %{version}-%{release}

%description -n %{develname_gconfig}
This package provides development header files and libraries for
the object configuration APIs.

%files -n %{develname_gconfig}
%doc examples/event-test.c
%{_libdir}/libvirt-gconfig-%{api}.so
%{_libdir}/pkgconfig/libvirt-gconfig-%{api}.pc
%dir %{_includedir}/libvirt-gconfig-%{api}
%dir %{_includedir}/libvirt-gconfig-%{api}/libvirt-gconfig
%{_includedir}/libvirt-gconfig-%{api}/libvirt-gconfig/libvirt-gconfig.h
%{_includedir}/libvirt-gconfig-%{api}/libvirt-gconfig/libvirt-gconfig-*.h
%{_datadir}/gir-1.0/LibvirtGConfig-%{girmajor}.gir
%{_datadir}/gtk-doc/html/Libvirt-gconfig
%{_datadir}/vala/vapi/libvirt-gconfig-%{api}.vapi


%package -n %{girname_gconfig}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname_gconfig} = %{version}-%{release}

%description -n %{girname_gconfig}
GObject Introspection interface description for %{name}.

%files -n %{girname_gconfig}
%{_libdir}/girepository-1.0/LibvirtGConfig-%{girmajor}.typelib


# ---------------------------------------------------------------------------


%package -n %{libname_gobject}
Group:		System/Libraries
Summary:	libvirt object APIs for managing virtualization hosts
Provides:	%{mklibname %{oname}-gobject %{major}} = %{version}-%{release}

%description -n %{libname_gobject}
This package provides APIs for managing virtualization host
objects

%files -n %{libname_gobject}
%{_libdir}/libvirt-gobject-%{api}.so.%{major}*


%package -n %{develname_gobject}
Group:		System/Libraries
Summary:	libvirt object APIs for managing virtualization hosts development files
Requires:	%{libname_gobject} = %{version}-%{release}
Requires:	%{develname_glib} = %{version}-%{release}
Requires:	%{develname_gconfig} = %{version}-%{release}
Provides:	%{name}-gobject-devel = %version-%release
Provides:	%{oname}-gobject-devel = %{version}-%{release}

%description -n %{develname_gobject}
This package provides development header files and libraries for
managing virtualization host objects

%files -n %{develname_gobject}
%doc examples/event-test.c
%{_libdir}/libvirt-gobject-%{api}.so
%{_libdir}/pkgconfig/libvirt-gobject-%{api}.pc
%dir %{_includedir}/libvirt-gobject-%{api}
%dir %{_includedir}/libvirt-gobject-%{api}/libvirt-gobject
%{_includedir}/libvirt-gobject-%{api}/libvirt-gobject/libvirt-gobject.h
%{_includedir}/libvirt-gobject-%{api}/libvirt-gobject/libvirt-gobject-*.h
%{_datadir}/gir-1.0/LibvirtGObject-%{girmajor}.gir
%{_datadir}/gtk-doc/html/Libvirt-gobject
%{_datadir}/vala/vapi/libvirt-gobject-%{api}.vapi
%{_datadir}/vala/vapi/libvirt-gobject-%{api}.deps


%package -n %{girname_gobject}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname_gobject} = %{version}-%{release}

%description -n %{girname_gobject}
GObject Introspection interface description for %{name}.

%files -n %{girname_gobject}
%{_libdir}/girepository-1.0/LibvirtGObject-%{girmajor}.typelib


# ---------------------------------------------------------------------------


%package python
Group:		System/Libraries
Summary:	libvirt glib integration for events python binding

%description python
This package provides a python module for integration between
libvirt and the glib event loop

%files python
%doc examples/event-test.py
%{py_platsitedir}/*

# ---------------------------------------------------------------------------


%prep
%setup -q


%build
%configure2_5x --enable-introspection --with-python --disable-static
%make


%install
%makeinstall_std
# Fix up libtool libraries.
find %{buildroot} -name '*.la' | xargs rm
