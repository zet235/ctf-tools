export PATH=$PATH:$(cd "$(dirname $0)"; pwd)
export PYTHONPATH=$(cd "$(dirname $0)"; pwd)

#alias
alias aslr.on="sudo sysctl -w kernel.randomize_va_space=2"
alias aslr.off="sudo sysctl -w kernel.randomize_va_space=0"
alias gdb="gdb -q"
alias objdump="objdump -M intel"
