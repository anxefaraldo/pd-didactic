"""
Use GS-API to extract Pitch values from MIDI sequence.
The output is written to a .txt file (copy the output and paste it in Pd)
"""
import gsapi
import sys

if (len(sys.argv) == 1):
	print "Missing argument with midi file name"

else:	
	out = open("melodyPC.txt", "w")

	midifile = str(sys.argv[1])

	pattern = gsapi.GSIO.fromMidi(midifile, "pitchNames")

	print pattern

	pc = []

	for event in pattern.events:
		pc.append(event.pitch)
		out.write(str(event.pitch) + " ")

	print pc	

	
	#out.write(str(pc)[1:-1])
	out.close()