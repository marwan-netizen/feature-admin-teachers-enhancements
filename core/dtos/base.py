from typing import List, Optional
from pydantic import BaseModel, Field

class PhoneticDTO(BaseModel):
    text: Optional[str] = None
    audio: Optional[str] = None

class MeaningDTO(BaseModel):
    part_of_speech: str = Field(alias="partOfSpeech")
    definitions: List[str]

class WordDefinitionDTO(BaseModel):
    word: str
    phonetics: List[PhoneticDTO] = []
    meanings: List[MeaningDTO] = []
    source_urls: List[str] = Field(default=[], alias="sourceUrls")

class SynonymAntonymDTO(BaseModel):
    word: str
    score: Optional[int] = None
    tags: List[str] = []

class ExampleSentenceDTO(BaseModel):
    text: str
    translation: Optional[str] = None
    source: Optional[str] = None

class GrammarIssueDTO(BaseModel):
    message: str
    short_message: Optional[str] = None
    offset: int
    length: int
    replacements: List[str] = []
    rule_id: str
    category: str

class GrammarAnalysisDTO(BaseModel):
    text: str
    issues: List[GrammarIssueDTO] = []

class MediaContentDTO(BaseModel):
    title: str
    content: str
    url: Optional[str] = None
    thumbnail: Optional[str] = None
    source: str
    metadata: dict = {}

class LearningGapDTO(BaseModel):
    topic: str
    level: str
    description: str
    recommended_actions: List[str] = []
