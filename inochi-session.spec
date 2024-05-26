%define inochi_session_ver 0.8.4
%define inochi_session_semver 0.8.4
%define inochi_session_dist 0
%define inochi_session_commit cc0e3a47fbc9b4bb149a917fde0570be6931c5cb
%define inochi_session_short cc0e3a4

# Project maintained deps
%define dportals_semver 0.1.0
%define dportals_commit 52e805408bc43c2f74a480e16e17d8d58682fd1f
%define dportals_short 52e8054

%define facetrack_d_semver 0.7.8
%define facetrack_d_commit f9539205d831bd2c135b989e9f9ea48629af9256
%define facetrack_d_short f953920

%define fghj_semver 1.0.2
%define fghj_commit cb73df65e289c820e801c62401c8048c03c806bf
%define fghj_short cb73df6

%define i18n_d_semver 1.0.2
%define i18n_d_commit 75c57ea0889d459b73765d932aec02f9b3e71b80
%define i18n_d_short 75c57ea

%define i2d_imgui_semver 0.8.0+build.4.ge34f8ba
%define i2d_imgui_commit e34f8ba04c0085be7ee83a8df200cf2ffb30bfd3
%define i2d_imgui_short e34f8ba

%define i2d_opengl_semver 1.0.0
%define i2d_opengl_commit 985ab89dd82aafc7f0733e855096a38b4a612762
%define i2d_opengl_short 985ab89

%define inmath_semver 1.0.6
%define inmath_commit 6ee33a0e160bcf0c0286a16e232feeeae2306548
%define inmath_short 6ee33a0

%define inochi2d_semver 0.8.4
%define inochi2d_commit e6049a86c5c1712e828acc293dba6f554ba0155e
%define inochi2d_short e6049a8

%define inui_semver 1.2.1+build.4.g4b260a5
%define inui_commit 4b260a54de54cd1a15ee71e0943d7b797347c931
%define inui_short 4b260a5

%define vmc_d_semver 1.1.3
%define vmc_d_commit df1a3b2c1a2bd1cb185c21e3c0a11c611755bb66
%define vmc_d_short df1a3b2

# Indirect deps
%define bindbc_loader_ver 1.0.3
%define bindbc_lua_ver 0.5.1
%define bindbc_sdl_ver 1.1.3
%define ddbus_ver 3.0.0-beta.2
%define diet_ng_ver 1.8.1
%define dunit_ver 1.0.16
%define eventcore_ver 0.9.30
%define imagefmt_ver 2.1.2
%define lumars_ver 1.6.1
%define mir_algorithm_ver 3.22.1
%define mir_core_ver 1.7.1
%define mir_linux_kernel_ver 1.0.1
%define openssl_ver 3.3.3
%define openssl_static_ver 1.0.5+3.0.8
%define silly_ver 1.1.1
%define stdx_allocator_ver 2.77.5
%define taggedalgebraic_ver 0.11.23
%define tinyfiledialogs_ver 0.10.1
%define vibe_container_ver 1.3.1
%define vibe_core_ver 2.8.4
%define vibe_d_ver 0.9.8

# cimgui
%define cimgui_commit 49bb5ce65f7d5eeab7861d8ffd5aa2a58ca8f08c
%define cimgui_short 49bb5ce
%define imgui_commit dd5b7c6847372016f45d5b5abda687bd5cd19224
%define imgui_short dd5b7c6

%if 0%{inochi_session_dist} > 0
%define inochi_session_suffix ^%{inochi_session_dist}.git%{inochi_session_short}
%endif

Name:           inochi-session
Version:        %{inochi_session_ver}%{?inochi_session_suffix:}
Release:        %autorelease
Summary:        Tool to use Inochi2D puppets

License:        BSD2 and MIT

URL:            https://github.com/Inochi2D/inochi-session

#https://github.com/Inochi2D/inochi-session/archive/{inochi_session_commit}/{name}-{inochi_session_short}.tar.gz
Source0:        %{name}-%{version}-norestricted.tar.gz
Source1:        inochi-session.appdata.xml
Source2:        icon.png
Source3:        generate-tarball.sh
Source4:        README.md

# Project maintained deps
Source5:        https://github.com/Inochi2D/dportals/archive/%{dportals_commit}/dportals-%{dportals_short}.tar.gz
Source6:        https://github.com/Inochi2D/facetrack-d/archive/%{facetrack_d_commit}/facetrack-d-%{facetrack_d_short}.tar.gz
Source7:        https://github.com/Inochi2D/fghj/archive/%{fghj_commit}/fghj-%{fghj_short}.tar.gz
Source8:        https://github.com/KitsunebiGames/i18n/archive/%{i18n_d_commit}/i18n-%{i18n_d_short}.tar.gz
Source9:        https://github.com/Inochi2D/i2d-imgui/archive/%{i2d_imgui_commit}/i2d-imgui-%{i2d_imgui_short}.tar.gz
Source10:       https://github.com/Inochi2D/i2d-opengl/archive/%{i2d_opengl_commit}/i2d-opengl-%{i2d_opengl_short}.tar.gz
Source11:       https://github.com/Inochi2D/inmath/archive/%{inmath_commit}/inmath-%{inmath_short}.tar.gz
Source12:       https://github.com/Inochi2D/inochi2d/archive/%{inochi2d_commit}/inochi2d-%{inochi2d_short}.tar.gz
Source13:       https://github.com/Inochi2D/inui/archive/%{inui_commit}/inui-%{inui_short}.tar.gz
Source14:       https://github.com/Inochi2D/vmc-d/archive/%{vmc_d_commit}/vmc-%{vmc_d_short}.tar.gz

# Indirect deps
Source15:       https://github.com/BindBC/bindbc-loader/archive/refs/tags/v%{bindbc_loader_ver}/bindbc-loader-%{bindbc_loader_ver}.tar.gz
Source16:       https://github.com/BindBC/bindbc-lua/archive/refs/tags/v%{bindbc_lua_ver}/bindbc-lua-%{bindbc_lua_ver}.tar.gz
Source17:       https://github.com/BindBC/bindbc-sdl/archive/refs/tags/v%{bindbc_sdl_ver}/bindbc-sdl-%{bindbc_sdl_ver}.tar.gz
Source18:       https://github.com/trishume/ddbus/archive/refs/tags/v%{ddbus_ver}/ddbus-%{ddbus_ver}.tar.gz
Source19:       https://github.com/rejectedsoftware/diet-ng/archive/refs/tags/v%{diet_ng_ver}/diet-ng-%{diet_ng_ver}.tar.gz
Source20:       https://github.com/nomad-software/dunit/archive/refs/tags/v%{dunit_ver}/dunit-%{dunit_ver}.tar.gz
Source21:       https://github.com/vibe-d/eventcore/archive/refs/tags/v%{eventcore_ver}/eventcore-%{eventcore_ver}.tar.gz
Source22:       https://github.com/tjhann/imagefmt/archive/refs/tags/v%{imagefmt_ver}/imagefmt-%{imagefmt_ver}.tar.gz
Source23:       https://github.com/BradleyChatha/lumars/archive/refs/tags/v%{lumars_ver}/lumars-%{lumars_ver}.tar.gz
Source24:       https://github.com/libmir/mir-algorithm/archive/refs/tags/v%{mir_algorithm_ver}/mir-algorithm-%{mir_algorithm_ver}.tar.gz
Source25:       https://github.com/libmir/mir-core/archive/refs/tags/v%{mir_core_ver}/mir-core-%{mir_core_ver}.tar.gz
Source26:       https://github.com/libmir/mir-linux-kernel/archive/refs/tags/v%{mir_linux_kernel_ver}/mir-linux-kernel-%{mir_linux_kernel_ver}.tar.gz
Source27:       https://github.com/D-Programming-Deimos/openssl/archive/refs/tags/v%{openssl_ver}/openssl-%{openssl_ver}.tar.gz
Source28:       https://github.com/bildhuus/deimos-openssl-static/archive/refs/tags/v%{openssl_static_ver}/openssl-static-%{openssl_static_ver}.tar.gz
Source29:       https://gitlab.com/AntonMeep/silly/-/archive/v%{silly_ver}/silly-v%{silly_ver}.tar.gz
Source30:       https://github.com/wilzbach/stdx-allocator/archive/refs/tags/v%{stdx_allocator_ver}/stdx-allocator-%{stdx_allocator_ver}.tar.gz
Source31:       https://github.com/s-ludwig/taggedalgebraic/archive/refs/tags/v%{taggedalgebraic_ver}/taggedalgebraic-%{taggedalgebraic_ver}.tar.gz
Source32:       https://github.com/dayllenger/tinyfiledialogs-d/archive/refs/tags/v%{tinyfiledialogs_ver}/tinyfiledialogs-d-%{tinyfiledialogs_ver}.tar.gz
Source33:       https://github.com/vibe-d/vibe-container/archive/refs/tags/v%{vibe_container_ver}/vibe-container-%{vibe_container_ver}.tar.gz
Source34:       https://github.com/vibe-d/vibe-core/archive/refs/tags/v%{vibe_core_ver}/vibe-core-%{vibe_core_ver}.tar.gz
Source35:       https://github.com/vibe-d/vibe.d/archive/refs/tags/v%{vibe_d_ver}/vibe-d-%{vibe_d_ver}.tar.gz

# cimgui
Source36:       https://github.com/Inochi2D/cimgui/archive/%{cimgui_commit}/cimgui-%{cimgui_short}.tar.gz
Source37:       https://github.com/Inochi2D/imgui/archive/%{imgui_commit}/imgui-%{imgui_short}.tar.gz

Patch0:         inochi-session_0.8.3_icon-fix.patch
Patch1:         inochi-session_0.8.3_lumars.patch
Patch2:         inochi2d_0.8.3_no-gitver.patch

# dlang
BuildRequires:  ldc
BuildRequires:  dub

# cimgui
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  freetype-devel
BuildRequires:  SDL2-devel
BuildRequires:  dbus-devel

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  git

Requires:       luajit
Requires:       hicolor-icon-theme


%description
Inochi2D is a framework for realtime 2D puppet animation which can be used for VTubing, 
game development and digital animation. 
Inochi Session is a tool that lets you use Inochi2D puppets as tracked avatars.
This is an unbranded build, unsupported by the official project.

%prep
%setup -n %{name}-%{inochi_session_commit}
%patch 0 -p1 -b .icon-fix
%patch 1 -p1 -b .lumars

mkdir deps

# Project maintained deps
tar -xzf %{SOURCE5}
mv dportals-%{dportals_commit} deps/dportals
dub add-local deps/dportals/ "%{dportals_semver}"

tar -xzf %{SOURCE6}
mv facetrack-d-%{facetrack_d_commit} deps/facetrack-d
dub add-local deps/facetrack-d/ "%{facetrack_d_semver}"

tar -xzf %{SOURCE7}
mv fghj-%{fghj_commit} deps/fghj
dub add-local deps/fghj/ "%{fghj_semver}"

tar -xzf %{SOURCE8}
mv i18n-%{i18n_d_commit} deps/i18n-d
dub add-local deps/i18n-d/ "%{i18n_d_semver}"

tar -xzf %{SOURCE9}
mv i2d-imgui-%{i2d_imgui_commit} deps/i2d-imgui
dub add-local deps/i2d-imgui/ "%{i2d_imgui_semver}"

tar -xzf %{SOURCE10}
mv i2d-opengl-%{i2d_opengl_commit} deps/i2d-opengl
dub add-local deps/i2d-opengl/ "%{i2d_opengl_semver}"

tar -xzf %{SOURCE11}
mv inmath-%{inmath_commit} deps/inmath
dub add-local deps/inmath/ "%{inmath_semver}"

tar -xzf %{SOURCE12}
mv inochi2d-%{inochi2d_commit} deps/inochi2d
dub add-local deps/inochi2d/ "%{inochi2d_semver}"

pushd deps; pushd inochi2d
%patch 2 -p1 -b .inochi2d-no-gitver
# FIX: Inochi2D version dependent on git
cat > source/inochi2d/ver.d <<EOF
module inochi2d.ver;

enum IN_VERSION = "%{inochi2d_semver}";
EOF
popd; popd

tar -xzf %{SOURCE13}
mv inui-%{inui_commit} deps/inui
dub add-local deps/inui/ "%{inui_semver}"

tar -xzf %{SOURCE14}
mv vmc-d-%{vmc_d_commit} deps/vmc-d
dub add-local deps/vmc-d/ "%{vmc_d_semver}"

# Indirect Deps

tar -xzf %{SOURCE15}
mv bindbc-loader-%{bindbc_loader_ver} deps/bindbc-loader
dub add-local deps/bindbc-loader/ "%{bindbc_loader_ver}"

tar -xzf %{SOURCE16}
mv bindbc-lua-%{bindbc_lua_ver} deps/bindbc-lua
dub add-local deps/bindbc-lua/ "%{bindbc_lua_ver}"

tar -xzf %{SOURCE17}
mv bindbc-sdl-%{bindbc_sdl_ver} deps/bindbc-sdl
dub add-local deps/bindbc-sdl/ "%{bindbc_sdl_ver}"

tar -xzf %{SOURCE18}
mv ddbus-%{ddbus_ver} deps/ddbus
dub add-local deps/ddbus/ "%{ddbus_ver}"

tar -xzf %{SOURCE19}
mv diet-ng-%{diet_ng_ver} deps/diet-ng
dub add-local deps/diet-ng/ "%{diet_ng_ver}"

tar -xzf %{SOURCE20}
mv dunit-%{dunit_ver} deps/dunit
dub add-local deps/dunit/ "%{dunit_ver}"

tar -xzf %{SOURCE21}
mv eventcore-%{eventcore_ver} deps/eventcore
dub add-local deps/eventcore/ "%{eventcore_ver}"

tar -xzf %{SOURCE22}
mv imagefmt-%{imagefmt_ver} deps/imagefmt
dub add-local deps/imagefmt/ "%{imagefmt_ver}"

tar -xzf %{SOURCE23}
mv lumars-%{lumars_ver} deps/lumars
dub add-local deps/lumars/ "%{lumars_ver}"

tar -xzf %{SOURCE24}
mv mir-algorithm-%{mir_algorithm_ver} deps/mir-algorithm
dub add-local deps/mir-algorithm/ "%{mir_algorithm_ver}"

tar -xzf %{SOURCE25}
mv mir-core-%{mir_core_ver} deps/mir-core
dub add-local deps/mir-core/ "%{mir_core_ver}"

tar -xzf %{SOURCE26}
mv mir-linux-kernel-%{mir_linux_kernel_ver} deps/mir-linux-kernel
dub add-local deps/mir-linux-kernel/ "%{mir_linux_kernel_ver}"

tar -xzf %{SOURCE27}
mv openssl-%{openssl_ver} deps/openssl
dub add-local deps/openssl/ "%{openssl_ver}"

tar -xzf %{SOURCE28}
mv deimos-openssl-static-* deps/openssl-static
dub add-local deps/openssl-static/ "%{openssl_static_ver}"

tar -xzf %{SOURCE29}
mv silly-v%{silly_ver} deps/silly
dub add-local deps/silly/ "%{silly_ver}"

tar -xzf %{SOURCE30}
mv stdx-allocator-%{stdx_allocator_ver} deps/stdx-allocator
dub add-local deps/stdx-allocator/ "%{stdx_allocator_ver}"

tar -xzf %{SOURCE31}
mv taggedalgebraic-%{taggedalgebraic_ver} deps/taggedalgebraic
dub add-local deps/taggedalgebraic/ "%{taggedalgebraic_ver}"

tar -xzf %{SOURCE32}
mv tinyfiledialogs-d-%{tinyfiledialogs_ver} deps/tinyfiledialogs
dub add-local deps/tinyfiledialogs/ "%{tinyfiledialogs_ver}"

tar -xzf %{SOURCE33}
mv vibe-container-%{vibe_container_ver} deps/vibe-container
dub add-local deps/vibe-container/ "%{vibe_container_ver}"

tar -xzf %{SOURCE34}
mv vibe-core-%{vibe_core_ver} deps/vibe-core
dub add-local deps/vibe-core/ "%{vibe_core_ver}"

tar -xzf %{SOURCE35}
mv vibe.d-%{vibe_d_ver} deps/vibe-d
dub add-local deps/vibe-d/ "%{vibe_d_ver}"

# cimgui

tar -xzf %{SOURCE36}
rm -r deps/i2d-imgui/deps/cimgui
mv cimgui-%{cimgui_commit} deps/i2d-imgui/deps/cimgui

tar -xzf %{SOURCE37}
rm -r deps/i2d-imgui/deps/cimgui/imgui
mv imgui-%{imgui_commit} deps/i2d-imgui/deps/cimgui/imgui

# FIX: Inochi session version dependent on git
cat > source/session/ver.d <<EOF
module session.ver;

enum INS_VERSION = "%{inochi_session_semver}";
EOF

# FIX: Inochi2D version dependent on git
cat > deps/inochi2d/source/inochi2d/ver.d <<EOF
module inochi2d.ver;

enum IN_VERSION = "%{inochi2d_semver}";
EOF

# FIX: make i2d-imgui submodule checking only check cimgui
rm deps/i2d-imgui/.gitmodules
cat > deps/i2d-imgui/.gitmodules <<EOF
[submodule "deps/cimgui"]
	path = deps/cimgui
	url = https://github.com/Inochi2D/cimgui.git
EOF
mkdir deps/i2d-imgui/deps/cimgui/.git

# FIX: Add fake dependency
mkdir -p deps/bindbc-spout2
cat > deps/bindbc-spout2/dub.sdl <<EOF
name "bindbc-spout2"
EOF
dub add-local deps/bindbc-spout2 "0.1.1"

mkdir -p deps/libasync
cat > deps/libasync/dub.sdl <<EOF
name "libasync"
EOF
dub add-local deps/libasync "0.8.6"


%build
export DFLAGS="%{_d_optflags} -L-rpath=%{_libdir}/inochi-session/"
dub build --config=barebones --skip-registry=all --compiler=ldc2


%install
install -d ${RPM_BUILD_ROOT}%{_libdir}/inochi-session
install -p ./out/cimgui.so ${RPM_BUILD_ROOT}%{_libdir}/inochi-session/cimgui.so

install -d ${RPM_BUILD_ROOT}%{_bindir}
install -p ./out/inochi-session ${RPM_BUILD_ROOT}%{_bindir}/inochi-session

install -d ${RPM_BUILD_ROOT}%{_datadir}/applications/
install -p -m 644 build-aux/linux/inochi-session.desktop ${RPM_BUILD_ROOT}%{_datadir}/applications/inochi-session.desktop
desktop-file-validate \
    ${RPM_BUILD_ROOT}%{_datadir}/applications/inochi-session.desktop

install -d ${RPM_BUILD_ROOT}%{_metainfodir}/
install -p -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_metainfodir}/inochi-session.appdata.xml
appstream-util validate-relax --nonet \
    ${RPM_BUILD_ROOT}%{_metainfodir}/inochi-session.appdata.xml

install -d $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/256x256/apps/
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/256x256/apps/inochi-session.png

# Dependency licenses
install -d ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/./deps/i2d-imgui/cimgui/
install -p -m 644 ./deps/i2d-imgui/deps/cimgui/LICENSE \
    ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/./deps/i2d-imgui/cimgui/LICENSE
install -d ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/./deps/i2d-imgui/imgui/
install -p -m 644 ./deps/i2d-imgui/deps/cimgui/imgui/LICENSE.txt \
    ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/./deps/i2d-imgui/imgui/LICENSE.txt

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
%{_libdir}/inochi-session/cimgui.so
%{_metainfodir}/inochi-session.appdata.xml
%{_datadir}/applications/inochi-session.desktop
%{_datadir}/icons/hicolor/256x256/apps/inochi-session.png


%changelog
%autochangelog