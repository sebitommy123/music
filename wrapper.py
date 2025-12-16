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
    _current_instrument = instrument_type
    if instrument_type:
        _current_stream.insert(0, instrument_type)
    return _current_stream

def _add_note(note_with_octave, duration):
    """Internal helper to add a note to the current stream"""
    global _current_stream, _current_offset
    if _current_stream is None:
        start_recording()
    
    n = note.Note(note_with_octave)
    n.duration.quarterLength = duration
    n.offset = _current_offset
    _current_stream.insert(_current_offset, n)
    _current_offset += duration

def play_piano(note_with_octave, duration):
    """Play a piano note (e.g., 'A4', 'C#5', 'G#6')"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.Piano():
        start_recording(instrument.Piano())
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

def play_synth(note_with_octave, duration):
    """Play a synthesizer note (e.g., 'A4', 'C#5', 'G#6')"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.ElectricOrgan():
        start_recording(instrument.ElectricOrgan())
    _add_note(note_with_octave, duration)

def play_bass_synth(note_with_octave, duration):
    """Play a bass synthesizer note (e.g., 'A2', 'C3')"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.ElectricBass():
        start_recording(instrument.ElectricBass())
    _add_note(note_with_octave, duration)

def play_lead_synth(note_with_octave, duration):
    """Play a lead synthesizer note (e.g., 'A4', 'C#5')"""
    global _current_instrument
    if _current_stream is None or _current_instrument != instrument.ElectricGuitar():
        start_recording(instrument.ElectricGuitar())
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
    """Wait/rest for a duration"""
    global _current_stream, _current_offset
    if _current_stream is None:
        start_recording()
    
    r = Rest()
    r.duration.quarterLength = duration
    r.offset = _current_offset
    _current_stream.insert(_current_offset, r)
    _current_offset += duration

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

