## Levels and Leyers in a Linux System:
2. User process: GUI, Servers, Shell, etc
1. Linux Kernel: System Calls, Process Management, Memory Management, Device Drivers
0. Hardware: CPU, RAM, Disks, Network Ports

The Kernel's tasks is to split memory inti many subdivisions. The kernel is in charge of managing tasks in four general system areas:
- Process
- Memory
- Device drivers
- System Calls

System Calls (alson known as __Syscalls__) is an interaction between a process and the kernel.
the main memory that the kernel allocates for user processes is called __user space__.
A __user__ is an entity that can run processes and own files.