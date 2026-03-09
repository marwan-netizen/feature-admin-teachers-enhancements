from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class OptionDTO:
    text: str
    is_correct: bool

@dataclass
class QuestionDTO:
    text: str
    question_type: str = 'mcq'
    options: List[OptionDTO] = field(default_factory=list)

@dataclass
class TestDTO:
    name: str
    level: str
    skill: str
    content: str
    questions: List[QuestionDTO] = field(default_factory=list)

@dataclass
class ComprehensiveTestDTO:
    reading: TestDTO
    writing: TestDTO
    speaking: TestDTO
