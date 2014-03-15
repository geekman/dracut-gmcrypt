# 
# function to generate the system key
#

gmcrypt_genkey() {
    KEYFILE=$1
	UUID=$2
    [ -z "$KEYFILE" -o -z "$UUID" ] && return 1

	> "$KEYFILE"
	for dmivar in bios-{vendor,version,release-date} \
		baseboard-{manufacturer,product-name,version,serial-number}  \
		chassis-asset-tag processor-{manufacturer,version} ; 
	do dmidecode -s $dmivar >> "$KEYFILE"; done
	echo "$UUID" >> "$KEYFILE"

    unset KEYFILE UUID
}

