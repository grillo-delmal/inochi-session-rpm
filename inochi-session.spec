%define inochi_session_ver 0.5.3
%define inochi_session_semver 0.5.3
%define inochi_session_dist 0
%define inochi_session_commit d74a491c0021d260842f2501dec272dc3e31f2e2
%define inochi_session_short d74a491

# Project maintained deps
%define bindbc_imgui_semver 0.7.0+build.20.g237a209
%define bindbc_imgui_commit 237a209b0b35ec4766f4263b4d599fac59bd4dc1
%define bindbc_imgui_short 237a209

%define bindbc_spout2_semver 0.1.1
%define bindbc_spout2_commit 3d6e26f73a754946a0000d4c096c18a2bb6320f2
%define bindbc_spout2_short 3d6e26f

%define facetrack_d_semver 0.6.2+build.32.g9e1b2b1
%define facetrack_d_commit 9e1b2b1d8f968828c6bfd545287ad60fd48ab97c
%define facetrack_d_short 9e1b2b1

%define fghj_semver 1.0.0
%define fghj_commit 7d8b68001ebef41c78709e8dfa78fbf24e75bffd
%define fghj_short 7d8b680

%define gitver_semver 1.5.0
%define gitver_commit 8616ef003a324fb5067a5e5f9da665898f4fe922
%define gitver_short 8616ef0

%define i18n_d_semver 1.0.1+build.1.ge4a7f0b
%define i18n_d_commit e4a7f0bdee45b02cd5dba622046681a4cde20199
%define i18n_d_short e4a7f0b

%define inmath_semver 1.0.3+build.4.gec62993
%define inmath_commit ec629939647eac2d6e44003adee35fbaddba78e8
%define inmath_short ec62993

%define inochi2d_semver 0.7.2+build.17.g0e32b36
%define inochi2d_commit 0e32b364f07e704641033ef9243a9520825d42d0
%define inochi2d_short 0e32b36

%define inui_semver 1.0.0+build.0-og.0.0.0.build.35.g38cd2fa
%define inui_commit 38cd2fa30cac4845b5f6ad8383c7439453f8fb74
%define inui_short 38cd2fa

%define vmc_d_semver 1.1.1+build.4.gb32fb96
%define vmc_d_commit b32fb96b4ce9a6357b193fb297e44edd8e6112ed
%define vmc_d_short b32fb96

# Indirect deps
%define bindbc_loader_ver 1.0.1
%define bindbc_lua_ver 0.5.0
%define bindbc_opengl_ver 1.0.2
%define bindbc_sdl_ver 1.1.3
%define imagefmt_ver 2.1.2
%define lumars_ver 1.4.1
%define mir_algorithm_ver 3.14.11
%define mir_core_ver 1.1.109
%define semver_ver 0.3.4
%define silly_ver 1.1.1
%define taggedalgebraic_ver 0.11.22
%define tinyfiledialogs_ver 0.10.1

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
Summary:        Tool to create and edit Inochi2D puppets

License:        BSD2 and MIT

URL:            https://github.com/Inochi2D/inochi-session

#https://github.com/Inochi2D/inochi-session/archive/{inochi_session_commit}/{name}-{inochi_session_short}.tar.gz
Source0:        %{name}-%{version}-norestricted.tar.gz
Source1:        generate-tarball.sh
Source2:        README.md

# Project maintained deps
Source3:        https://github.com/Inochi2D/bindbc-imgui/archive/%{bindbc_imgui_commit}/bindbc-imgui-%{bindbc_imgui_short}.tar.gz
Source4:        https://github.com/Inochi2D/bindbc-spout2/archive/%{bindbc_spout2_commit}/bindbc-spout2-%{bindbc_spout2_short}.tar.gz
Source5:        https://github.com/Inochi2D/facetrack-d/archive/%{facetrack_d_commit}/facetrack-d-%{facetrack_d_short}.tar.gz
Source6:        https://github.com/Inochi2D/fghj/archive/%{fghj_commit}/fghj-%{fghj_short}.tar.gz
Source7:        https://github.com/Inochi2D/gitver/archive/%{gitver_commit}/gitver-%{gitver_short}.tar.gz
Source8:        https://github.com/KitsunebiGames/i18n/archive/%{i18n_d_commit}/i18n-%{i18n_d_short}.tar.gz
Source9:        https://github.com/Inochi2D/inmath/archive/%{inmath_commit}/inmath-%{inmath_short}.tar.gz
Source10:       https://github.com/Inochi2D/inochi2d/archive/%{inochi2d_commit}/inochi2d-%{inochi2d_short}.tar.gz
Source11:       https://github.com/Inochi2D/inui/archive/%{inui_commit}/inui-%{inui_short}.tar.gz
Source12:       https://github.com/Inochi2D/vmc-d/archive/%{vmc_d_commit}/vmc-%{vmc_d_short}.tar.gz

# Indirect deps
Source13:       https://github.com/BindBC/bindbc-loader/archive/refs/tags/v%{bindbc_loader_ver}/bindbc-loader-%{bindbc_loader_ver}.tar.gz
Source14:       https://github.com/BindBC/bindbc-lua/archive/refs/tags/v%{bindbc_lua_ver}/bindbc-lua-%{bindbc_lua_ver}.tar.gz
Source15:       https://github.com/BindBC/bindbc-opengl/archive/refs/tags/v%{bindbc_opengl_ver}/bindbc-opengl-%{bindbc_opengl_ver}.tar.gz
Source16:       https://github.com/BindBC/bindbc-sdl/archive/refs/tags/v%{bindbc_sdl_ver}/bindbc-sdl-%{bindbc_sdl_ver}.tar.gz
Source17:       https://github.com/tjhann/imagefmt/archive/refs/tags/v%{imagefmt_ver}/imagefmt-%{imagefmt_ver}.tar.gz
Source18:       https://github.com/BradleyChatha/lumars/archive/refs/tags/v%{lumars_ver}/lumars-%{lumars_ver}.tar.gz
Source19:       https://github.com/libmir/mir-algorithm/archive/refs/tags/v%{mir_algorithm_ver}/mir-algorithm-%{mir_algorithm_ver}.tar.gz
Source20:       https://github.com/libmir/mir-core/archive/refs/tags/v%{mir_core_ver}/mir-core-%{mir_core_ver}.tar.gz
Source21:       https://github.com/dcarp/semver/archive/refs/tags/v%{semver_ver}/semver-%{semver_ver}.tar.gz
Source22:       https://gitlab.com/AntonMeep/silly/-/archive/v%{silly_ver}/silly-v%{silly_ver}.tar.gz
Source23:       https://github.com/s-ludwig/taggedalgebraic/archive/refs/tags/v%{taggedalgebraic_ver}/taggedalgebraic-%{taggedalgebraic_ver}.tar.gz
Source24:       https://github.com/dayllenger/tinyfiledialogs-d/archive/refs/tags/v%{tinyfiledialogs_ver}/tinyfiledialogs-d-%{tinyfiledialogs_ver}.tar.gz

# cimgui
Source25:       https://github.com/Inochi2D/cimgui/archive/%{cimgui_commit}/cimgui-%{cimgui_short}.tar.gz
Source26:       https://github.com/Inochi2D/imgui/archive/%{imgui_commit}/imgui-%{imgui_short}.tar.gz

Patch0:         inochi-session_0.5.3_appdata-fix.patch

# dlang
BuildRequires:  ldc
BuildRequires:  dub

# cimgui
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  freetype-devel
BuildRequires:  SDL2-devel

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  git

Requires:       xprop

%description
Inochi2D is a framework for realtime 2D puppet animation which can be used for VTubing, 
game development and digital animation. 
Inochi Session is a tool that lets you use Inochi2D puppets as tracked avatars.

%prep
%setup -n %{name}-%{inochi_session_commit}
%patch0 -p1 -b .appdata-fix

mkdir deps

# Project maintained deps
tar -xzf %{SOURCE3}
mv bindbc-imgui-%{bindbc_imgui_commit} deps/bindbc-imgui
dub add-local deps/bindbc-imgui/ "%{bindbc_imgui_semver}"

tar -xzf %{SOURCE4}
mv bindbc-spout2-%{bindbc_spout2_commit} deps/bindbc-spout2
dub add-local deps/bindbc-spout2/ "%{bindbc_spout2_semver}"

tar -xzf %{SOURCE5}
mv facetrack-d-%{facetrack_d_commit} deps/facetrack-d
dub add-local deps/facetrack-d/ "%{facetrack_d_semver}"

tar -xzf %{SOURCE6}
mv fghj-%{fghj_commit} deps/fghj
dub add-local deps/fghj/ "%{fghj_semver}"

tar -xzf %{SOURCE7}
mv gitver-%{gitver_commit} deps/gitver
dub add-local deps/gitver/ "%{gitver_semver}"

tar -xzf %{SOURCE8}
mv i18n-%{i18n_d_commit} deps/i18n-d
dub add-local deps/i18n-d/ "%{i18n_d_semver}"

tar -xzf %{SOURCE9}
mv inmath-%{inmath_commit} deps/inmath
dub add-local deps/inmath/ "%{inmath_semver}"

tar -xzf %{SOURCE10}
mv inochi2d-%{inochi2d_commit} deps/inochi2d
dub add-local deps/inochi2d/ "%{inochi2d_semver}"

tar -xzf %{SOURCE11}
mv inui-%{inui_commit} deps/inui
dub add-local deps/inui/ "%{inui_semver}"

tar -xzf %{SOURCE12}
mv vmc-d-%{vmc_d_commit} deps/vmc-d
dub add-local deps/vmc-d/ "%{vmc_d_semver}"

# Indirect Deps

tar -xzf %{SOURCE13}
mv bindbc-loader-%{bindbc_loader_ver} deps/bindbc-loader
dub add-local deps/bindbc-loader/ "%{bindbc_loader_ver}"

tar -xzf %{SOURCE14}
mv bindbc-lua-%{bindbc_lua_ver} deps/bindbc-lua
dub add-local deps/bindbc-lua/ "%{bindbc_lua_ver}"

tar -xzf %{SOURCE15}
mv bindbc-opengl-%{bindbc_opengl_ver} deps/bindbc-opengl
dub add-local deps/bindbc-opengl/ "%{bindbc_opengl_ver}"

tar -xzf %{SOURCE16}
mv bindbc-sdl-%{bindbc_sdl_ver} deps/bindbc-sdl
dub add-local deps/bindbc-sdl/ "%{bindbc_sdl_ver}"

tar -xzf %{SOURCE17}
mv imagefmt-%{imagefmt_ver} deps/imagefmt
dub add-local deps/imagefmt/ "%{imagefmt_ver}"

tar -xzf %{SOURCE18}
mv lumars-%{lumars_ver} deps/lumars
dub add-local deps/lumars/ "%{lumars_ver}"

tar -xzf %{SOURCE19}
mv mir-algorithm-%{mir_algorithm_ver} deps/mir-algorithm
dub add-local deps/mir-algorithm/ "%{mir_algorithm_ver}"

tar -xzf %{SOURCE20}
mv mir-core-%{mir_core_ver} deps/mir-core
dub add-local deps/mir-core/ "%{mir_core_ver}"

tar -xzf %{SOURCE21}
mv semver-%{semver_ver} deps/semver
dub add-local deps/semver/ "%{semver_ver}"

tar -xzf %{SOURCE22}
mv silly-v%{silly_ver} deps/silly
dub add-local deps/silly/ "%{silly_ver}"

tar -xzf %{SOURCE23}
mv taggedalgebraic-%{taggedalgebraic_ver} deps/taggedalgebraic
dub add-local deps/taggedalgebraic/ "%{taggedalgebraic_ver}"

tar -xzf %{SOURCE24}
mv tinyfiledialogs-d-%{tinyfiledialogs_ver} deps/tinyfiledialogs
dub add-local deps/tinyfiledialogs/ "%{tinyfiledialogs_ver}"

# cimgui

tar -xzf %{SOURCE25}
rm -r deps/bindbc-imgui/deps/cimgui
mv cimgui-%{cimgui_commit} deps/bindbc-imgui/deps/cimgui

tar -xzf %{SOURCE26}
rm -r deps/bindbc-imgui/deps/cimgui/imgui
mv imgui-%{imgui_commit} deps/bindbc-imgui/deps/cimgui/imgui

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

# FIX: make bindbc-imgui submodule checking only check cimgui
rm deps/bindbc-imgui/.gitmodules
cat > deps/bindbc-imgui/.gitmodules <<EOF
[submodule "deps/cimgui"]
	path = deps/cimgui
	url = https://github.com/Inochi2D/cimgui.git
EOF
mkdir deps/bindbc-imgui/deps/cimgui/.git


%build
export DFLAGS="%{_d_optflags} -L-rpath=%{_libdir}/inochi-session/"
dub build --config=barebones --skip-registry=all --compiler=ldc2


%install
install -d ${RPM_BUILD_ROOT}%{_libdir}/inochi-session
install -p ./out/cimgui.so ${RPM_BUILD_ROOT}%{_libdir}/inochi-session/cimgui.so

install -d ${RPM_BUILD_ROOT}%{_bindir}
install -p ./out/inochi-session ${RPM_BUILD_ROOT}%{_bindir}/inochi-session

install -d ${RPM_BUILD_ROOT}%{_datadir}/applications/
install -p -m 644 res/inochi-session.desktop ${RPM_BUILD_ROOT}%{_datadir}/applications/inochi-session.desktop
desktop-file-validate \
    ${RPM_BUILD_ROOT}%{_datadir}/applications/inochi-session.desktop

install -d ${RPM_BUILD_ROOT}%{_metainfodir}/
install -p -m 644 res/inochi-session.appdata.xml \
    ${RPM_BUILD_ROOT}%{_metainfodir}/inochi-session.appdata.xml
appstream-util validate-relax --nonet \
    ${RPM_BUILD_ROOT}%{_metainfodir}/inochi-session.appdata.xml

# Dependency licenses
install -d ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/./deps/bindbc-imgui/cimgui/
install -p -m 644 ./deps/bindbc-imgui/deps/cimgui/LICENSE \
    ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/./deps/bindbc-imgui/cimgui/LICENSE
install -d ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/./deps/bindbc-imgui/imgui/
install -p -m 644 ./deps/bindbc-imgui/deps/cimgui/imgui/LICENSE.txt \
    ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/./deps/bindbc-imgui/imgui/LICENSE.txt

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


%changelog
%autochangelog