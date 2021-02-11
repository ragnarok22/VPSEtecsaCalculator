apt-get install dh-virtualenv devscripts
mkdir "debian"
touch debian/control

PACKAGE_NAME="VPSEtecsaCalculator"
VERSION="0.1"
MAINTAINER="Reinier Hernández"
MAINTAINER_EMAIL="sasuke.reinier@gmail.com"

cat > debian/control <<EOL
Source: $PACKAGE_NAME
Section: python3
Priority: extra
Maintainer: $MAINTAINER <$MAINTAINER_EMAIL>
Build-Depends: debhelper (>= 9), python3.8, dh-virtualenv (>= 0.8)
Standards-Version: $VERSION

Package: $PACKAGE_NAME
Architecture: any
Pre-Depends: dpkg (>= 1.16.1), python3.8, \${misc:Pre-Depends}
Depends: \${misc:Depends}
Description: Calculadora de los precios de los VPS de Etecsa
EOL

touch debian/compat
echo "9" > debian/compat
dch --create
cp requirements.txt requirements.in

pip-compile requirements.in > requirements.txt

touch debian/rules
cat > debian/rules <<EOL
#!/usr/bin/make -f

%:
        dh $@ --with python-virtualenv --python /usr/bin/python3.8
EOL

debuild -b -us -uc
