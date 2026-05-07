"""
PerceptionAdapter (感知接入器) - External Perception Interface

The PerceptionAdapter is the standardized interface for digital lifeforms
to perceive the external world. It converts various information sources
into a format that digital life can understand.

Core Modules:
    - Text Perception: NLP parsing, semantic encoding, sentiment
    - Image Perception: Visual encoding, object recognition, scene understanding
    - Audio Perception: Speech recognition, sound classification
    - Data Normalization: Format conversion, quality control, priority

Usage:
    >>> from novusvita.perception import PerceptionAdapter
    >>> adapter = PerceptionAdapter()
    >>> result = adapter.perceive("Hello world", modality="text")
"""

__version__ = "0.1.0"


from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from enum import Enum


class Modality(Enum):
    """Supported perception modalities."""
    TEXT = "text"
    IMAGE = "image"
    AUDIO = "audio"
    MULTIMODAL = "multimodal"


@dataclass
class PerceptionResult:
    """Standardized perception result."""
    modality: Modality
    raw_data: Any
    processed_data: Dict[str, Any]
    semantic_embedding: List[float] = field(default_factory=list)
    confidence: float = 0.0
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)


class PerceptionAdapter:
    """
    PerceptionAdapter - External Perception Interface
    
    Standardized interface for digital lifeforms to perceive
    the external world through multiple modalities.
    """
    
    def __init__(self):
        """Initialize the PerceptionAdapter."""
        self.modalities = {
            Modality.TEXT: TextPerceiver(),
            Modality.IMAGE: ImagePerceiver(),
            Modality.AUDIO: AudioPerceiver(),
        }
        self.normalizer = DataNormalizer()
    
    def perceive(
        self, 
        input_data: Any, 
        modality: str
    ) -> PerceptionResult:
        """
        Perceive input data of specified modality.
        
        Args:
            input_data: The input data to perceive
            modality: Modality type ('text', 'image', 'audio')
            
        Returns:
            Standardized PerceptionResult
        """
        modality_enum = Modality(modality.lower())
        perceiver = self.modalities.get(modality_enum)
        
        if perceiver is None:
            raise ValueError(f"Unsupported modality: {modality}")
        
        # Process with specific perceiver
        raw_result = perceiver.process(input_data)
        
        # Normalize the result
        normalized = self.normalizer.normalize(raw_result)
        
        return PerceptionResult(
            modality=modality_enum,
            raw_data=input_data,
            processed_data=normalized,
            confidence=raw_result.get("confidence", 0.0),
            metadata=raw_result.get("metadata", {})
        )
    
    def perceive_text(self, text: str) -> PerceptionResult:
        """
        Perceive text input.
        
        Args:
            text: Text string
            
        Returns:
            PerceptionResult
        """
        return self.perceive(text, "text")
    
    def perceive_image(self, image_data: bytes) -> PerceptionResult:
        """
        Perceive image input.
        
        Args:
            image_data: Image as bytes
            
        Returns:
            PerceptionResult
        """
        return self.perceive(image_data, "image")
    
    def perceive_audio(self, audio_data: bytes) -> PerceptionResult:
        """
        Perceive audio input.
        
        Args:
            audio_data: Audio as bytes
            
        Returns:
            PerceptionResult
        """
        return self.perceive(audio_data, "audio")
    
    def perceive_multimodal(
        self, 
        inputs: List[tuple]
    ) -> List[PerceptionResult]:
        """
        Perceive multiple modality inputs together.
        
        Args:
            inputs: List of (data, modality) tuples
            
        Returns:
            List of PerceptionResults
        """
        results = []
        for data, modality in inputs:
            results.append(self.perceive(data, modality))
        return results


class TextPerceiver:
    """Text perception module."""
    
    def process(self, text: str) -> Dict[str, Any]:
        """
        Process text input.
        
        Args:
            text: Input text string
            
        Returns:
            Processing result dictionary
        """
        # Simplified text processing
        return {
            "text": text,
            "length": len(text),
            "words": text.split(),
            "sentiment": self._analyze_sentiment(text),
            "entities": self._extract_entities(text),
            "confidence": 0.85,
            "metadata": {"source": "text_perceiver"}
        }
    
    def _analyze_sentiment(self, text: str) -> float:
        """Analyze text sentiment."""
        # Simplified sentiment analysis
        positive_words = ["好", "喜欢", "开心", "good", "like", "happy"]
        negative_words = ["坏", "讨厌", "难过", "bad", "hate", "sad"]
        
        pos_count = sum(1 for w in positive_words if w in text.lower())
        neg_count = sum(1 for w in negative_words if w in text.lower())
        
        if pos_count + neg_count == 0:
            return 0.0
        
        return (pos_count - neg_count) / (pos_count + neg_count)
    
    def _extract_entities(self, text: str) -> List[str]:
        """Extract named entities."""
        # Simplified entity extraction
        return []


class ImagePerceiver:
    """Image perception module."""
    
    def process(self, image_data: bytes) -> Dict[str, Any]:
        """
        Process image input.
        
        Args:
            image_data: Image as bytes
            
        Returns:
            Processing result dictionary
        """
        # Simplified image processing
        return {
            "size": len(image_data),
            "format": self._detect_format(image_data),
            "objects": [],
            "scene": "unknown",
            "confidence": 0.75,
            "metadata": {"source": "image_perceiver"}
        }
    
    def _detect_format(self, data: bytes) -> str:
        """Detect image format."""
        if data[:3] == b'\xff\xd8\xff':
            return "jpeg"
        elif data[:4] == b'\x89PNG':
            return "png"
        return "unknown"


class AudioPerceiver:
    """Audio perception module."""
    
    def process(self, audio_data: bytes) -> Dict[str, Any]:
        """
        Process audio input.
        
        Args:
            audio_data: Audio as bytes
            
        Returns:
            Processing result dictionary
        """
        # Simplified audio processing
        return {
            "size": len(audio_data),
            "duration": 0.0,  # Would need actual audio processing
            "speech_detected": False,
            "sound_types": [],
            "confidence": 0.70,
            "metadata": {"source": "audio_perceiver"}
        }


class DataNormalizer:
    """Normalizes perception data to standard format."""
    
    def normalize(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Normalize perception data.
        
        Args:
            data: Raw perception data
            
        Returns:
            Normalized data dictionary
        """
        return {
            "content": data.get("text") or data.get("objects") or data.get("sound_types"),
            "type": data.get("source", "unknown"),
            "attributes": {
                k: v for k, v in data.items()
                if k not in ["text", "objects", "sound_types", "metadata"]
            }
        }
