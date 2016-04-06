export CTFTOOLS=$(cd "$(dirname $0)"; pwd)
export PATH=$PATH:$CTFTOOLS/bin
export PYTHONPATH=$CTFTOOLS/pylib

#alias
alias aslr.on="sudo sysctl -w kernel.randomize_va_space=2"
alias aslr.off="sudo sysctl -w kernel.randomize_va_space=0"
alias gdb="gdb -q"
alias objdump="objdump -M intel"
function heap()
{
    ltrace $1 |& python3 $CTFTOOLS/villoc/villoc.py - /usr/share/nginx/html/$1.html
}

function maps()
{
    cat /proc/$1/maps
}
