dracut-gmcrypt
================
Dracut module to provide passwordless decryption for LUKS-encrypted root
volumes.  This module in itself does not provide any LUKS decryption mechanism
but relies on the `crypt` module already distributed with dracut.  It works by
overwriting `/etc/crypttab` with a version that specifies a key file in `/tmp`
which is generated at boot.  This key is derived from system board information
using `dmidecode`.

**What happens if I change my hardware?**
When you change your motherboard or upgrade your BIOS, the crypt module will be
unable to unlock the volume with the keyfile and fall back to prompting for a
password in another key slot (typically #0 created by the installer).

**This is dumb - what's the use of this?**
It's used to protect the root device should you need to send it in for servicing 
and it cannot be wiped effectively or in a timely manner. It's similar to using
an external USB device that contains the key, but slightly less secure as parts 
of the keyfile can be guessed. This removes the need for another USB key, or the 
reliance on a hardware TPM module.


Initial Setup
---------------
Install the system as you would, and opt to encrypt the root partition.

Run the `add-key.sh` script on the system:

    /usr/share/dracut/modules.d/90zgmcrypt/add-key.sh <luks-device>

If you upgrade your system and it no longer automatically unlocks, just run
this script again. It assumes the system-generated key resides in slot #1 and
will prompt you to remove it on each run.


Installation
--------------
This module was designed for CentOS/RHEL systems, so it's built as an RPM.

You can build the RPM from the `tar.gz` file:

    rpmbuild -tb dracut-gmcrypt.tar.gz


License
--------
Copyright (C) 2014 Darell Tan

This module follows the same license as dracut, which is GPLv2.
Some parts of the scripts are clearly copied from dracut.

