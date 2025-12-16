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
    
    play_piano("A4", 0.5)     # standard A4
    play_piano("A5", 0.5)     # one octave higher
    play_piano("C4", 1.5)
    wait(0.5)
    play_piano("G#6", 0.25)
    
    piano = end_recording()
    
    # Bass part
    start_recording()
    play_piano("A2", 4.0)
    bass = end_recording()
    
    # Guitar part
    start_recording()
    play_guitar("A4", 1.0)
    play_guitar("C5", 1.0)
    play_guitar("E5", 1.0)
    play_guitar("A4", 1.0)
    guitar = end_recording()
    
    # Flute part
    start_recording()
    play_flute("A5", 0.5)
    play_flute("C6", 0.5)
    play_flute("E6", 1.0)
    flute = end_recording()
    
    # Synth part
    start_recording()
    play_synth("A4", 0.5)
    play_lead_synth("C5", 0.5)
    play_bass_synth("A2", 2.0)
    synth = end_recording()
    
    # Drums
    start_recording()
    play_drum("kick", 0.5)
    play_drum("snare", 0.5)
    play_drum("hihat", 0.5)
    play_drum("snare", 0.5)
    drums = end_recording()
    
    # Play all together
    play_recordings([piano, bass, guitar, flute, synth, drums])
