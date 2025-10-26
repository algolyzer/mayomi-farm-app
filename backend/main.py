from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(title="Mayomi Nishat Agro Farm API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class Product(BaseModel):
    id: int
    name: str
    name_bn: str
    category: str
    description: str
    description_bn: str
    image: str
    price: Optional[float] = None

class ChatMessage(BaseModel):
    message: str

class ContactForm(BaseModel):
    name: str
    email: str
    phone: str
    message: str

# Sample data
products = [
    {
        "id": 1,
        "name": "Pangasius Fish",
        "name_bn": "পাঙ্গাশ মাছ",
        "category": "fish",
        "description": "Fresh and healthy Pangasius fish from our farm",
        "description_bn": "আমাদের খামার থেকে তাজা ও স্বাস্থ্যকর পাঙ্গাশ মাছ",
        "image": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=500",
        "price": 250
    },
    {
        "id": 2,
        "name": "Tilapia Fish",
        "name_bn": "তেলাপিয়া মাছ",
        "category": "fish",
        "description": "Premium quality Tilapia fish",
        "description_bn": "উন্নতমানের তেলাপিয়া মাছ",
        "image": "https://images.unsplash.com/photo-1534043464124-3be32fe000c9?w=500",
        "price": 180
    },
    {
        "id": 3,
        "name": "Fresh Milk",
        "name_bn": "তাজা দুধ",
        "category": "dairy",
        "description": "100% pure and fresh cow milk",
        "description_bn": "১০০% বিশুদ্ধ ও তাজা গরুর দুধ",
        "image": "https://images.unsplash.com/photo-1550583724-b2692b85b150?w=500",
        "price": 80
    },
    {
        "id": 4,
        "name": "Broiler Chicken",
        "name_bn": "ব্রয়লার মুরগি",
        "category": "poultry",
        "description": "Healthy broiler chicken meat",
        "description_bn": "স্বাস্থ্যকর ব্রয়লার মুরগির মাংস",
        "image": "https://images.unsplash.com/photo-1587593810167-a84920ea0781?w=500",
        "price": 220
    },
    {
        "id": 5,
        "name": "Farm Fresh Eggs",
        "name_bn": "খামারের তাজা ডিম",
        "category": "poultry",
        "description": "Farm fresh organic eggs",
        "description_bn": "খামারের তাজা জৈব ডিম",
        "image": "https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?w=500",
        "price": 12
    },
    {
        "id": 6,
        "name": "Premium Rice",
        "name_bn": "উন্নতমানের চাল",
        "category": "crops",
        "description": "High quality rice from our farm",
        "description_bn": "আমাদের খামার থেকে উচ্চমানের চাল",
        "image": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=500",
        "price": 60
    },
    {
        "id": 7,
        "name": "Mangoes",
        "name_bn": "আম",
        "category": "fruits",
        "description": "Sweet and juicy seasonal mangoes",
        "description_bn": "মিষ্টি ও রসালো মৌসুমি আম",
        "image": "https://images.unsplash.com/photo-1591073113125-e46713c829ed?w=500",
        "price": 150
    },
    {
        "id": 8,
        "name": "Desi Chicken",
        "name_bn": "দেশি মুরগি",
        "category": "poultry",
        "description": "Traditional farm-raised desi chicken",
        "description_bn": "ঐতিহ্যবাহী খামারে পালিত দেশি মুরগি",
        "image": "https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?w=500",
        "price": 450
    }
]

# Routes
@app.get("/")
def read_root():
    return {
        "message": "Welcome to Mayomi Nishat Agro Farm API",
        "version": "1.0.0"
    }

@app.get("/api/products", response_model=List[Product])
def get_products(category: Optional[str] = None):
    if category:
        filtered = [p for p in products if p["category"] == category]
        return filtered
    return products

@app.get("/api/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/api/chat")
def chat(message: ChatMessage):
    # Simple chatbot responses
    user_message = message.message.lower()
    
    responses = {
        "hello": "আসসালামু আলাইকুম! মায়োমি নিশাত এগ্রো ফার্মে আপনাকে স্বাগতম। আমি আপনাকে কীভাবে সাহায্য করতে পারি?",
        "hi": "হ্যালো! আমাদের ফার্ম সম্পর্কে জানতে চান?",
        "product": "আমাদের পণ্যগুলির মধ্যে রয়েছে: মাছ, দুধ, মুরগি, ডিম, চাল এবং মৌসুমি আম। কোনটি সম্পর্কে জানতে চান?",
        "fish": "আমরা পাঙ্গাশ, শিং, তেলাপিয়া, রুই এবং মৃগেল মাছ চাষ করি। সব মাছ স্বাস্থ্যকর পরিবেশে চাষ করা হয়।",
        "milk": "আমাদের দুধ ১০০% বিশুদ্ধ এবং কোনো রাসায়নিক মিশ্রণ ছাড়াই সংগ্রহ করা হয়।",
        "chicken": "আমরা ব্রয়লার, দেশি এবং লেয়ার মুরগি পালন করি। সব মুরগি স্বাস্থ্যবিধি মেনে পালন করা হয়।",
        "price": "দাম জানতে আমাদের সাথে যোগাযোগ করুন: +8801711727357",
        "contact": "📞 ফোন: +8801711727357\n📧 ইমেইল: nishat@manishatagro.com\n📍 ঠিকানা: Vabakhali bazar",
        "location": "আমরা Vabakhali bazar এ অবস্থিত।"
    }
    
    for key in responses:
        if key in user_message:
            return {"response": responses[key]}
    
    return {
        "response": "ধন্যবাদ আপনার বার্তার জন্য। আরো তথ্যের জন্য আমাদের সাথে যোগাযোগ করুন: +8801711727357"
    }

@app.post("/api/contact")
def submit_contact(form: ContactForm):
    # In production, save to database or send email
    return {
        "success": True,
        "message": "আপনার বার্তা সফলভাবে পাঠানো হয়েছে। আমরা শীঘ্রই আপনার সাথে যোগাযোগ করব।"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
