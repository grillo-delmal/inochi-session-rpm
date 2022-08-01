#!/bin/sh

set -e
set -x

TAGVER="$(sed -n 's/%define inochi_session_ver\s*//p' *.spec)"
DIST="$(sed -n 's/%define inochi_session_dist\s*//p' *.spec)"
COMMIT="$(sed -n 's/%define inochi_session_commit\s*//p' *.spec)"
SHORT="$(sed -n 's/%define inochi_session_short\s*//p' *.spec)"
VERSION=${TAGVER}$([ ${DIST} -gt 0 ] && echo "^${DIST}.git${SHORT}" || echo "")

# Retrieve and set version
curl -L https://github.com/Inochi2D/inochi-session/archive/${COMMIT}/inochi-session-${SHORT}.tar.gz --output inochi-session-${SHORT}.tar.gz
tar -xzf inochi-session-${SHORT}.tar.gz

pushd inochi-session-${COMMIT}

# Remove restricted assets
rm res/tex/ada.png
rm res/tex/logo.png
rm res/icon_x256.png
rm res/icon.ico
rm res/inochi-session.rc

popd

tar -czf inochi-session-$VERSION-norestricted.tar.gz inochi-session-${COMMIT}
rm -rf inochi-session-${COMMIT}
rm -rf inochi-session-${SHORT}.tar.gz

