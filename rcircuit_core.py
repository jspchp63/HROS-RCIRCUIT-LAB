# ============================================================
# RCIRCUIT CORE PROTOTYPE v0.1
# Phase Computing · Δsignal Propagation · Resonance Engine
# Author: Chulhee Park (HROS Lab)
# ============================================================

class PhaseNode:
    """
    A minimal unit of RCIRCUIT.
    Holds:
        - local phase
        - local noise estimate
        - last resonance score
    """
    def __init__(self, phase=0.0):
        self.phase = phase          # local phase value
        self.noise = 0.0            # local noise
        self.resonance = 0.0        # coherence score

    def update_phase(self, delta_phase):
        """Phase adjustment (local coherence alignment)."""
        self.phase += delta_phase

    def compute_resonance(self, neighbor_phase):
        """
        Simple coherence function:
        High when phases are similar, low when different.
        """
        diff = abs(self.phase - neighbor_phase)
        self.resonance = 1.0 / (1.0 + diff)
        return self.resonance


class DeltaSignal:
    """
    The Δsignal object: what gets propagated.
    NOT full data. Only meaningful change.
    """
    def __init__(self, value):
        self.value = value  # value = phase difference OR semantic delta


class RCIRCUIT:
    """
    Main resonance engine (prototype).
    Handles:
        - local phase update
        - noise filtering
        - Δsignal propagation
    """
    def __init__(self):
        self.nodes = []

    def add_node(self, node: PhaseNode):
        self.nodes.append(node)

    def noise_filter(self, delta: float, threshold: float = 0.05):
        """
        If Δ is too small (noise), remove it.
        Only propagate meaningful Δsignal.
        """
        if abs(delta) < threshold:
            return None  # filtered out
        return DeltaSignal(delta)

    def propagate(self, node_index: int, delta_signal: DeltaSignal):
        """
        Propagate Δsignal to neighbors (conceptual).
        Only phase changes, not raw tensor movement.
        """
        if delta_signal is None:
            return
        
        for i, node in enumerate(self.nodes):
            if i == node_index:
                continue
            node.update_phase(delta_signal.value)


# ============================================================
# Example usage (toy)
# ============================================================

if __name__ == "__main__":
    # Build simple RCIRCUIT
    rc = RCIRCUIT()
    rc.add_node(PhaseNode(phase=1.0))
    rc.add_node(PhaseNode(phase=1.5))

    # Compute Δ
    delta = 1.5 - 1.0

    # Filter noise
    signal = rc.noise_filter(delta)

    # Propagate meaningful Δ
    rc.propagate(0, signal)

    print("Node phases after propagation:")
    for n in rc.nodes:
        print(n.phase)

