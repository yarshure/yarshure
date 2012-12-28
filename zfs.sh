gpart create -s gpt ada1
gpart add -s 64K -t freebsd-boot -l boot0 ada1
gpart add -s 8G -t freebsd-swap -l swap0 ada1
gpart add -t freebsd-zfs -l disk0 ada1
gpart bootcode -b /boot/pmbr -p /boot/gptzfsboot -i 1 ada1


zpool create -o altroot=/mnt zroot mirror /dev/gpt/disk0 

zpool create -o altroot=/mnt zroot /dev/gpt/disk0

zfs create zroot/tmp
chmod 1777 /mnt/tmp
zfs create zroot/usr
zfs create zroot/var
zfs create zroot/home
