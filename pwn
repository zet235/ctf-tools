export CTFTOOLS=$(cd "$(dirname $0)"; pwd)
export PATH=$PATH:$CTFTOOLS/bin
export PYTHONPATH=$CTFTOOLS/pylib

#alias
alias gdb="gdb -q"
alias gdb-peda="gdb -x $CTFTOOLS/peda/peda.py"
alias gdb-heap="gdb -x $CTFTOOLS/pylib/libheap.py"
alias objdump="objdump -M intel"
alias lddd="LD_TRACE_LOADED_OBJECTS=1"
alias rop="ROPgadget --binary"


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


function libc()
{
    libc_system=$(readelf -s "$1" | grep " system@" | awk '{print $2}')
    libc_execve=$(readelf -s "$1" | grep " execve@" | awk '{print $2}')
    libc_sh=$(strings -tx "$1" | grep "/bin/sh" | awk '{print $1}')
    echo "libc_system = libc_base + 0x$libc_system"
    echo "libc_execve= libc_base + 0x$libc_execve"
    echo "libc_sh = libc_base + 0x$libc_sh"
}

syscall()
{
    grep --color -m 1 "$1" /usr/include/asm/unistd.h /usr/include/asm/unistd_32.h /usr/include/asm/unistd_64.h 2>/dev/null
}

function heap()
{
    ltrace $1 |& python3 $CTFTOOLS/villoc/villoc.py - /usr/share/nginx/html/$1.html
}

function maps()
{
    cat /proc/$1/maps
}
