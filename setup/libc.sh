#!/bin/bash
mkdir -p $HOME/glibc-$1
cd $HOME/glibc-$1
wget "http://ftp.gnu.org/gnu/glibc/glibc-$1.tar.gz"
tar xvf "glibc-$1.tar.gz"

mkdir -p "$HOME/glibc-$1/build/64"
cd       "$HOME/glibc-$1/build/64"
CFLAGS="-g -g3 -ggdb -gdwarf-4 -Og -Wno-error=maybe-uninitialized" \
    CXXFLAGS="-g -g3 -ggdb -gdwarf-4 -Og -Wno-error=maybe-uninitialized" \
    "$HOME/glibc-$1/glibc-$1/configure" --prefix="$HOME/glibc-$1/64"
make -j 5


mkdir -p "$HOME/glibc-$1/build/32"
cd       "$HOME/glibc-$1/build/32"
CC="gcc -m32" CXX="g++ -m32" \
    CFLAGS="-g -g3 -ggdb -gdwarf-4 -Og -Wno-error=maybe-uninitialized" \
    CXXFLAGS="-g -g3 -ggdb -gdwarf-4 -Og -Wno-error=maybe-uninitialized" \
    "$HOME/glibc-$1/glibc-$1/configure" --prefi="$HOME/glibc-$1/32" \
    --host=i686-linux-gnu 
make -j5
