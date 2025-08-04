from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class Activity(BaseModel):
    id: str
    name: str
    description: Optional[str]
    location: Optional[str]
    source: Optional[str]
    price: Optional[float]
    bookable: Optional[bool]
    bookingUrl: Optional[str]
    tags: Optional[List[str]] = []
    suitability: Optional[List[str]] = []
    weatherSuitability: Optional[List[str]] = []
    userSelected: Optional[bool] = False


class WeatherInfo(BaseModel):
    date: str
    description: str
    temperature: Optional[float]
    icon: Optional[str]
    humidity: Optional[int]
    windSpeed: Optional[float]
    source: Optional[str]


class DayPlan(BaseModel):
    id: str
    day: int
    date: str
    morningActivities: List[Activity] = []
    afternoonActivities: List[Activity] = []
    eveningActivities: List[Activity] = []
    weatherInfo: Optional[WeatherInfo]


class TravellerPreferences(BaseModel):
    type: str
    interests: Optional[List[str]] = []


class ItinerarySummary(BaseModel):
    keyLocations: List[str] = []
    mainActivities: List[str] = []
    travellerProfile: Optional[str]


class GuideLanguageSummary(BaseModel):
    en: Optional[str]
    es: Optional[str]
    fr: Optional[str]
    # Add more languages as needed


class Result(BaseModel):
    id: str
    destination: str
    inspiration: Optional[str]
    duration: int
    createdAt: str
    travellerPreferences: TravellerPreferences
    tripSummary: GuideLanguageSummary
    days: List[DayPlan]
    summary: ItinerarySummary
    creditsUsed: Optional[int]
    userCustomizations: Optional[List[str]] = []


class ItineraryEntry(BaseModel):
    id: int
    created_at: str
    user: int
    destination: str
    inspiration: Optional[str]
    travelerType: Optional[str]
    language: Optional[str]
    dateOfTrip: str
    durationOfTrip: int
    status: Optional[str]
    credits: Optional[int]
    result: Result
    interests: Optional[List[str]] = []


class ErrorInfo(BaseModel):
    code: str
    message: str
    details: Optional[Any]


class APIResponse(BaseModel):
    status: str = Field(..., example="success")
    itinerary: List[ItineraryEntry] = []
    error: Optional[ErrorInfo]