from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from user_database.db import get_db
from user_models.model import Post
from user_schemas.schemas import PostCreate, PostResponse
from user_auth.security import get_current_user

router = APIRouter(prefix="/posts", tags=["Posts"])

# ---------------- Create Post ----------------
@router.post("/", response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    new_post = Post(**post.dict(), owner_id=current_user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# ---------------- Get All Posts ----------------
@router.get("/", response_model=list[PostResponse])
def get_all_posts(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    posts = db.query(Post).filter(Post.owner_id == current_user.id).all()
    return posts

# ---------------- Get Single Post ----------------
@router.get("/{post_id}", response_model=PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    post = db.query(Post).filter(Post.id == post_id, Post.owner_id == current_user.id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post
