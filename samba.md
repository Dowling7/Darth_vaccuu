# Mounting a windows folder on Linux machine, and routinely update

## Mounting a windows directory via samba
- **Mood:** 😀😐😞
- **Sleep Quality:** 💤💤💤 (Rate: 1-5)
- **Dreams:** *(Any memorable dreams?)*  
- **Gratitude List:**  
  - 1.  
  - 2.  
  - 3.  

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