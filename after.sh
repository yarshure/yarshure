echo 'zfs_enable="YES"' >> /mnt/etc/rc.conf
echo 'zfs_load="YES"' >> /mnt/boot/loader.conf
echo 'vfs.root.mountfrom="zfs:zroot"' >> /mnt/boot/loader.conf
zfs unmount -a
zpool export zroot
zpool import -o cachefile=/tmp/zpool.cache -o altroot=/mnt zroot
 
zfs set mountpoint=/ zroot
cp /tmp/zpool.cache /mnt/boot/zfs/
zfs unmount -a
zpool set bootfs=zroot zroot
zpool set cachefile='' zroot
zfs set mountpoint=legacy zroot
zfs set mountpoint=/tmp zroot/tmp
zfs set mountpoint=/usr zroot/usr
zfs set mountpoint=/var zroot/var
zfs set mountpoint=/home zroot/home
