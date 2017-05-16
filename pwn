export CTFTOOLS=$(cd "$(dirname $0)"; pwd)
export PATH=$PATH:$CTFTOOLS/bin
export PYTHONPATH=$CTFTOOLS/pylib

#alias
alias gdb="gdb -q"
alias gdb-peda="gdb -x $CTFTOOLS/peda/peda.py"
alias gdb-heap="gdb -x $CTFTOOLS/pylib/libheap.py"
alias objdump="objdump -M intel"
alias lddd="LD_TRACE_LOADED_OBJECTS=1"

function aslr()
{
    if [ -z $1 ]; then
        cat /proc/sys/kernel/randomize_va_space
    elif [ $1 = "on" ]; then
        sudo sysctl -w kernel.randomize_va_space=2
    elif [ $1 = "off" ]; then
        sudo sysctl -w kernel.randomize_va_space=0
    fi
}

function ndog()
{
    if [ $1 = "-h" ]; then
        echo " -l ltrace \n -s strace \n -g gdb"
    elif [ $1 = "-l" ]; then
        ncat -vc 'ltrace -ix $2' -kl 127.0.0.1 4000
    elif [ $1 = "-s" ]; then
        ncat -vc 'strace -ix $2' -kl 127.0.0.1 4000
    elif [ $1 = "-g" ]; then
        echo "type [ target remote 127.0.0.1:4444 ] ing db"
        ncat -vc 'gdbserver 127.0.0.1:4444 $2' -l 127.0.0.1 4000
    else
        if [ -f "$1" ]; then
            ncat -vc $1 -kl 127.0.0.1 4000
        else
            echo "[x] file not fuond"
        fi
    fi
}

function libc()
{
    libc_system=$(readelf -s "$1" | grep " system@" | awk '{print $2}')
    libc_execve=$(readelf -s "$1" | grep " execve@" | awk '{print $2}')
    libc_sh=$(strings -tx "$1" | grep "/bin/sh" | awk '{print $1}')
    echo "libc_system = libc_base + 0x$libc_system"
    echo "libc_execve= libc_base + 0x$libc_execve"
    echo "libc_sh = libc_base + 0x$libc_sh"
}

function heap()
{
    ltrace $1 |& python3 $CTFTOOLS/villoc/villoc.py - /usr/share/nginx/html/$1.html
}

function maps()
{
    cat /proc/$1/maps
}
