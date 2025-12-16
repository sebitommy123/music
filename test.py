from wrapper import (
    start_recording, play_piano, play_guitar, play_flute,
    play_synth, play_bass_synth, play_lead_synth, play_drum,
    play_electric_piano, play_pad_synth, play_bass, play_electric_bass,
    play_fretless_bass, play_trumpet, play_trombone, play_horn,
    play_saxophone, play_clarinet, play_oboe, play_violin, play_viola,
    play_cello, play_harp, play_organ, play_harpsichord, play_celesta,
    play_glockenspiel, play_banjo, play_harmonica, play_accordion,
    wait, end_recording, play_recordings
)

# Example usage:
if __name__ == "__main__":
    start_recording()
    
    # These all play simultaneously at the same time
    play_synth("A4", 0.5)     # standard A4
    play_synth("A5", 0.5)     # one octave higher
    play_synth("C4", 1.5)
    
    # Wait moves time forward
    wait(0.5)
    
    # This plays after the wait
    play_synth("G#6", 0.25)
    
    piano = end_recording()
    
    # Play all together
    play_recordings([piano])
