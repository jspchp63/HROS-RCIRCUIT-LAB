# ============================================================
# RCIRCUIT CORE PROTOTYPE v0.2
# Added:
#  - PhaseScheduler
#  - Δsignal Normalization
#  - Basic Coherence Map
# ============================================================

class PhaseNode:
    def __init__(self, phase=0.0):
        self.phase = phase
        self.noise = 0.0
        self.resonance = 0.0

    def update_phase(self, delta_phase):
        self.phase += delta_phase

    def compute_resonance(self, neighbor_phase):
        diff = abs(self.phase - neighbor_phase)
        self.resonance = 1.0 / (1.0 + diff)
        return self.resonance


class DeltaSignal:
    def __init__(self, value):
        self.value = value


class PhaseScheduler:
    """Determines which node updates first."""
    def pick_node(self, nodes):
        return max(range(len(nodes)), key=lambda i: nodes[i].noise)


class RCIRCUIT:
    def __init__(self):
        self.nodes = []
        self.scheduler = PhaseScheduler()

    def add_node(self, node: PhaseNode):
        self.nodes.append(node)

    def normalize(self, delta: float):
        """Δ normalization for stability."""
        return max(min(delta, 1.0), -1.0)

    def noise_filter(self, delta: float, threshold: float = 0.05):
        if abs(delta) < threshold:
            return None
        return DeltaSignal(self.normalize(delta))

    def propagate(self, node_index: int, delta_signal: DeltaSignal):
        if delta_signal is None:
            return
        for i, node in enumerate(self.nodes):
            if i == node_index:
                continue
            node.update_phase(delta_signal.value)
