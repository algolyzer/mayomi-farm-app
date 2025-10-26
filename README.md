# 🌾 মায়োমি নিশাত এগ্রো ফার্ম - Website

A beautiful, modern, and fully responsive website for Mayomi Nishat Agro Farm built with **FastAPI** (backend) and **Vue.js** (frontend).

## ✨ Features

- 🎨 **Beautiful Modern Design** - Clean, professional UI with smooth animations
- 📱 **100% Responsive** - Perfect on mobile, tablet, and desktop
- 🤖 **AI Chatbot** - Interactive chatbot for customer support
- 🛒 **Product Catalog** - Browse all farm products with filtering
- 📧 **Contact Form** - Easy way for customers to get in touch
- 🌐 **Bilingual** - Bengali and English support
- ⚡ **Fast & Lightweight** - Optimized performance

## 🚀 Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation

### Frontend
- **Vue.js 3** - Progressive JavaScript framework
- **Vue Router** - Client-side routing
- **Tailwind CSS** - Utility-first CSS framework
- **Axios** - HTTP client
- **Vite** - Next-generation frontend tooling

## 📋 Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone 
cd mayomi-nishat-agro
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install dependencies
pip install -r requirements.txt

# Run the server
python main.py
```

The backend will run on `http://localhost:8000`

### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

The frontend will run on `http://localhost:3000`

## 🌐 Production Build

### Backend

```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
npm run build
npm run preview
```

## 📱 Features Overview

### 1. Home Page
- Hero section with call-to-action
- Feature highlights
- Product preview grid
- Farm goals section

### 2. Products Page
- Complete product catalog
- Category filtering (Fish, Dairy, Poultry, Crops, Fruits)
- Product detail modal
- Direct order buttons

### 3. About Page
- Farm information
- Detailed farm activities
- Goals and objectives

### 4. Contact Page
- Contact form
- Contact information
- Business hours
- Location map placeholder

### 5. Chatbot
- Floating chat button
- Interactive conversation
- Product inquiries
- Contact information

## 🎨 Design Features

- **Color Scheme**: Green (Primary) and Orange (Secondary)
- **Typography**: Poppins (English) and Noto Sans Bengali (Bengali)
- **Animations**: Smooth fade-ins, hover effects, and transitions
- **Icons**: Emoji-based icons for better accessibility
- **Responsive Grid**: Mobile-first approach

## 📞 Contact Information

- **Phone**: +8801711727357
- **Email**: nishat@manishatagro.com
- **Location**: Vabakhali bazar

## 🔧 Customization

### Adding New Products

Edit `backend/main.py` and add to the `products` list:

```python
{
    "id": 9,
    "name": "Product Name",
    "name_bn": "পণ্যের নাম",
    "category": "category_name",
    "description": "Product description",
    "description_bn": "পণ্যের বিবরণ",
    "image": "https://image-url.com",
    "price": 100
}
```

### Changing Colors

Edit `frontend/tailwind.config.js`:

```javascript
colors: {
  primary: {
    // Your colors here
  }
}
```

### Modifying Chatbot Responses

Edit the `chat` function in `backend/main.py`:

```python
responses = {
    "keyword": "Response in Bengali"
}
```

## 📄 API Endpoints

- `GET /` - API info
- `GET /api/products` - Get all products
- `GET /api/products/{id}` - Get specific product
- `GET /api/products?category=fish` - Filter by category
- `POST /api/chat` - Chat with bot
- `POST /api/contact` - Submit contact form

## 🐛 Troubleshooting

### Backend Issues

If you get CORS errors:
```python
# CORS is already configured in main.py
# Make sure frontend is running on port 3000
```

### Frontend Issues

If pages don't load:
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```
