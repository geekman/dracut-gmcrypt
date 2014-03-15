#!/bin/sh

. /lib/dracut-gmcrypt-lib.sh

LUKS=$(getargs rd_LUKS_UUID=)

if ! getarg rd_NO_LUKS && [ -n "$LUKS" ] ; then
    gmcrypt_genkey /tmp/rootfs.key $LUKS
fi

