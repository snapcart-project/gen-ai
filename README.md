Snapchart Connect

AI-first marketplace empowering Indian artisans with zero-typing onboarding.
Artisans upload a photo + voice note, and Snapchart Connect transforms it into a polished, multilingual product story, enhanced visuals, and a shareable product page with live buyer connect.

🌍 Problem Statement

Indian artisans face three key challenges:

Poor product presentation → photos don’t capture authenticity.

Language & literacy barriers → difficult to write product descriptions.

Lack of visibility on e-commerce → small creators get buried under mass-produced goods.

The real problem isn’t lack of talent — it’s lack of a voice.

💡 Solution

Snapchart Connect is a zero-typing, AI-powered storytelling engine that bridges artisans with global markets.

Upload photo + voice note, AI does the rest.

Generates multilingual product stories, captions, hashtags, and pricing insights.

Enhances photos while keeping originals visible for authenticity.

Publishes a QR-based product page with a “Join Live” button for buyers to connect directly.

Provides buyer interaction bot + real-time live sessions with transcription and translation.

🚀 Features
✅ Core MVP (Built)

Voice-to-Story AI → Voice → Text → Multilingual Story.

Image Enhancement → Background cleanup, lighting/shadow adjustment, tag extraction.

Product Page → Original + enhanced photo, story, hashtags, QR code.

Live Window → Buyer ↔ Artisan real-time connect via Google Meet.

Buyer Bot → Answers FAQs from product data.

Lightweight PWA → Buyers can access without heavy app install.

🔮 Future Vision

Dynamic Storytelling → Personalized stories for each buyer.

Generative Marketing Assets → Auto-create social posts, videos, and campaigns.

AI Business Insights → Pricing intelligence + market trend analytics.

Interactive Live AI → Real-time transcription + translation during live sessions.

AR/VR Integration → Virtual try-on for crafts like jewelry & textiles.

🏗️ System Architecture

Users:

Artisan (uploads photo + voice)

Buyer (scans QR, views product page, joins live)

Frontend:

React / JavaScript PWA

Upload screen, Preview screen, Product page with Live Connect

Backend:

Flask (Python) → Voice-to-Story service

Node.js + Express → REST APIs & DB integration

Supabase / Firestore → Product metadata & artisan profiles

Cloud Functions + Cloud Storage → Image pipeline triggers & storage

Google Cloud Services:

Vertex AI (Gemini) → Story generation + captions

Speech-to-Text API → Voice transcription

Vision AI → Image enhancement & tagging

Dialogflow CX → Buyer Bot

Google Meet / WebRTC API → Live Connect

Firestore Database → Product metadata + user interactions

🛠️ Tech Stack

Frontend: React, HTML, CSS, JavaScript
Backend: Python (Flask), Node.js (Express)
Database: Supabase (Postgres), Firestore
Cloud & AI: Google Cloud Services

Vertex AI (Gemini)

Cloud Speech-to-Text

Vision AI

Dialogflow CX

Firestore, Cloud Storage, Cloud Functions, Google Meet API
DevOps: Git + GitHub, Thunder Client/Postman, Ngrok (for local demo), Google Cloud Run (for deployment)

🔄 Process Flow

Artisan uploads photo + voice note.

AI enhances image + transcribes and translates voice.

AI generates story, captions, hashtags, pricing tips.

Backend creates product page (with original + enhanced photo, QR code, Join Live).

Buyer scans QR → views story-driven product page.

Buyer interacts via FAQ Bot or joins Live session.

Artisan receives buyer feedback + AI insights.

📱 Wireframes / Mockups

Upload Screen → Upload photo, record voice.

Preview Screen → Original vs AI-enhanced photo, generated story.


📊 Cost Estimation

Prototype (Hackathon): Free (Google Cloud Free Tier)

Early Deployment (~500 artisans): <$250/month

Scale: ~$1–2/user/month, usage-based


📬 Contacts

Team Name: Bytestack

Team Leader: Priyanka Yadav
Team members: payel bera, tanya, palak , maitri , priyanka

Product Page → Enhanced photo, hashtags, QR, Join Live button.

Buyer Interaction → Bot chat + Live video connect.
