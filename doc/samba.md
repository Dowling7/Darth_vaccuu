# Remote access via samba
Author: Dwong 
Laste edited: Feb 10, 2025  
Initialized: Feb 10, 2025  
- **Linux server side:** 
  - On the server side machine:
  ```bash
  sudo apt update
  sudo apt install samba
  ```

  ```bash
  sudo mkdir -p /srv/samba/shared
  ```
  Adjust permissions: Ensure the folder has appropriate permissions for the users who will access it:
  ```bash
  sudo chown -R nobody:nogroup /srv/samba/shared
  sudo chmod -R 0777 /srv/samba/shared
  ```
  
  ```bash
  sudo nano /etc/samba/smb.conf

  [SharedFolder]
  path = /srv/samba/shared
  browseable = yes
  writable = yes
  guest ok = yes
  read only = no

  ```
  Make sure Samba (smbd and nmbd) is enabled at boot and running:
  ```bash
  sudo systemctl enable smb nmb
  sudo systemctl start smb nmb
  ```
  Open the firwalls: Samba typically uses TCP ports 139 and 445, and UDP ports 137 and 138. Port 22 usually is for ssh
  ```bash
  sudo ufw allow samba
  ```


- **Linux client side:** 
  ```bash
  sudo apt update
  sudo apt install cifs-utils

  ```
  ```bash
  sudo mkdir -p /mnt/windows_share

  ```
  ```bash
  sudo mount -t cifs -o credentials=/etc/samba/keyence  //192.168.13.89/IMSeriesShared /mnt/win_share
  ls /mnt/win_share/
  sudo umount /mnt/win_share/
  EDITOR=vim sudoedit /etc/fstab 
  sudo mount /mnt/win_share/ 
  ```
  find the correcsponding local mounting point entry. edit fstab. systemctl daemon-reload only change what systemctl has read, not really do the operation of mounting. 
  ```
  ```bash
  sudo ufw allow samba
  ```


## Tips
 - TCP port 22 is the default port used by SSH (Secure Shell)
 - dmesg displays the messages from the kernel’s ring buffer. The kernel ring buffer is an in-memory log where the Linux kernel writes messages about hardware, drivers, and other low-level system components.
  - cat to view text file
  - Text file in linux doesn't need an extension
  - EDITOR=vim sudoedit /etc/fstab 
  - crontab: time-based job scheduler
  ```bash
    MINUTE  HOUR  DAY_OF_MONTH  MONTH  DAY_OF_WEEK  COMMAND
    MINUTE: 0–59
    HOUR: 0–23
    DAY_OF_MONTH: 1–31
    MONTH: 1–12 (or short names like jan, feb, …)
    DAY_OF_WEEK: 0–7 (where 0 or 7 is Sunday, or short names sun, mon, etc.)
    COMMAND: The actual command/script you want to run
  ```


## /etc/fstab 
- [ ] **Main Goal:** *(The most important thing to achieve today)*
- [ ] **Secondary Goals:**  
  - [ ]  
  
## /etc/crontab, and rountinely update

```bash
#!/bin/bash
##############################################################
       qdir=/media/win_share/
       subdir=data/
  sicherdir=/ddweb/daten/cmsprobex/
#######################################################
#folgende Datei sollte auf dem Share vorhanden sein:
fil=$qdir'nicht_loeschen.txt'
if [ -e "$fil" ]; then
    echo 'das NT-Sever-Laufwerk ist gemountet'
else
    echo 'das netzlaufwerk wird gemounted'
    mount.cifs //192.168.13.186/probe_new $qdir -o vers=3.0,credentials=/etc/samba/zumprobemounten
    sleep 5s
#
    if [ -e "$fil" ]; then
       echo 'jetzt ist das Probe-Laufwerk gemountet'
       mountzbv=1
    else
       echo 'das netzlaufwerk liess sich nicht mounten'
       exit 1
    fi
fi
#######################################################
logdir=$sicherdir
logfile=cmsprobe2sicherung.log
datt=`date`
echo "Beginn des Kopierens "$datt >> $logdir$logfile
##
cp -pruv  $qdir   $sicherdir   >> $logdir$logfile
##
datt=`date`
echo "Ende des Kopierens "$datt >> $logdir$logfile
if [ "$mountzbv" = "1" ]; then
    echo die Platte war voher nicht gemounted
    umount $qdir
fi
##
exit 0

```

```bash
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin:opt/bin
#MAILTO=root

# For details see man 4 crontabs

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed

################################################################################################
# ------------------- Sicherung der Probe-Daten Mo,Di,Mi,Do,Fr um 21:07 -------------------
07 21 * * 1,2,3,4,5 root sh /ddweb/verwaltung/sicherungen/production/cmsprobe1sicherung.com
27 21 * * 1,2,3,4,5 root sh /ddweb/verwaltung/sicherungen/production/cmsprobe2sicherung.com
#
# prüft den Raid-Status dreimal wöchentlich:
18  21  *  *  2,4,7  root sh /root/pruefplatten02.com
#
```