#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v21
# autospec commit: f07e061
#
# Source0 file verified with key 0x2209D6902F969C95 (meissner@suse.de)
#
Name     : libmtp
Version  : 1.1.22
Release  : 15
URL      : https://sourceforge.net/projects/libmtp/files/libmtp/1.1.22/libmtp-1.1.22.tar.gz
Source0  : https://sourceforge.net/projects/libmtp/files/libmtp/1.1.22/libmtp-1.1.22.tar.gz
Source1  : https://sourceforge.net/projects/libmtp/files/libmtp/1.1.22/libmtp-1.1.22.tar.gz.asc
Source2  : 2209D6902F969C95.pkey
Summary  : libmtp is a library for accessing Media Transfer Protocol devices
Group    : Development/Tools
License  : LGPL-2.1
Requires: libmtp-bin = %{version}-%{release}
Requires: libmtp-config = %{version}-%{release}
Requires: libmtp-lib = %{version}-%{release}
Requires: libmtp-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : file
BuildRequires : gnupg
BuildRequires : libgcrypt-dev
BuildRequires : pkgconfig(libusb-1.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Don-t-fallback-to-libdir-for-udev-path.patch

%description
Building and Installing
-----------------------
See the "INSTALL" file.
Initiator and Responder
-----------------------

%package bin
Summary: bin components for the libmtp package.
Group: Binaries
Requires: libmtp-config = %{version}-%{release}
Requires: libmtp-license = %{version}-%{release}

%description bin
bin components for the libmtp package.


%package config
Summary: config components for the libmtp package.
Group: Default

%description config
config components for the libmtp package.


%package dev
Summary: dev components for the libmtp package.
Group: Development
Requires: libmtp-lib = %{version}-%{release}
Requires: libmtp-bin = %{version}-%{release}
Provides: libmtp-devel = %{version}-%{release}
Requires: libmtp = %{version}-%{release}

%description dev
dev components for the libmtp package.


%package lib
Summary: lib components for the libmtp package.
Group: Libraries
Requires: libmtp-license = %{version}-%{release}

%description lib
lib components for the libmtp package.


%package license
Summary: license components for the libmtp package.
Group: Default

%description license
license components for the libmtp package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2209D6902F969C95' gpg.status
%setup -q -n libmtp-1.1.22
cd %{_builddir}/libmtp-1.1.22
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1743192542
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%reconfigure --disable-static --with-udev-group=plugdev \
--with-udev-mode=0660
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1743192542
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libmtp
cp %{_builddir}/libmtp-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libmtp/2cf3b1b4efcd76fbc3c4765a5f464898e8e10cc9 || :
export GOAMD64=v2
GOAMD64=v2
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/udev/hwdb.d/69-libmtp.hwdb
/usr/lib64/udev/mtp-probe

%files bin
%defattr(-,root,root,-)
/usr/bin/mtp-albumart
/usr/bin/mtp-albums
/usr/bin/mtp-connect
/usr/bin/mtp-delfile
/usr/bin/mtp-detect
/usr/bin/mtp-emptyfolders
/usr/bin/mtp-files
/usr/bin/mtp-filetree
/usr/bin/mtp-folders
/usr/bin/mtp-format
/usr/bin/mtp-getfile
/usr/bin/mtp-getplaylist
/usr/bin/mtp-hotplug
/usr/bin/mtp-newfolder
/usr/bin/mtp-newplaylist
/usr/bin/mtp-playlists
/usr/bin/mtp-reset
/usr/bin/mtp-sendfile
/usr/bin/mtp-sendtr
/usr/bin/mtp-thumb
/usr/bin/mtp-tracks
/usr/bin/mtp-trexist

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/69-libmtp.rules

%files dev
%defattr(-,root,root,-)
/usr/include/libmtp.h
/usr/lib64/libmtp.so
/usr/lib64/pkgconfig/libmtp.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmtp.so.9
/usr/lib64/libmtp.so.9.4.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libmtp/2cf3b1b4efcd76fbc3c4765a5f464898e8e10cc9
