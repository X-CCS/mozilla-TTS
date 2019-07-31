#!/bin/bash

dir=mozilla-tacotron-tagent-bn-July-30-2019_02+50PM-726e54a

test_data=(
	"Today is a rainy day." 
	"Welcome to the League of Legends." 
)

rm keep/$dir/test_audios/*.wav

for item in "${test_data[@]}"
do
	echo $item
	python synthesize.py "$item" config_tacotron_ljspeech.json keep/$dir/best_model.pth.tar keep/$dir/test_audios/
done

