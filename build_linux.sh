#!/bin/bash

PACKAGE_NAME="VPSEtecsaCalculator"
VERSION="1.0"
MAINTAINER="Reinier Hernández"
MAINTAINER_EMAIL="sasuke.reinier@gmail.com"

FOLDER=${PACKAGE_NAME}_${VERSION}-debian

# Creando las carpetas necesarias
mkdir $FOLDER
mkdir $FOLDER/DEBIAN
mkdir $FOLDER/usr
mkdir $FOLDER/usr/local
mkdir $FOLDER/usr/local/bin
mkdir $FOLDER/usr/share
mkdir $FOLDER/usr/share/applications

# Creando archivos necesarios
touch $FOLDER/DEBIAN/control
touch $FOLDER/usr/share/applications/$PACKAGE_NAME.desktop

cat >$FOLDER/DEBIAN/control <<EOL
Package: ${PACKAGE_NAME}
Version: ${VERSION}
Section: python3
Priority: extra
Architecture: any
Maintainer: ${MAINTAINER} <${MAINTAINER_EMAIL}>
Description: Calculadora de los precios de los VPS de Etecsa
EOL
cat $FOLDER/DEBIAN/control

cat >$FOLDER/usr/share/applications/$PACKAGE_NAME.desktop <<EOL
[Desktop Entry]
Version: ${VERSION}
Type: Application
Name: ${PACKAGE_NAME}
GenericName: VPS Etecsa Calculator
Comment: Calculadora de los precios de los VPS de Etecsa
Exec=/usr/local/bin/${PACKAGE_NAME}
Terminal: false
Keywords:VPS;Etecsa;Calculator;${PACKAGE_NAME}
Categories=Productivity
StartupNotify=true
EOL
cat $FOLDER/usr/share/applications/$PACKAGE_NAME.desktop

# Generando ejecutable
pyinstaller main.py --name "${PACKAGE_NAME}" --noconsole --onefile
cp dist/$PACKAGE_NAME $FOLDER/usr/local/bin/

# compilando el paquete
dpkg-deb --build $FOLDER
