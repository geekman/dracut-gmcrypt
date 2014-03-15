#!/bin/bash
# 
# generates the system key and adds it into the specified LUKS volume
# this needs to be run on the SAME system that is used to generate the key!
#
#   usage: add-key.sh <dev>
#

DEV=$1

if [ -z "$DEV" -o ! -b "$DEV" ]; then
    echo "usage: `basename $0` <luks-dev>"
    exit 1
fi

# include the lib
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source $SCRIPT_DIR/gmcrypt-lib.sh

if ! cryptsetup isLuks "$DEV" 2>/dev/null; then
    echo "$DEV is not a LUKS device"
    exit 1
fi

DEV_UUID=luks-$(cryptsetup luksUUID "$DEV")

if [ ${#DEV_UUID} -lt 10 ]; then
    echo "cryptsetup returned UUID is too short: $DEV_UUID"
    exit 1
fi

TMPFILE=$(mktemp -q /tmp/keyfile.rootfs.XXXXXXXXXX) || exit 1
trap "rm -f $TMPFILE" EXIT

#
# show user key slots and ask if we should remove slot 1
#
echo
cryptsetup luksDump $DEV | grep -i "slot\|header"

read -p "Should I remove key from slot 1? " removeKey
case $removeKey in
    [Yy])
        echo "Wiping key slot #1..."
        cryptsetup luksKillSlot $DEV 1
        ;;
esac

#
# generate and add key
#
echo 
echo "Generating key and adding it to ${DEV}..."

gmcrypt_genkey "$TMPFILE" "$DEV_UUID" &&
    cryptsetup luksAddKey "$DEV" "$TMPFILE" 

echo "Done."

