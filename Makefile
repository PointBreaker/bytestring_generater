# Define variables
HEADER_FILE = HEADER

# Rule to generate the ASM file based on the input file name
%.asm: %.s
	sed 's/^/\t/' $< > $<.temp
	cat $(HEADER_FILE) $<.temp > $@
	rm $<.temp

%.out: %.asm
	as $< -o $@

%.bin: %.out
	objcopy -O binary --only-section=.text $< $@

%.view: %.bin
	echo "The string literal is:"
	python binary2hex.py $<

rm:
	rm *.o *.asm *.temp, *.out *.bin