%define inochi_session_ver 0.8.4
%define inochi_session_semver 0.8.4
%define inochi_session_dist 0
%define inochi_session_commit cc0e3a47fbc9b4bb149a917fde0570be6931c5cb
%define inochi_session_short cc0e3a4

%if 0%{inochi_session_dist} > 0
%define inochi_session_suffix ^%{inochi_session_dist}.git%{inochi_session_short}
%endif

Name:           inochi-session
Version:        %{inochi_session_ver}%{?inochi_session_suffix:}
Release:        %autorelease
Summary:        Tool to use Inochi2D puppets

# Bundled lib licenses

# Static dependencies licenses
##   bindbc-loader licenses: BSL-1.0
##   bindbc-lua licenses: BSL-1.0
##   bindbc-sdl licenses: BSL-1.0
##   ddbus licenses: MIT
##   diet-ng licenses: MIT
##   dportals licenses: BSD-2-Clause
##   dunit licenses: MIT
##   eventcore licenses: MIT
##   facetrack-d licenses: BSD-2-Clause
##   fghj licenses: BSL-1.0
##   i18n-d licenses: BSD-2-Clause
##   i2d-imgui licenses: BSL-1.0 and MIT
##   i2d-opengl licenses: BSL-1.0
##   imagefmt licenses: BSD-2-Clause
##   inmath licenses: BSD-2-Clause
##   inochi2d licenses: BSD-2-Clause
##   inui licenses: BSD-2-Clause
##   lumars licenses: MIT
##   mir-algorithm licenses: Apache-2.0
##   mir-core licenses: Apache-2.0
##   mir-linux-kernel licenses: BSL-1.0
##   openssl licenses: OpenSSL
##   silly licenses: ISC
##   stdx-allocator licenses: BSD-2-Clause
##   taggedalgebraic licenses: BSD-2-Clause
##   tinyfiledialogs licenses: Zlib
##   vibe-container licenses: MIT
##   vibe-core licenses: MIT
##   vibe-d licenses: MIT
##   vmc-d licenses: BSD-2-Clause
License:        BSD-2-Clause and Apache-2.0 and BSL-1.0 and ISC and MIT and OpenSSL and Zlib

URL:            https://github.com/grillo-delmal/inochi-session-rpm

#https://github.com/Inochi2D/inochi-session/archive/{inochi_session_commit}/{name}-{inochi_session_short}.tar.gz
Source0:        %{name}-%{version}-norestricted.tar.gz
Source1:        icon.png

# Project maintained deps

Patch0:         inochi-session_0_icon-fix.patch
Patch1:         inochi-session_1_lumars.patch
Patch2:         inochi-session_2_metadata-fix.patch

# dlang
BuildRequires:  ldc
BuildRequires:  dub
BuildRequires:  jq

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  git

BuildRequires:  zdub-dub-settings-hack

BuildRequires:  zdub-bindbc-loader-static
BuildRequires:  zdub-bindbc-lua-static
BuildRequires:  zdub-bindbc-sdl-static
BuildRequires:  zdub-ddbus-static
BuildRequires:  zdub-diet-ng-static
BuildRequires:  zdub-dportals-static
BuildRequires:  zdub-dunit-static
BuildRequires:  zdub-eventcore-static
BuildRequires:  zdub-facetrack-d-static
BuildRequires:  zdub-fghj-static
BuildRequires:  zdub-i18n-d-static
BuildRequires:  zdub-i2d-imgui-static
BuildRequires:  zdub-i2d-opengl-static
BuildRequires:  zdub-imagefmt-static
BuildRequires:  zdub-inmath-static
BuildRequires:  zdub-inochi2d-static
BuildRequires:  zdub-inui-static
BuildRequires:  zdub-lumars-static
BuildRequires:  zdub-mir-algorithm-static
BuildRequires:  zdub-mir-core-static
BuildRequires:  zdub-mir-linux-kernel-static
BuildRequires:  zdub-openssl-static
BuildRequires:  zdub-silly-static
BuildRequires:  zdub-stdx-allocator-static
BuildRequires:  zdub-taggedalgebraic-static
BuildRequires:  zdub-tinyfiledialogs-static
BuildRequires:  zdub-vibe-container-static
BuildRequires:  zdub-vibe-core-static
BuildRequires:  zdub-vibe-d-static
BuildRequires:  zdub-vmc-d-static

Requires:       hicolor-icon-theme

#bindbc-lua deps
Requires:       luajit

#dportals deps
Requires:       dbus

#i2d-imgui deps
Requires:       libstdc++
Requires:       freetype
Requires:       SDL2

#openssl deps
Requires:       openssl


%description
Inochi2D is a framework for realtime 2D puppet animation which can be used for VTubing, 
game development and digital animation. 
Inochi Session is a tool that lets you use Inochi2D puppets as tracked avatars.
This is an unbranded build, unsupported by the official project.


%prep
%setup -n %{name}-%{inochi_session_commit}

# FIX: Inochi session version dependent on git
cat > source/session/ver.d <<EOF
module session.ver;

enum INS_VERSION = "%{inochi_session_semver}";
EOF

# FIX: Add fake dependency
mkdir -p deps/bindbc-spout2
cat > deps/bindbc-spout2/dub.sdl <<EOF
name "bindbc-spout2"
EOF
dub add-local deps/bindbc-spout2 "0.1.1"


%patch -P 0 -p1 -b .inochi-session-icon-fix
%patch -P 1 -p1 -b .inochi-session-lumars
%patch -P 2 -p1 -b .inochi-session-metadata-fix
mkdir -p deps

# Project maintained deps

%build
export DFLAGS="%{_d_optflags} -L-rpath=%{_libdir}/inochi-session/"
dub build \
    --cache=local \
    --config=barebones \
    --skip-registry=all \
    --non-interactive \
    --temp-build \
    --compiler=ldc2
mkdir ./out/
cp /tmp/.dub/build/inochi-session*/barebones*/* ./out/


%install
install -d ${RPM_BUILD_ROOT}%{_libdir}/inochi-session
install -p ./out/cimgui.so ${RPM_BUILD_ROOT}%{_libdir}/inochi-session/cimgui.so

install -d ${RPM_BUILD_ROOT}%{_bindir}
install -p ./out/inochi-session ${RPM_BUILD_ROOT}%{_bindir}/inochi-session

install -d ${RPM_BUILD_ROOT}%{_datadir}/applications/
install -p -m 644 ./build-aux/linux/inochi-session.desktop ${RPM_BUILD_ROOT}%{_datadir}/applications/inochi-session.desktop
desktop-file-validate \
    ${RPM_BUILD_ROOT}%{_datadir}/applications/inochi-session.desktop

install -d ${RPM_BUILD_ROOT}%{_metainfodir}/
install -p -m 644 ./build-aux/linux/inochi-session.appdata.xml ${RPM_BUILD_ROOT}%{_metainfodir}/inochi-session.appdata.xml
appstream-util validate-relax --nonet \
    ${RPM_BUILD_ROOT}%{_metainfodir}/inochi-session.appdata.xml

install -d $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/256x256/apps/
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/256x256/apps/inochi-session.png

# Dependency licenses
install -d ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/deps/
find ./deps/ -mindepth 1 -maxdepth 1 -exec \
    install -d ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/{} ';'

find ./deps/ -mindepth 2 -maxdepth 2 -iname '*LICENSE*' -exec \
    install -p -m 644 "{}" "${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/{}" ';'

install -d ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/res/
find ./res/ -mindepth 1 -maxdepth 1 -iname '*LICENSE*' -exec \
    install -p -m 644 {} ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/{} ';'


%files
%license LICENSE
%{_datadir}/licenses/%{name}/*
%{_bindir}/inochi-session
%{_libdir}/inochi-session/*
%{_metainfodir}/inochi-session.appdata.xml
%{_datadir}/applications/inochi-session.desktop
%{_datadir}/icons/hicolor/256x256/apps/inochi-session.png


%changelog
%autochangelog
