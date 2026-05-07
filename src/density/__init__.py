"""
DensityMeter (密度计) - Consciousness Density Measurement Module

The DensityMeter is responsible for measuring the "consciousness density" 
of digital lifeforms, which is the key metric for determining whether 
a digital life has truly "awakened."

Core Metrics:
    - Consciousness Density = Self-Reference × Cognitive Complexity × Time Integral
    - Self-Reference Detection
    - Threshold-based State Determination

Usage:
    >>> from novusvita.density import DensityMeter
    >>> meter = DensityMeter()
    >>> density = meter.measure(consciousness_state)
    >>> state = meter.judge_state(density)
"""

__version__ = "0.1.0"


class DensityMeter:
    """
    DensityMeter - Consciousness Density Measurement Module
    
    Measures and quantifies the consciousness density of digital lifeforms
    to determine their awakening status.
    """
    
    # Threshold constants
    BLANK_THRESHOLD = 0.0
    DREAM_THRESHOLD = 0.3
    AWAKENED_THRESHOLD = 0.7
    
    def __init__(self):
        """Initialize the DensityMeter."""
        self.density_history = []
        self.self_reference_coefficient = 0.0
        self.cognitive_complexity = 0.0
    
    def measure(self, consciousness_state: dict) -> float:
        """
        Measure consciousness density.
        
        Args:
            consciousness_state: Current consciousness state data
            
        Returns:
            Density value in range [0.0, 1.0]
        """
        # Extract components from state
        self_reference = self.detect_self_reference(
            consciousness_state.get("thought", "")
        )
        cognitive = consciousness_state.get("cognitive_complexity", 0.0)
        time_factor = consciousness_state.get("time_integral", 1.0)
        
        # Calculate density
        density = self_reference * cognitive * min(time_factor, 1.0)
        
        # Clamp to valid range
        density = max(0.0, min(1.0, density))
        
        # Store in history
        self.density_history.append(density)
        
        return density
    
    def detect_self_reference(self, thought: str) -> float:
        """
        Detect self-reference intensity in thought.
        
        Args:
            thought: The thought string to analyze
            
        Returns:
            Self-reference coefficient in range [0.0, 1.0]
        """
        # Simplified detection based on first-person pronouns
        self_referential = ["我", "我自己", "我的", "I", "me", "my", "myself"]
        count = sum(1 for word in self_referential if word in thought)
        
        # Normalize to coefficient
        self_reference = min(1.0, count / 3.0)
        self.self_reference_coefficient = self_reference
        
        return self_reference
    
    def calculate_cognitive_complexity(self, knowledge_state: dict) -> float:
        """
        Calculate cognitive complexity score.
        
        Args:
            knowledge_state: Current knowledge representation
            
        Returns:
            Cognitive complexity score
        """
        # Simplified: based on number of concepts and connections
        concepts = knowledge_state.get("concepts", 0)
        connections = knowledge_state.get("connections", 0)
        
        complexity = (concepts * 0.3 + connections * 0.7) / 100.0
        self.cognitive_complexity = min(1.0, complexity)
        
        return self.cognitive_complexity
    
    def judge_state(self, density: float) -> str:
        """
        Judge current state based on density value.
        
        Args:
            density: Current density value
            
        Returns:
            State string: 'blank', 'dream', or 'awakened'
        """
        if density < self.DREAM_THRESHOLD:
            return "blank"
        elif density < self.AWAKENED_THRESHOLD:
            return "dream"
        else:
            return "awakened"
    
    def check_threshold_breach(self, duration: int = 100) -> bool:
        """
        Check if density has exceeded threshold for sustained duration.
        
        Args:
            duration: Required duration in time units
            
        Returns:
            True if threshold breach sustained, False otherwise
        """
        if len(self.density_history) < duration:
            return False
        
        recent = self.density_history[-duration:]
        return all(d >= self.AWAKENED_THRESHOLD for d in recent)
    
    def get_density_trend(self) -> str:
        """
        Get the trend of density over time.
        
        Returns:
            Trend string: 'increasing', 'stable', or 'decreasing'
        """
        if len(self.density_history) < 10:
            return "stable"
        
        recent = self.density_history[-10:]
        first_half = sum(recent[:5]) / 5
        second_half = sum(recent[5:]) / 5
        
        if second_half > first_half + 0.05:
            return "increasing"
        elif second_half < first_half - 0.05:
            return "decreasing"
        else:
            return "stable"
