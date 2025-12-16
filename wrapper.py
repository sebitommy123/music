from music21 import stream, note, tempo, meter, instrument
from music21.note import Rest
import time

# Simple wrapper for music21
_current_stream = None
_current_offset = 0
_current_instrument = None

def start_recording(instrument_type=None):
    """Start a new recording stream with optional instrument"""
    global _current_stream, _current_offset, _current_instrument
    _current_stream = stream.Stream()
    _current_offset = 0
    # Store instrument for comparison - use midiProgram if available, otherwise the object itself
    if instrument_type:
        _current_stream.insert(0, instrument_type)
        if hasattr(instrument_type, 'midiProgram') and instrument_type.midiProgram is not None:
            _current_instrument = (instrument_type.midiProgram, getattr(instrument_type, 'instrumentName', ''))
        else:
            _current_instrument = instrument_type
    else:
        _current_instrument = None
    return _current_stream

def _add_note(note_with_octave, duration):
    """Internal helper to add a note to the current stream (doesn't advance offset)"""
    global _current_stream, _current_offset
    if _current_stream is None:
        start_recording()
    
    n = note.Note(note_with_octave)
    n.duration.quarterLength = duration
    n.offset = _current_offset  # Use current offset, but don't advance it
    _current_stream.insert(_current_offset, n)
    # Note: offset is NOT incremented here - only wait() advances it

def play_piano(note_with_octave, duration):
    """Play a piano note (e.g., 'A4', 'C#5', 'G#6')"""
    global _current_instrument
    piano_inst = instrument.Piano()
    if _current_stream is None or _current_instrument != piano_inst:
        start_recording(piano_inst)
    _add_note(note_with_octave, duration)

def play_guitar(note_with_octave, duration):
    """Play a guitar note (e.g., 'A4', 'C#5', 'G#6')"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.AcousticGuitar():
        start_recording(instrument.AcousticGuitar())
    _add_note(note_with_octave, duration)

def play_flute(note_with_octave, duration):
    """Play a flute note (e.g., 'A4', 'C#5', 'G#6')"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.Flute():
        start_recording(instrument.Flute())
    _add_note(note_with_octave, duration)

# Helper to create custom instrument with MIDI program number
def _create_synth_instrument(name, midi_program):
    """Create a custom synth instrument with specific MIDI program"""
    inst = instrument.Instrument()
    inst.midiProgram = midi_program
    inst.instrumentName = name
    return inst

# Real Electronic/Synth Instruments (using proper MIDI program numbers)
def play_synth(note_with_octave, duration):
    """Play a synthesizer note - Lead 1 (Sawtooth)"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Lead 1", 80)
    inst_id = (80, "Synth Lead 1")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

# Real Electronic/Synth Instruments (using proper MIDI program numbers)
def play_synth(note_with_octave, duration):
    """Play a synthesizer note - Lead 1 (Sawtooth)"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Lead 1", 80)
    inst_id = (80, "Synth Lead 1")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

def play_lead_synth(note_with_octave, duration):
    """Play a lead synthesizer - Lead 2 (Sawtooth)"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Lead 2", 81)
    inst_id = (81, "Synth Lead 2")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

def play_lead_synth_square(note_with_octave, duration):
    """Play a square wave lead synth - Lead 3 (Calliope)"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Lead 3", 82)
    inst_id = (82, "Synth Lead 3")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

def play_lead_synth_chiff(note_with_octave, duration):
    """Play a chiff lead synth - Lead 4 (Chiff)"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Lead 4", 83)
    inst_id = (83, "Synth Lead 4")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

def play_lead_synth_charang(note_with_octave, duration):
    """Play a charang lead synth - Lead 5 (Charang)"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Lead 5", 84)
    inst_id = (84, "Synth Lead 5")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

def play_lead_synth_voice(note_with_octave, duration):
    """Play a voice lead synth - Lead 6 (Voice)"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Lead 6", 85)
    inst_id = (85, "Synth Lead 6")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

def play_lead_synth_fifths(note_with_octave, duration):
    """Play a fifths lead synth - Lead 7 (Fifths)"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Lead 7", 86)
    inst_id = (86, "Synth Lead 7")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

def play_lead_synth_bass_lead(note_with_octave, duration):
    """Play a bass lead synth - Lead 8 (Bass + Lead)"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Lead 8", 87)
    inst_id = (87, "Synth Lead 8")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

def play_pad_synth(note_with_octave, duration):
    """Play a pad synthesizer - Pad 1 (New Age)"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Pad 1", 88)
    inst_id = (88, "Synth Pad 1")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

def play_pad_synth_warm(note_with_octave, duration):
    """Play a warm pad synth - Pad 2 (Warm)"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Pad 2", 89)
    inst_id = (89, "Synth Pad 2")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

def play_pad_synth_polysynth(note_with_octave, duration):
    """Play a polysynth pad - Pad 3 (Polysynth)"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Pad 3", 90)
    inst_id = (90, "Synth Pad 3")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

def play_pad_synth_choir(note_with_octave, duration):
    """Play a choir pad synth - Pad 4 (Choir)"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Pad 4", 91)
    inst_id = (91, "Synth Pad 4")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

def play_pad_synth_bowed(note_with_octave, duration):
    """Play a bowed pad synth - Pad 5 (Bowed)"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Pad 5", 92)
    inst_id = (92, "Synth Pad 5")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

def play_pad_synth_metallic(note_with_octave, duration):
    """Play a metallic pad synth - Pad 6 (Metallic)"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Pad 6", 93)
    inst_id = (93, "Synth Pad 6")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

def play_pad_synth_halo(note_with_octave, duration):
    """Play a halo pad synth - Pad 7 (Halo)"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Pad 7", 94)
    inst_id = (94, "Synth Pad 7")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

def play_pad_synth_sweep(note_with_octave, duration):
    """Play a sweep pad synth - Pad 8 (Sweep)"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Pad 8", 95)
    inst_id = (95, "Synth Pad 8")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

def play_bass_synth(note_with_octave, duration):
    """Play a bass synthesizer - Synth Bass 1"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Bass 1", 38)
    inst_id = (38, "Synth Bass 1")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

def play_bass_synth_2(note_with_octave, duration):
    """Play a bass synthesizer - Synth Bass 2"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Bass 2", 39)
    inst_id = (39, "Synth Bass 2")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

def play_synth_brass(note_with_octave, duration):
    """Play a synth brass - Synth Brass 1"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Brass 1", 62)
    inst_id = (62, "Synth Brass 1")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

def play_synth_brass_2(note_with_octave, duration):
    """Play a synth brass - Synth Brass 2"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Brass 2", 63)
    inst_id = (63, "Synth Brass 2")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

def play_synth_strings(note_with_octave, duration):
    """Play synth strings - Synth Strings 1"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Strings 1", 50)
    inst_id = (50, "Synth Strings 1")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

def play_synth_strings_2(note_with_octave, duration):
    """Play synth strings - Synth Strings 2"""
    global _current_instrument
    synth_inst = _create_synth_instrument("Synth Strings 2", 51)
    inst_id = (51, "Synth Strings 2")
    if _current_stream is None or _current_instrument != inst_id:
        start_recording(synth_inst)
    _add_note(note_with_octave, duration)

# Electronic/Synth Instruments (keeping electric piano)
def play_electric_piano(note_with_octave, duration):
    """Play an electric piano note"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.ElectricPiano():
        start_recording(instrument.ElectricPiano())
    _add_note(note_with_octave, duration)

def play_bass(note_with_octave, duration):
    """Play an acoustic bass note"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.AcousticBass():
        start_recording(instrument.AcousticBass())
    _add_note(note_with_octave, duration)

def play_electric_bass(note_with_octave, duration):
    """Play an electric bass note"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.ElectricBass():
        start_recording(instrument.ElectricBass())
    _add_note(note_with_octave, duration)

def play_fretless_bass(note_with_octave, duration):
    """Play a fretless bass note"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.FretlessBass():
        start_recording(instrument.FretlessBass())
    _add_note(note_with_octave, duration)

# Brass Instruments
def play_trumpet(note_with_octave, duration):
    """Play a trumpet note"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.Trumpet():
        start_recording(instrument.Trumpet())
    _add_note(note_with_octave, duration)

def play_trombone(note_with_octave, duration):
    """Play a trombone note"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.Trombone():
        start_recording(instrument.Trombone())
    _add_note(note_with_octave, duration)

def play_horn(note_with_octave, duration):
    """Play a French horn note"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.Horn():
        start_recording(instrument.Horn())
    _add_note(note_with_octave, duration)

# Woodwind Instruments
def play_saxophone(note_with_octave, duration):
    """Play a saxophone note (alto sax)"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.AltoSaxophone():
        start_recording(instrument.AltoSaxophone())
    _add_note(note_with_octave, duration)

def play_clarinet(note_with_octave, duration):
    """Play a clarinet note"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.Clarinet():
        start_recording(instrument.Clarinet())
    _add_note(note_with_octave, duration)

def play_oboe(note_with_octave, duration):
    """Play an oboe note"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.Oboe():
        start_recording(instrument.Oboe())
    _add_note(note_with_octave, duration)

# String Instruments
def play_violin(note_with_octave, duration):
    """Play a violin note"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.Violin():
        start_recording(instrument.Violin())
    _add_note(note_with_octave, duration)

def play_viola(note_with_octave, duration):
    """Play a viola note"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.Viola():
        start_recording(instrument.Viola())
    _add_note(note_with_octave, duration)

def play_cello(note_with_octave, duration):
    """Play a cello note"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.Cello():
        start_recording(instrument.Cello())
    _add_note(note_with_octave, duration)

def play_harp(note_with_octave, duration):
    """Play a harp note"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.Harp():
        start_recording(instrument.Harp())
    _add_note(note_with_octave, duration)

# Other Instruments
def play_organ(note_with_octave, duration):
    """Play an organ note"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.Organ():
        start_recording(instrument.Organ())
    _add_note(note_with_octave, duration)

def play_harpsichord(note_with_octave, duration):
    """Play a harpsichord note"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.Harpsichord():
        start_recording(instrument.Harpsichord())
    _add_note(note_with_octave, duration)

def play_celesta(note_with_octave, duration):
    """Play a celesta note (bell-like sound)"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.Celesta():
        start_recording(instrument.Celesta())
    _add_note(note_with_octave, duration)

def play_glockenspiel(note_with_octave, duration):
    """Play a glockenspiel note"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.Glockenspiel():
        start_recording(instrument.Glockenspiel())
    _add_note(note_with_octave, duration)

def play_banjo(note_with_octave, duration):
    """Play a banjo note"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.Banjo():
        start_recording(instrument.Banjo())
    _add_note(note_with_octave, duration)

def play_harmonica(note_with_octave, duration):
    """Play a harmonica note"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.Harmonica():
        start_recording(instrument.Harmonica())
    _add_note(note_with_octave, duration)

def play_accordion(note_with_octave, duration):
    """Play an accordion note"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.Accordion():
        start_recording(instrument.Accordion())
    _add_note(note_with_octave, duration)

def play_drum(drum_type, duration):
    """Play a drum sound. Types: 'kick', 'snare', 'hihat', 'crash', 'ride', 'tom'"""
    global _current_stream, _current_offset, _current_instrument
    if _current_stream is None or _current_instrument != instrument.Percussion():
        start_recording(instrument.Percussion())
    
    # Map drum types to MIDI percussion notes (channel 10, standard GM percussion)
    drum_map = {
        'kick': 36,      # C2 - Bass Drum
        'snare': 38,     # D2 - Acoustic Snare
        'hihat': 42,     # F#2 - Closed Hi-Hat
        'crash': 49,     # C#3 - Crash Cymbal
        'ride': 51,      # D#3 - Ride Cymbal
        'tom': 45,       # A2 - Low Tom
        'tom_high': 48,  # C3 - Hi-Mid Tom
        'open_hihat': 46, # A#2 - Open Hi-Hat
    }
    
    midi_num = drum_map.get(drum_type.lower(), 36)  # Default to kick
    
    # Create percussion note on channel 10 (9 in 0-indexed)
    n = note.Note(midi=midi_num)
    n.duration.quarterLength = duration
    n.offset = _current_offset
    n.midiChannel = 9  # Channel 10 for percussion
    # Also set the stream's channel
    if hasattr(_current_stream, 'midiChannel'):
        _current_stream.midiChannel = 9
    _current_stream.insert(_current_offset, n)
    _current_offset += duration

def wait(duration):
    """Wait/rest for a duration - this is the ONLY function that advances the offset"""
    global _current_stream, _current_offset
    if _current_stream is None:
        start_recording()
    
    r = Rest()
    r.duration.quarterLength = duration
    r.offset = _current_offset
    _current_stream.insert(_current_offset, r)
    _current_offset += duration  # Only wait() advances the offset

def end_recording():
    """End the current recording and return the stream"""
    global _current_stream, _current_offset, _current_instrument
    stream_to_return = _current_stream
    _current_stream = None
    _current_offset = 0
    _current_instrument = None
    return stream_to_return

def play_recordings(streams, tempo_bpm=100):
    """Play multiple recordings together"""
    # Create a Score with multiple Parts
    from music21 import stream as stream_module
    
    score = stream_module.Score()
    score.insert(0, tempo.MetronomeMark(number=tempo_bpm))
    score.insert(0, meter.TimeSignature('4/4'))
    
    # Create a Part for each stream to preserve instruments
    for s in streams:
        part = stream_module.Part()
        # Check if this is a percussion stream
        insts = s.getElementsByClass(instrument.Instrument)
        is_percussion = False
        if insts:
            inst = insts[0]
            is_percussion = isinstance(inst, instrument.Percussion)
            part.insert(0, inst)
        
        # Set MIDI channel for percussion (channel 10 = 9 in 0-indexed)
        if is_percussion:
            part.midiChannel = 9
            part.midiProgram = 0
            # Also set instrument's midiChannel
            if insts:
                insts[0].midiChannel = 9
        
        # Copy all notes and rests (but not instruments)
        for element in s:
            if not isinstance(element, instrument.Instrument):
                # Force percussion notes to channel 9
                if is_percussion and isinstance(element, note.Note):
                    element.midiChannel = 9
                part.insert(element.offset, element)
        score.insert(0, part)
    
    # Play the music
    print("Playing music...")
    score.show('midi')
    
    # Keep script running
    print("Music is playing! Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped.")

