#! /bin/sh

mock -r fedora-19-i386 --resultdir=./granite-0.2.3.1-1.fc19.i386 granite-0.2.3.1-1.fc20.src.rpm
mock -r fedora-19-x86_64 --resultdir=./granite-0.2.3.1-1.fc19.x86_64 granite-0.2.3.1-1.fc20.src.rpm

mock -r fedora-20-i386 --resultdir=./granite-0.2.3.1-1.fc20.i386 granite-0.2.3.1-1.fc20.src.rpm
mock -r fedora-20-x86_64 --resultdir=./granite-0.2.3.1-1.fc20.x86_64 granite-0.2.3.1-1.fc20.src.rpm

mock -r fedora-rawhide-i386 --resultdir=./granite-0.2.3.1-1.fc21.rawhide.i386 granite-0.2.3.1-1.fc20.src.rpm
mock -r fedora-rawhide-x86_64 --resultdir=./granite-0.2.3.1-1.fc21.rawhide.x86_64 granite-0.2.3.1-1.fc20.src.rpm
