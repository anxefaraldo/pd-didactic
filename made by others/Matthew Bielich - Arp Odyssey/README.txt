FINAL PROJECT FOR MUSIC 171, WI05
Author: Matthew Bielich
Date: 3-17-05


~~ ABOUT THE PROJECT ~~

I have modelled the ARP Odyssey for my final project.  All sliders may
be controlled via various MIDI controllers if setup on the MIDI device
(controllers 1-34, 7 for VCA gain, 64 for pedal input).  Notes can be
played using a MIDI device keyboard and pitchbend as well.  All features
are fully functional, including the sample and hold circuit, pink noise,
and sync which were optional.

Extra credit: as will be described in more detail below, I also included
a looping step sequencer along with three sample sequence presets.


~~ RUNNING THE ARP ODYSSEY ~~

Open ARPodyssey.pd in Pd.  Audio will be turned on but the MIDI device
will not be connected by default.  Make sure to connect a MIDI device
before using the patch.

REQUIRED FILES:
ARPodyssey.pd requires that mcs.pd (a midi control scale tool) and
sequencer.pd (a simple interface for the sequencer) be in the same level
directory.  pinknoise.wav must also be located in the same level
directory to use sampled pink-noise.  The "patches" subfolder contains
.ody patch files which hold the settings needed to obtain different
sounds or instruments.  In order to save preset files this project needs
to be copied to the computer instead of being run off of a CD (as data
cannot be saved/written to the CD).

To begin using the synthesizer, simply set controls to the desired
positions and play notes using either the provided simple 1-note keyboard
on screen or any MIDI device via MIDI note messages.  When using a MIDI
keyboard, the Odyssey will function as the original analog synthesizer
would, complete with duophonic (2-note) capabilities.

To test the portamento feature you must be holding down the foot pedal
and have the pedal setup as a portamento pedal.  This follows the
specifications of the ARP manual.  While there can be two pedals, this
model allows for one pedal to be selected for use with either portamento
or the modulation controller.  A real pedal would allow for values other
than on or off, but this was the best I could simulate.  If no pedal is
available, one can be simulated using the large toggle labelled pedal.

Notice some user controls in the lower left corner of the ARP Odyssey,
to the left of the model keyboard.  There are a few useful subpatches to
know about in the ARPodyssey.pd project:
    * [pd patches] contains samples of patches as were listed in the back
        of the manual.  This panel also allows the user to store and recall
        up to 5 preset files to experiment with making your own patches.
    * [pd tools] contains simple tools for the user: level of CPU load, an
        overload warning for when the output of the Odyssey clips, a scope
        for viewing the output waveform, and a looping step sequencer
        * [pd sequencer] contains all the patchwork used to make the looping
            step sequencer.  The sequencer is monophonic and can take twelve
            notes each with its own duration.  Note that setting a note to
            zero (or lower) is read by the sequencer to be a puase/rest/delay
            before the next note in sequence.  A few sample sequences are
            provided and can be set using the buttons on the Tools panel, or
            the sequence can be altered by hand by opening this sequencer
            subpatch and changing the notes and durations each step at a time.
    * [pd guts] contains all the patchwork for the ARP Odyssey.  It is
        organized like page 9 in the manual where each piece of the synthesizer
        is a subpatch with inlets and outlets.


~~ NOTES ~~
* throws and catches were used for the sample and hold mixer because Pd would
  see it as a loop otherwise, causing an overflow.
* in the Tools panel you can select between a 2-pole VCF (which matches the
  white-faced Odyssey I modelled) or a 4-pole VCF (which was used in the
  second and third generation Odysseys).  2 poles work fine for most patches.
* I used the right outlet of the vcf~ object, which is sort of a low pass
  filter.  It is unfortunately not perfect, so there are times where no sound
  can be heard simply because lower frequencies are not being passed.  Also,
  there is a VCF gain compensate slider to amplify the sound lost due to the
  VCF.  Also, the vcf~ object is not the same as the Odyssey's filter in all
  respects, such as how turning the resonance all the way up does not create
  self oscillation in the filter like it would in the analog Odyssey.
* making pink noise with a lop~ filter didn't sound quite right so I used
  sampled pink noise instead.
* I noticed some latency between the MIDI device and Pd - it's best to turn
  off local sound on the keyboard.
* pitch bending with the wheel is supposed to go to +- an octave, but this
  happened too quickly with even a small bend, so I adjusted it to be an
  exponential (power of 2) curve instead.  Now small bends are like normal
  pitch bending but larger turns of the wheel allow for full octave bending.
* in the Patches panel, the Reset bang sets everything back to basic raw
  waves and basic settings.  Simply turn up the mixer on VCO 1 or 2 and
  hit a note.
* I am including a sheet with all the control names and ranges listed on it
  for reference.  All controls send wireless values as "controlname" and
  are initialized as "init_controlname".  the mcs.pd file scales midi
  controllers to the appropriate range for each control.