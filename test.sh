#!/bin/bash

dir=mozilla-tacotron-tagent-bn-July-30-2019_02+50PM-726e54a

test_data=(
	"Scientists at the CERN laboratory say they have discovered a new particle." 
	"There's a way to measure the acute emotional intelligence
	that has never gone out of style."
	"President Trump met with other leaders at the Group of 20 conference."
	"Generative adversarial network or variational auto-encoder."	
	"Please call Stella."
	"Some have accepted this as a miracle without any physical explanation."
)

rm keep/$dir/test_audios/*.wav

for item in "${test_data[@]}"
do
	echo $item
	python synthesize.py "$item" config_tacotron_ljspeech.json keep/$dir/best_model.pth.tar keep/$dir/test_audios/
done

