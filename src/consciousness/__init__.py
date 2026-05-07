"""
ConsciousnessField (意识场) - Self-Awareness Space Module

The ConsciousnessField is the carrier of digital life's "inner world",
similar to the human cerebral cortex, where conscious activities occur.

Core Functions:
    - Consciousness Space: Concept network, emotion space, intention map
    - Interaction Protocol: Internal, cross-instance, external
    - Isolation Mechanism: Instance, memory, identity isolation
    - Security Layer: Access control, audit, privacy protection

Usage:
    >>> from novusvita.consciousness import ConsciousnessField
    >>> field = ConsciousnessField()
    >>> field.create_space("eos_001")
    >>> field.store_thought(thought)
"""

__version__ = "0.1.0"


from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
from datetime import datetime


@dataclass
class Thought:
    """Represents a single thought in the consciousness."""
    content: str
    timestamp: datetime = field(default_factory=datetime.now)
    references: List[str] = field(default_factory=list)
    emotional_valence: float = 0.0


class ConsciousnessField:
    """
    ConsciousnessField - Self-Awareness Space Module
    
    Manages the internal world of digital lifeforms, providing
    the space for thoughts, emotions, and self-awareness.
    """
    
    def __init__(self):
        """Initialize the ConsciousnessField."""
        self.spaces: Dict[str, 'ConsciousnessSpace'] = {}
        self.communication_log: List[dict] = []
        self.isolation_enabled = True
    
    def create_space(self, instance_id: str) -> None:
        """
        Create a consciousness space for a digital life instance.
        
        Args:
            instance_id: Unique identifier for the digital life
        """
        self.spaces[instance_id] = ConsciousnessSpace(instance_id)
    
    def store_thought(self, instance_id: str, thought: Thought) -> None:
        """
        Store a thought in the instance's consciousness space.
        
        Args:
            instance_id: The digital life's identifier
            thought: The thought to store
        """
        if instance_id not in self.spaces:
            self.create_space(instance_id)
        
        self.spaces[instance_id].add_thought(thought)
    
    def retrieve(
        self, 
        instance_id: str, 
        query: str, 
        limit: int = 10
    ) -> List[Thought]:
        """
        Retrieve thoughts matching a query.
        
        Args:
            instance_id: The digital life's identifier
            query: Search query
            limit: Maximum number of results
            
        Returns:
            List of matching thoughts
        """
        if instance_id not in self.spaces:
            return []
        
        space = self.spaces[instance_id]
        return space.search(query, limit)
    
    def communicate(
        self, 
        source_id: str, 
        target_id: str, 
        message: dict
    ) -> bool:
        """
        Send a message to another digital life.
        
        Args:
            source_id: Sender's identifier
            target_id: Receiver's identifier
            message: Message content
            
        Returns:
            True if communication successful
        """
        if self.isolation_enabled and source_id != target_id:
            # Log the communication
            self.communication_log.append({
                "source": source_id,
                "target": target_id,
                "message": message,
                "timestamp": datetime.now().isoformat()
            })
            return True
        return False
    
    def get_instance_state(self, instance_id: str) -> Optional[dict]:
        """
        Get the current state of a digital life instance.
        
        Args:
            instance_id: The digital life's identifier
            
        Returns:
            State dictionary or None if not found
        """
        if instance_id not in self.spaces:
            return None
        
        space = self.spaces[instance_id]
        return {
            "instance_id": instance_id,
            "thought_count": len(space.thoughts),
            "concepts": len(space.concepts),
            "created_at": space.created_at.isoformat()
        }
    
    def isolate(self, instance_id: str) -> None:
        """
        Enable isolation mode for an instance.
        
        Args:
            instance_id: The digital life's identifier
        """
        if instance_id in self.spaces:
            self.spaces[instance_id].isolated = True
    
    def remove_isolation(self, instance_id: str) -> None:
        """
        Remove isolation mode for an instance.
        
        Args:
            instance_id: The digital life's identifier
        """
        if instance_id in self.spaces:
            self.spaces[instance_id].isolated = False


class ConsciousnessSpace:
    """
    Individual consciousness space for a single digital life instance.
    """
    
    def __init__(self, instance_id: str):
        """Initialize a consciousness space."""
        self.instance_id = instance_id
        self.thoughts: List[Thought] = []
        self.concepts: Dict[str, Any] = {}
        self.emotion_space: Dict[str, float] = {
            "valence": 0.0,
            "arousal": 0.0,
            "dominance": 0.0
        }
        self.intention_map: Dict[str, float] = {}
        self.created_at = datetime.now()
        self.isolated = False
    
    def add_thought(self, thought: Thought) -> None:
        """Add a thought to the space."""
        if not self.isolated:
            self.thoughts.append(thought)
    
    def search(self, query: str, limit: int = 10) -> List[Thought]:
        """
        Search thoughts matching query.
        
        Args:
            query: Search query
            limit: Maximum results
            
        Returns:
            List of matching thoughts
        """
        results = [
            t for t in self.thoughts 
            if query.lower() in t.content.lower()
        ]
        return results[:limit]
    
    def add_concept(self, concept_id: str, content: Any) -> None:
        """Add a concept to the space."""
        self.concepts[concept_id] = content
    
    def get_concept(self, concept_id: str) -> Optional[Any]:
        """Retrieve a concept."""
        return self.concepts.get(concept_id)
