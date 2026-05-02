from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

# Field allows for validation of the fiels like min, max etc

# These are the schemas for the issue tracker app. They define the structure of the data that will be used in the API. The IssueCreate schema is used for creating a new issue, while the IssueUpdate schema is used for updating an existing issue. The IssueOut schema is used for returning an issue in the API response. The IssueStatus and IssuePriority enums are used to define the possible values for the status and priority fields of an issue.
class IssueStatus(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"


class IssuePriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class IssueCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=5, max_length=1000)
    #status: IssueStatus = Field(default=IssueStatus.OPEN)
    priority: IssuePriority = IssuePriority.MEDIUM

class IssueUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=3, max_length=100)
    description: Optional[str] = Field(default=None, min_length=5, max_length=1000)
    status: Optional[IssueStatus] = Field(default=None)
    priority: Optional[IssuePriority] = Field(default=None)


class IssueOut(BaseModel):
    id: str
    title: str
    description: str
    status: IssueStatus
    priority: IssuePriority