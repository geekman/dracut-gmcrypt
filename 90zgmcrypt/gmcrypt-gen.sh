#!/bin/sh

. /lib/dracut-gmcrypt-lib.sh

NO_LUKS=0
LUKS=$(getargs rd_LUKS_UUID=)
getarg rd_NO_LUKS && NO_LUKS=1

# dracut >= 033
if type getargbool >/dev/null 2>&1; then
    LUKS=$(getargs rd.luks.uuid -d rd_LUKS_UUID)
    getargbool 1 rd.luks -d -n rd_NO_LUKS || NO_LUKS=1
fi

if [ $NO_LUKS -eq 0 ] && [ -n "$LUKS" ] ; then
    gmcrypt_genkey /tmp/rootfs.key $LUKS
fi

