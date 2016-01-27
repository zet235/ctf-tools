export PYTHONPATH="/root/ctf-tools"
alias aslr.on="sudo sysctl -w kernel.randomize_va_space=2"
alias aslr.off="sudo sysctl -w kernel.randomize_va_space=0"
