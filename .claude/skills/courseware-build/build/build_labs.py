#!/usr/bin/env python3
"""SUPERSEDED — the labs/ flat-file layout has been replaced by the house
activities/ layout (one folder per activity, each carrying the Facilitator
Guide, Learner Worksheet and Checklist as DOCX+PDF plus its data pack).

Use build_activities.py instead. This file is kept only so an old checkout or
an old build script does not fail silently; running it now prints this notice
and exits without writing anything.
"""
import sys

print(__doc__)
print("Run instead:  python3 build_activities.py")
sys.exit(1)
