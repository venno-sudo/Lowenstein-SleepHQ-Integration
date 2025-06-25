#!/bin/bash
sleep 10
if grep -qs '/media/USER/Weinmann ' /proc/mounts; then
    file_today="/media/USER/Weinmann/therapy.pdat"
    file_prev="/home/USER/prisma/data/therapy.pdat"
	if [[ ! -f "$file_prev" || "$file_today" -nt "$file_prev" ]]; then
		cd /home/USER/prisma/scripts
		/home/USER/prisma/mypython/bin/python3 /home/USER/prisma/scripts/transfer_data.py
		/home/USER/prisma/mypython/bin/python3 /home/USER/prisma/scripts/prisma20a_sleephq_uploader.py
		./nas_sync.sh
	fi
	sleep 1
    umount /dev/sda
	sleep 1
    sudo ykushcmd ykushxs -d
else
    echo "It's not mounted."
fi