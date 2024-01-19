## Generate bytes string literals from assembly

This is a simple program that generates bytes from assembly code. It is intended to be used as a library, but it can also be used as a standalone program.

### Usage

write a file with assembly code, for example `test.asm`:

```asm
mov eax, 0x1337
```

then run the makefile:

```bash
make test.view
```

this will output the bytes to stdout:

```bash
\x48\xc7\xc7\x37\x13\x00\x00
```

which can be used to create a shellcode:


