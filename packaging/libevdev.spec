Name:           libevdev
Version:        1.2.2
Release:        0
License:        MIT
Summary:        wrapper library for evdev input devices
Url:            git://anongit.freedesktop.org/libevdev
Group:          System/Libraries
Source:         %{name}-%{version}.tar.gz
Source1001:		%name.manifest

BuildRequires:  doxygen
BuildRequires:  make
BuildRequires:  python

%global TZ_SYS_RO_SHARE  %{?TZ_SYS_RO_SHARE:%TZ_SYS_RO_SHARE}%{!?TZ_SYS_RO_SHARE:/usr/share}

%description
libevdev is a wrapper library for evdev devices. it moves the common
tasks when dealing with evdev devices into a library and provides a library
interface to the callers, thus avoiding erroneous ioctls, etc.


%package devel
Summary:    wrapper library for evdev input devices
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
libevdev is a wrapper library for evdev devices. it moves the common
tasks when dealing with evdev devices into a library and provides a library
interface to the callers, thus avoiding erroneous ioctls, etc.

%prep
%setup -q
cp %{SOURCE1001} .
%autogen

%build
make %{?jobs:-j%jobs} V=1

%install
%make_install
#%fdupes %{buildroot}

# for license notification
mkdir -p %{buildroot}/%{TZ_SYS_RO_SHARE}/license
cp -a %{_builddir}/%{buildsubdir}/COPYING %{buildroot}/%{TZ_SYS_RO_SHARE}/license/%{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%manifest %{name}.manifest
%defattr(-,root,root)
%{TZ_SYS_RO_SHARE}/license/%{name}
%{_bindir}/touchpad-edge-detector
%{_libdir}/*.so.*
%{_datadir}/*


%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
