# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       ostree

# >> macros
# << macros

Summary:    Git for operating system binaries
Version:    2014.2
Release:    1
Group:      System/Libraries
License:    LGPLv2+
URL:        http://live.gnome.org/OSTree
Source0:    ostree-%{version}.tar.xz
Source1:    91-ostree.preset
Source100:  ostree.yaml
Requires:   dracut
Requires:   systemd
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libattr-devel
BuildRequires:  gpgme-devel
BuildRequires:  dracut
BuildRequires:  systemd

%description
OSTree is a tool for managing bootable, immutable, versioned
filesystem trees. While it takes over some of the roles of tradtional
"package managers" like dpkg and rpm, it is not a package system; nor
is it a tool for managing full disk images. Instead, it sits between
those levels, offering a blend of the advantages (and disadvantages)
of both.


%package devel
Summary:    Development headers for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package includes the header files for the %{name} library.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
cd upstream
env NOCONFIGURE=1 ./autogen.sh
# << build pre

%configure --disable-static \
    --disable-silent-rules \
    --disable-gtk-doc \
    --disable-libarchive \
    --with-dracut

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
cd upstream
# << install pre
%make_install

# >> install post
install -D -m 0644 %{SOURCE1} %{buildroot}/${_prefix}/lib/systemd/system-preset/91-ostree.preset
# << install post

%preun
# >> preun
%systemd_preun ostree-remount.service
# << preun

%post
/sbin/ldconfig
# >> post
%systemd_post ostree-remount.service
# << post

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/ostree
%{_sbindir}/ostree*
%{_datadir}/ostree
%{_sysconfdir}/dracut.conf.d/ostree.conf
%dir %{_prefix}/lib/dracut/modules.d/98ostree
%{_prefix}/lib/systemd/system/ostree*.service
%{_prefix}/lib/dracut/modules.d/98ostree/*
%{_libdir}/*.so.1*
%{_libdir}/girepository-1.0/OSTree-1.0.typelib
%{_prefix}/lib/systemd/system-preset/91-ostree.preset
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/OSTree-1.0.gir
# >> files devel
# << files devel