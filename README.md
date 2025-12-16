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
- `play_bass_synth(note, duration)` - Bass Synthesizer

**Electronic/Synth:**
- `play_synth(note, duration)` - Synthesizer (Electric Organ)
- `play_lead_synth(note, duration)` - Lead Synthesizer
- `play_pad_synth(note, duration)` - Pad Synthesizer (warm, sustained)

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
