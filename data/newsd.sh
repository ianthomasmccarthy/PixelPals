#!/bin/bash

INTERFACES_PATH='/opt/pixelpals/data/interfaces'

case "$1" in

	'megaman')  PIXEL_PAL='Megaman'
				NETWORK=12
		;;

    'vaultboy') PIXEL_PAL='VaultBoy'
                NETWORK=13
        ;;

    'smb3firemario') PIXEL_PAL='smb3FireMario'
                     NETWORK=15
        ;;

	'smbmario')    PIXEL_PAL='smbMario'
                   NETWORK=19
        ;;

    'smbluigi')     PIXEL_PAL='smbLuigi'
                    NETWORK=20
        ;;

    'batman')       PIXEL_PAL='Batman'
                    NETWORK=23
        ;;

    'joker')        PIXEL_PAL='TheJoker'
                    NETWORK=24
        ;;

    'harleyquinn')  PIXEL_PAL='HarleyQuinn'
                    NETWORK=25
        ;;

    'akuma')        PIXEL_PAL='SFAkuma'
                    NETWORK=27
        ;;

    'smwmario')     PIXEL_PAL='smwMario'
                    NETWORK=30
        ;;

	'smb3tanookimario') PIXEL_PAL='smb3TanookiMario'
                        NETWORK=34
		;;
    *) echo "Please enter a name"
        exit 1
        ;;

esac

cp ${INTERFACES_PATH} ${INTERFACES_PATH}1
sed -i "s/PIXEL_IP/$NETWORK/" ${INTERFACES_PATH}1
mv /opt/pixelpals/data/interfaces1 /etc/network/interfaces
sed -i "s/raspberrypi/$PIXEL_PAL/" /etc/hostname
sed -i "s/raspberrypi/$PIXEL_PAL/" /etc/hosts
