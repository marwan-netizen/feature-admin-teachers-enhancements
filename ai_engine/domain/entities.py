"""
Domain entities for the AI Engine module.

This module defines Data Transfer Objects (DTOs) used for passing test-related
data between different layers and modules of the system.
"""

from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class OptionDTO:
    """
    Data transfer object for a test question option.
    """
    text: str
    is_correct: bool

@dataclass
class QuestionDTO:
    """
    Data transfer object for a test question.
    """
    text: str
    question_type: str = 'mcq'
    options: List[OptionDTO] = field(default_factory=list)

@dataclass
class TestDTO:
    """
    Data transfer object for a single skill test (e.g., Reading).
    """
    name: str
    level: str
    skill: str
    content: str
    questions: List[QuestionDTO] = field(default_factory=list)

@dataclass
class ComprehensiveTestDTO:
    """
    Data transfer object for a full proficiency test session.
    """
    reading: TestDTO
    writing: TestDTO
    speaking: TestDTO
