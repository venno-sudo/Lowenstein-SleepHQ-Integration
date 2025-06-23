#!/bin/bash
if grep -qs '/media/USER/Weinmann ' /proc/mounts; then
    cd /home/USER/prisma/scripts
    /home/USER/prisma/mypython/bin/python3 transfer_data.py
    /home/USER/prisma/mypython/bin/python3 prisma20a_sleephq_uploader.py
    umount /dev/sda
    sudo ykushcmd ykushxs -d
    ./nas_sync.sh
else
    echo "It's not mounted."
fi
