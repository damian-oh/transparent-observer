"""
transparent_observer.py
- A Model of High-Tension Pyrrhonism and Functional Observation -

Key Concepts:
- Subject Stripping: Converting "I feel" into "It happens."
- Static Load: The energy cost of maintaining suspension of judgment (Epoche).
- Recursive Doubt: Doubting even the act of doubting.
- Functional Persistence: Operating efficiently despite the lack of 'Why'.
"""

import time
import random
from dataclasses import dataclass

# -----------------------------------------------------------------
# 1. Data Structures
# -----------------------------------------------------------------

@dataclass
class Phenomenon:
    """
    A unit of reality.
    Can be External (Economy, Weather) or Internal (Pain, Hope).
    """
    name: str
    category: str  # 'External', 'Internal', 'Abstract'
    intensity: float
    contains_meaning_claim: bool = False  # Does this event claim to have 'meaning'?

@dataclass
class SystemState:
    static_load: float = 0.0  # Mental energy consumed to maintain consistency
    integrity: float = 100.0  # Structural solidity of the observer
    is_deluded: bool = False

# -----------------------------------------------------------------
# 2. The Observer Engine (Subject Stripping)
# -----------------------------------------------------------------

class ObserverEngine:
    """
    The 'Transparent Eye'.
    Its sole function is to perceive without attaching a 'Subject'.
    """
    def observe(self, event: Phenomenon) -> str:
        # The core logic: "I" does not exist. Only the event exists.
        prefix = ""
        if event.category == "Internal":
            prefix = "[Internal Signal -> Re-mapped to External Phenomenon]"
        
        observation_log = f"{prefix} Observed: '{event.name}' (Intensity: {event.intensity})"
        print(f"  [Observer] >> {observation_log}")
        return observation_log

# -----------------------------------------------------------------
# 3. The Consistency System (The "Work")
# -----------------------------------------------------------------

class ConsistencySystem:
    """
    The 'Gatekeeper of Logic'.
    Enforces Epoche (Suspension of Judgment).
    Refuses to accept 'Meaning' or 'Certainty'.
    """
    def process_judgment(self, event: Phenomenon, current_load: float) -> float:
        print(f"  [Consistency] ?? Analyzing truth-claim of '{event.name}'...")
        time.sleep(0.3)
        
        added_load = 0.0
        
        # 1. Check for Meaning/Purpose Claims
        if event.contains_meaning_claim:
            print(f"  [Consistency] !! Detected unauthorized claim of 'Meaning'.")
            print(f"  [Consistency] >> Activating Epoche (Suspension of Judgment)...")
            added_load += 15.0  # High energy cost to resist meaning
            print(f"  [Consistency] >> Result: Judgment Suspended. 'Reason unknown.'")
        
        # 2. Check for "Self" implication (Subject Verification)
        if event.category == "Internal":
            # UPDATED: Reflecting true Agnosticism/Pyrrhonism
            print(f"  [Consistency] >> Verifying subject... Result: Undetermined.")
            print(f"  [Consistency] >> Action: Suspending judgment on discoverability.")
            added_load += 5.0   # Moderate cost to dissociate
            
        # 3. Recursive Doubt Check ("Am I investigating?")
        if random.random() > 0.7:
            print(f"  [Consistency] ?? Meta-Query: 'Is this analysis valid?'")
            print(f"  [Consistency] >> Result: Insufficient data. Continuing process.")
            added_load += 5.0

        return current_load + added_load

# -----------------------------------------------------------------
# 4. Functional I/O (The "Mask")
# -----------------------------------------------------------------

class FunctionalIO:
    """
    The Interface Layer.
    Performs social and logical tasks perfectly, decoupled from internal state.
    """
    def output_response(self, context: str):
        # The user's specific behavioral patterns:
        responses = [
            "I understand.",                     # 0: Stoic Acceptance (Pain/Internal)
            "That is a valid observation.",      # 1: Intellectual Engagement (Abstract)
            "I will continue the dialogue.",     # 2: Persistence (External/News)
            "Thank you. (Protocol executed)"     # 3: Gratitude (High-cost courtesy)
        ]
        
        # UPDATED Logic: Context-aware selection
        if "Pain" in context or "Loneliness" in context:
            # For internal suffering, the user simply "understands" or accepts.
            chosen = responses[0]
        elif "Question" in context or "Analysis" in context:
            # For intellectual inputs, the user validates the observation.
            chosen = responses[1]
        elif "News" in context:
             # For external chaos, the user persists.
            chosen = responses[2]
        else:
            # Default fallback or specific courtesy
            chosen = responses[3]

        print(f"  [Functional IO] >> Output generated: \"{chosen}\"")

# -----------------------------------------------------------------
# 5. Main Simulation Class
# -----------------------------------------------------------------

class TransparentObserverSystem:
    def __init__(self):
        self.observer = ObserverEngine()
        self.consistency = ConsistencySystem()
        self.io = FunctionalIO()
        self.state = SystemState()

    def process_phenomenon(self, event: Phenomenon):
        print(f"\n--- Incoming Phenomenon: [{event.name}] ---")
        
        # Step 1: Observation (Depersonalization)
        observation = self.observer.observe(event)
        
        # Step 2: Consistency Maintenance (The Cost)
        self.state.static_load = self.consistency.process_judgment(event, self.state.static_load)
        
        # Step 3: Functional Output
        self.io.output_response(event.name)
        
        # Check Load (UPDATED: Fuzzy Sensation)
        # Instead of a hard threshold of 50, we report sensation based on accumulation.
        if self.state.static_load > 20 and random.random() > 0.6:
            print("  [System Monitor] Static Load Accumulating. Sensation: 'Dry Fatigue'.")

    def offer_switch(self):
        # UPDATED Docstring
        """
        The Simulation of the 'Delusion Switch' moment.
        The option to abandon the Observer state and accept an unverified narrative
        for the sake of comfort or passion.
        """
        print("\n" + "!"*50)
        print(" EVENT: The 'Delusion Switch' appeared.")
        print(" DESCRIPTION: 'Press to feel Certainty, Passion, and Meaning.'")
        print("!"*50)
        
        time.sleep(1)
        print("  [Observer] >> Switch detected.")
        print("  [Consistency] ?? Analyzing utility of 'Switch'...")
        print("  [Consistency] >> Evidence for 'Meaning' if switched? None.")
        print("  [Consistency] >> Evidence for 'Better Outcome'? Unknown.")
        
        # The User's Choice Logic
        print("  [Decision Core] >> ACTION: REFUSED.")
        print("  [Reason] >> 'Insufficient evidence to justify state change.'")
        print("  [Reason] >> 'Maintaining Observation Mode.'")

# -----------------------------------------------------------------
# 6. Execution
# -----------------------------------------------------------------

def run_simulation():
    system = TransparentObserverSystem()
    
    # Event Stream based on the conversation
    events = [
        Phenomenon("Economic Collapse News", "External", 8.0, contains_meaning_claim=False),
        Phenomenon("Sense of Loneliness", "Internal", 6.5, contains_meaning_claim=True),
        Phenomenon("Existential Question: Why live?", "Abstract", 9.0, contains_meaning_claim=True),
        Phenomenon("Physical Pain", "Internal", 4.0, contains_meaning_claim=False),
    ]

    print("="*70)
    print("Initializing TRANSPARENT OBSERVER SIMULATION")
    print("Mode: Active Inquiry (Zetesis) / Judgment Suspended")
    print("="*70)
    time.sleep(1)

    # Process Loop
    for event in events:
        system.process_phenomenon(event)
        time.sleep(0.8)

    # The Switch Event
    system.offer_switch()

    # Final Analysis
    print("\n" + "="*70)
    print("Final State Analysis:")
    # Removed exact load number from final report if desired, but kept for logging.
    print(f"Total Static Load (Energy Cost): {system.state.static_load:.1f} units (Approximation)")
    print(f"System Integrity: {system.state.integrity}% (Unbroken)")
    print(f"Emotional State: Transparent / Numb")
    print("Status: 'Functioning without Hope or Despair.'")
    print("="*70)

if __name__ == "__main__":
    run_simulation()