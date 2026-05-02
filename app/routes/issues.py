import uuid
from fastapi import APIRouter, HTTPException, status
from app.schemas import IssueCreate, IssueUpdate, IssueOut, IssueStatus
from app.storage import load_data, save_data

router = APIRouter(prefix="/api/v1/issues", tags=["issues"])

@router.get("/", response_model=list[IssueOut], status_code=status.HTTP_200_OK)
def get_issues():
    """Retrieves all issues."""
    issues = load_data()
    return issues

@router.post("/", response_model=IssueOut, status_code=status.HTTP_201_CREATED)
def create_issue(payload: IssueCreate):
    """Creates a new issue."""
    issues = load_data()

    new_issue = {
        "id": str(uuid.uuid4()),
        "title": payload.title,
        "description": payload.description,
        "priority": payload.priority,
        "status": IssueStatus.OPEN
    }

    issues.append(new_issue) # type: ignore
    save_data(issues)
    return new_issue

@router.put("/{issue_id}", response_model=IssueOut, status_code=status.HTTP_200_OK)
def update_issue(issue_id: str, payload: IssueUpdate):
    """Updates an existing issue."""
    issues = load_data()
    if issues is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="failed to load issues data")
    
    for issue in issues:
        if issue["id"] == issue_id:
            if payload.title is not None:
                issue["title"] = payload.title
            if payload.description is not None:
                issue["description"] = payload.description
            if payload.status is not None:
                issue["status"] = payload.status
            if payload.priority is not None:
                issue["priority"] = payload.priority
            save_data(issues)
            return IssueOut(**issue)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")

@router.get("/{issue_id}", response_model=IssueOut, status_code=status.HTTP_200_OK)
def get_issue(issue_id: str):
    """Retrieves a specific issue by ID."""
    issues = load_data()
    if issues is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="failed to load issues data")
    for issue in issues:
        if issue["id"] == issue_id:
            return IssueOut(**issue)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")

@router.delete("/{issue_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_issue(issue_id: str):
    """Deletes an issue by ID."""
    issues = load_data()
    if issues is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="failed to load issues data")
    for index, issue in enumerate(issues):
        if issue["id"] == issue_id:
            issues.pop(index)
            save_data(issues)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")