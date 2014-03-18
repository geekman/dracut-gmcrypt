# 
# function to generate the system key
#

gmcrypt_genkey() {
    KEYFILE=$1
    UUID=$2
    [ -z "$KEYFILE" -o -z "$UUID" ] && return 1

    > "$KEYFILE"
    for dmivar in bios-vendor bios-version bios-release-date \
                    baseboard-manufacturer baseboard-product-name \
                    baseboard-version baseboard-serial-number \
                    chassis-asset-tag processor-manufacturer processor-version ; 
        do dmidecode -s $dmivar >> "$KEYFILE"
    done
    echo "$UUID" >> "$KEYFILE"

    unset KEYFILE UUID
}

