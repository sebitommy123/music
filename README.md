# Music21 Music Project

This project uses music21 for creating and playing music in Python with a simple, easy-to-use wrapper.

## Quick Setup (macOS)

**One-click setup:**
```bash
./setup.sh
```

That's it! The script will:
- Check for Python 3
- Create a virtual environment
- Install music21 and all dependencies
- Verify everything works

## Manual Setup

If you prefer to set up manually:

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install music21

# Run the example
python test.py
```

## Usage

### Basic Example

```python
from wrapper import *

start_recording()
play_piano("A4", 0.5)
play_piano("C5", 0.5)
piano = end_recording()

play_recordings([piano])
```

### Available Instruments

**Piano & Keys:**
- `play_piano(note, duration)` - Acoustic Piano
- `play_electric_piano(note, duration)` - Electric Piano
- `play_organ(note, duration)` - Organ
- `play_harpsichord(note, duration)` - Harpsichord
- `play_celesta(note, duration)` - Celesta (bell-like)

**Guitars:**
- `play_guitar(note, duration)` - Acoustic Guitar
- `play_banjo(note, duration)` - Banjo

**Bass:**
- `play_bass(note, duration)` - Acoustic Bass
- `play_electric_bass(note, duration)` - Electric Bass
- `play_fretless_bass(note, duration)` - Fretless Bass
- `play_bass_synth(note, duration)` - Synth Bass 1
- `play_bass_synth_2(note, duration)` - Synth Bass 2

**Electronic/Synth (Real MIDI Synth Sounds):**
- `play_synth(note, duration)` - Synth Lead 1 (Sawtooth)
- `play_lead_synth(note, duration)` - Synth Lead 2 (Sawtooth)
- `play_lead_synth_square(note, duration)` - Synth Lead 3 (Calliope/Square)
- `play_lead_synth_chiff(note, duration)` - Synth Lead 4 (Chiff)
- `play_lead_synth_charang(note, duration)` - Synth Lead 5 (Charang)
- `play_lead_synth_voice(note, duration)` - Synth Lead 6 (Voice)
- `play_lead_synth_fifths(note, duration)` - Synth Lead 7 (Fifths)
- `play_lead_synth_bass_lead(note, duration)` - Synth Lead 8 (Bass + Lead)
- `play_pad_synth(note, duration)` - Synth Pad 1 (New Age)
- `play_pad_synth_warm(note, duration)` - Synth Pad 2 (Warm)
- `play_pad_synth_polysynth(note, duration)` - Synth Pad 3 (Polysynth)
- `play_pad_synth_choir(note, duration)` - Synth Pad 4 (Choir)
- `play_pad_synth_bowed(note, duration)` - Synth Pad 5 (Bowed)
- `play_pad_synth_metallic(note, duration)` - Synth Pad 6 (Metallic)
- `play_pad_synth_halo(note, duration)` - Synth Pad 7 (Halo)
- `play_pad_synth_sweep(note, duration)` - Synth Pad 8 (Sweep)
- `play_synth_brass(note, duration)` - Synth Brass 1
- `play_synth_brass_2(note, duration)` - Synth Brass 2
- `play_synth_strings(note, duration)` - Synth Strings 1
- `play_synth_strings_2(note, duration)` - Synth Strings 2

**Brass:**
- `play_trumpet(note, duration)` - Trumpet
- `play_trombone(note, duration)` - Trombone
- `play_horn(note, duration)` - French Horn

**Woodwinds:**
- `play_flute(note, duration)` - Flute
- `play_saxophone(note, duration)` - Alto Saxophone
- `play_clarinet(note, duration)` - Clarinet
- `play_oboe(note, duration)` - Oboe

**Strings:**
- `play_violin(note, duration)` - Violin
- `play_viola(note, duration)` - Viola
- `play_cello(note, duration)` - Cello
- `play_harp(note, duration)` - Harp

**Percussion:**
- `play_drum(type, duration)` - Drums
  - Types: `'kick'`, `'snare'`, `'hihat'`, `'crash'`, `'ride'`, `'tom'`, `'tom_high'`, `'open_hihat'`
- `play_glockenspiel(note, duration)` - Glockenspiel

**Other:**
- `play_harmonica(note, duration)` - Harmonica
- `play_accordion(note, duration)` - Accordion

**Utilities:**
- `wait(duration)` - Rest/wait

### Example with Multiple Instruments

```python
from wrapper import *

# Piano part
start_recording()
play_piano("A4", 0.5)
play_piano("C5", 1.0)
piano = end_recording()

# Drums
start_recording()
play_drum("kick", 0.5)
play_drum("snare", 0.5)
drums = end_recording()

# Play together
play_recordings([piano, drums])
```

## Files

- `wrapper.py` - The music wrapper (import this!)
- `test.py` - Example usage with all instruments
- `setup.sh` - Automated setup script
- `README.md` - This file

## Notes

- Notes are specified as strings like "A4", "C#5", "G#6"
- Durations are in beats (quarter notes)
- The music will open in GarageBand (or your default MIDI player) on macOS
